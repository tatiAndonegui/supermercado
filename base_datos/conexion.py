import sqlite3

class Conexion:
    #constructor de conexion a la bd
    def __init__(self,nombre_bd):
        self.conexion=sqlite3.connect(nombre_bd)
        self.cursor=self.conexion.cursor()

    def crear_tabla_clientes(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes(nombre TEXT, apellido TEXT, dni TEXT)''')
        self.conexion.commit()
    
    def agregar_clientes(self,nombre,apellido,dni):
        self.cursor.execute('''INSERT INTO clientes VALUES(?,?,?)''',(nombre , apellido , dni))
        self.conexion.commit()

    def mostrar_clientes(self):
        self.cursor.execute('''SELECT * FROM clientes''')
        clientes=self.cursor.fetchall()
        return clientes
    
    def editar_cliente(self,nombre,apellido,dni):
        self.cursor.execute('''UPDATE clientes SET nombre=?,apellido=?,dni=? WHERE dni=?''', (nombre,apellido,dni,dni))
        self.conexion.commit()

    def eliminar_cliente(self,dni):
        self.cursor.execute('''DELETE FROM clientes WHERE dni=? ''',(dni,))
        self.conexion.commit()
        
    #cierra la conexion a la bd
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
    