from base_datos.conexion import Conexion 

print("Bienvenidos al sistema del Supermercado")

opcion=0
while (opcion!=5):
    try:
        opcion=input("Escoja una opción:\n 1- Agregar cliente \n 2- Editar cliente\n 3-Eliminar cliente\n 4-Mostrar clientes \n 5- Salir\n")
        if (opcion =="1"):
            nombre=print("Ingrese el nombre del cliente")
            apellido=print("Ingrese el apellido del cliente")
            dni=print("Ingrese el dni del cliente")
            conexion=Conexion("base_datos/supermercado.db")
            conexion.crear_tabla_clientes()
        if (opcion =="5"):
            print("saliendo")
    except:
        print("Ingrese opcion valida")

print("Estas fuera del sistema")