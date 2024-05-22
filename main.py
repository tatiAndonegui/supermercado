from base_datos.conexion import Conexion 

print("Bienvenidos al sistema del Supermercado")

opcion=0
while (opcion!=5):
    try:
        opcion=input("Escoja una opción:\n 1- Agregar cliente \n 2- Editar cliente\n 3-Eliminar cliente\n 4-Mostrar clientes \n 5- Salir\n")
        if (opcion =="1"):
            nombre=input("Ingrese el nombre del cliente ")
            apellido=input("Ingrese el apellido del cliente ")
            dni=input("Ingrese el dni del cliente ")
            conexion=Conexion("base_datos/supermercado.db")
            conexion.crear_tabla_clientes()
            conexion.agregar_clientes(nombre,apellido,dni)

        if (opcion =="2"):
            dni=input("Ingrese el dni del cliente a editar: ")
            clientes=conexion.mostrar_clientes()
            for cliente in clientes:
                if(clientes[2]==dni):
                    nombre=input("Ingrese el nombre del cliente a editar ")
                    apellido=input("Ingrese el apellido del cliente a editar ")
                    print("Cliente actualizado correctamente")
            
        if (opcion =="3"):
            input("Ingrese el dni del cliente a eliminar")
            conexion.eliminar_cliente(dni)

        if (opcion =="4"):
            clientes=conexion.mostrar_clientes()
            for cliente in clientes:
                print(cliente)

        if (opcion =="5"):
            print("saliendo")
        
    except:
        print("Ingrese opcion valida")

print("Estas fuera del sistema")