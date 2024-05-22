from base_datos.conexion import Conexion 

print("Bienvenidos al sistema del Supermercado")

opcion=1
while (opcion!=0):
    try:
        opcion=input("Escoja una opción: \n 1- Agregar cliente \n 2- Editar cliente \n 3-Eliminar cliente")
    except:
        print("Ingrese opcion valida")



print("Estas fuera del sistema")