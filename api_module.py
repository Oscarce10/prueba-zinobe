import requests
import random
import json

# Llamar la api y devolver las regiones en formato json no recibe parametros

def getRegiones():
    url = "https://restcountries-v1.p.rapidapi.com/all"

    headers = {
        'x-rapidapi-host': "restcountries-v1.p.rapidapi.com",
        'x-rapidapi-key': "ce35d55362mshc5290db67bdff6ep1a3e8cjsn05666fb3e1a0"
        }

    response = requests.request("GET", url, headers=headers)
    return response.text

# Se llama la api y pasandole la region como argumento esta la consulta y devuelve un solo pais escogido al azar de la lista de paises que devuelve la api
def getPaisPorRegion(region):
    url = f"https://restcountries.eu/rest/v2/region/{region}"
    response = requests.get(url)
    # Se devuelve el indice de un pais tomado al azar de la longitud de paises devueltos todo esto usando el modulo json de python. Se busca en el diccionario el nombre del 
    # pais y es lo que se retorna
    respuesta = json.loads(response.text)
    return(respuesta[random.randint(0, len(respuesta) - 1)]["name"])

# Se llama la api y pasandole el pais como argumento esta funcion la consulta y devuelve el lenguaje hablado en el pais
def getLanguage(country):
    # You can filter the output of your request to include only the specified fields.
    url = f"https://restcountries.eu/rest/v2/name/{country}?fields=languages"
    response = requests.get(url)
    # print(json.loads(response.text)) # retorna array
    # print(json.loads(response.text)[0]) # retorna un diccionario
    # print(json.loads(response.text)[0]["languages"]) # retorna array
    # print(json.loads(response.text)[0]["languages"][0]) # retorna diccionario
    # print(json.loads(response.text)[0]["languages"][0]["name"]) # obtengo el campo que requiero 

    # Despues de saber como obtener el lenguaje del archivo json retornado por la api lo devuelvo en la función
    return json.loads(response.text)[0]["languages"][0]["name"]

    


