# Importar modulos
import pandas as pd
import time
import hashlib
# Modulo de la api
import api_module as api
# Modulo de bd sqlite
from db_module import ConexionDB

# 1. De https://rapidapi.com/apilayernet/api/rest-countries-v1, 
# obtenga todas las regiones existentes.

# Almacenar la respuesta json de la api en un dataframe
df = pd.read_json(api.getRegiones()) 

# Mostrar 5 primeras tuplas del dataframe
# print(df.head())

# Mostrar las columnas del dataframe
# print(df.columns)

# Obtener las regiones existentes y su numero de apariciones
# print(df["region"].value_counts())


# 2. De https://restcountries.eu/ Obtenga un pais por region apartir de la region obtenida del punto 1.

# Consultar tipo de dato del metodo value_counts(): Series
# print(type(df["region"].value_counts()))

# Traer las regiones que son las keys del diccionario y asignarlas a una variable como una lista
regiones = df["region"].value_counts().keys().to_list()
# print(regiones)

# Dado a que hay una region sin nombre en la lista y que puede suponer un problema a la hora de consultar los paises en la api, esta se saca de la lista
#if "" in regiones:
 #   regiones.remove("")
#print(regiones)

# Se iteran las regiones en la lista y por cada una se llama la api y pasando como argumento cada region, se devuelve un solo pais

# Se crea un variable que almacenará las filas a almacenar en el dataframe
filas = []
for region in regiones:
    try:
        # En tal caso que no se haya limpiado la lista de regiones y se detecte una region nula o sin nombre, para evitar errores se evalua dentro
        # de un try-catch usando la funcion assert() que evalua valores y devuelve una excepcion AssertionError la cual evita que enviemos a la api
        # valores vacios o nulos y se nos generen problemas
        assert(region)
        # Comienzo el reloj para calcular el tiempo que tarda cada tupla en generarse
        start_time = time.time()
        pais = api.getPaisPorRegion(region)
        # print(pais)

        # 3. De https://restcountries.eu/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
        # Ahora vuelvo a llamar a la api y esta vez le paso como argumento cada pais con el fin de retornar el lenguaje que habla
        lenguaje = api.getLanguage(pais)
        # print(f"{region} -> {pais} -> {lenguage}")

        # Encripto el lenguage con SHA1
        lenguaje = hashlib.sha1(lenguaje.encode('UTF-8')).hexdigest()
        # print(lenguage)

        # 4. En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)

        # Al tiempo que se hace esto se almacena la fila en el la lista de las filas
        filas.append([region, pais, lenguaje, time.time() - start_time])
        
    except AssertionError:
        # print("Region vacia")
        pass  
        
# Se crea el dataframe a mostrar como resultado, se le agregan las columnas y se rellena con las filas
dataframe = pd.DataFrame(filas, columns=["Region", "Country", "Language", "Time"])
print(dataframe)

# 6. Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
print(f"Tiempo total: {dataframe['Time'].sum()} s")
print(f"Tiempo promedio: {dataframe['Time'].mean()} s")
print(f"Tiempo minimo: {dataframe['Time'].min()} s")
print(f"Tiempo maximo: {dataframe['Time'].max()} s")

# Insertar todas las filas en una base de datos sqlite
db = ConexionDB()

# Crear tabla
db.crearTabla()

# Por cada fila que hay en el array de filas se envia para ser almacenada en la bd
for i in filas:
    db.insertarFila(i)

# Se muestra la tabla

print("----------- Tabla de sqlite ----------------")
for i in db.mostrarFilas():
    print(i)


# 8. Genere un Json de la tabla creada y guardelo como data.json

# Se usa el metodo de pandas.DataFrame.to_json que nos permite exportar el dataframe creado en formato json y como argumento se pasa destino y nombre de archivo
dataframe.to_json(r'data.json')

# Se evalua el archivo json generado
print('--------- Dataframe from data.json ----------')
print(pd.read_json('data.json'))