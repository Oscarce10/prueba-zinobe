import sqlite3
from sqlite3 import Error

class ConexionDB():
    # Todos los atributos propios de la clase deben ir precedidos por self.
    def __init__(self):
        self.con = sqlite3.connect('database.db')
        self.cursor = self.con.cursor()

    def crearTabla(self):
        self.cursor.execute("CREATE TABLE tabla (id integer PRIMARY KEY AUTOINCREMENT, region text, country text, language text, time text)")

    def insertarFila(self, fila):
        self.cursor.execute("INSERT INTO tabla (region, country, language, time) VALUES (?, ?, ?, ?)", fila)

    def mostrarFilas(self):
        self.cursor.execute("SELECT * FROM tabla")
        rows = self.cursor.fetchall()
        return rows

