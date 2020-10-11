import sqlite3
from sqlite3 import Error

class ConexionDB():
    # Todos los atributos y metodos propios de la clase deben ir precedidos por self.
    
    def __init__(self):
        try:
            self.con = sqlite3.connect("../db/database.db")
        except Exception as e:
            print(e)

    def abrir(self):
        self.con = sqlite3.connect('../db/database.db')
        # Cursor class is an instance using which you can invoke methods that execute SQLite statements, fetch data from the result sets of the queries.
        self.cursor = self.con.cursor()

    def cerrar(self):
        self.con.close()

    # Siempre que se va a efectuar una operacion sobre la bd se abre la conexion e independientemente de si hay algun error o se completa el trabajo se cierra la conexion

    def crearTabla(self):
        try:
            self.abrir()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS tabla (id INTEGER PRIMARY KEY AUTOINCREMENT, region TEXT, country TEXT, language TEXT, time REAL)")
            self.con.commit()
        except Exception as error:
            print ("Error creando tabla", error)
        finally:
            self.cerrar()

    def insertarFila(self, fila):
        try:
            self.abrir()
            self.cursor.execute(f"INSERT INTO tabla (region, country, language, time) VALUES (?, ?, ? ,?)", fila)
            self.con.commit()
        except Exception as error:
            print ("Error insertando fila", error)
        finally:
            self.cerrar()

    def mostrarFilas(self):
        try:
            self.abrir()
            self.cursor.execute(f"SELECT * FROM tabla")
            rows = self.cursor.fetchall()
            return rows        
        except Exception:
            print ("Error mostrando filas", error)
        finally:
            self.cerrar()