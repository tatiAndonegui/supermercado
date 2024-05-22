import sqlite3

class Conexion:
    #constructor de conexion a la bd
    def __init__(self,nombre_bd):
        self.conexion=sqlite3.connect(nombre_bd)
        self.cursor=self.conexion.cursor()

    #cierra la conexion a la bd
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()