'''
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes 
se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro 
diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente 
tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una 
opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos 
los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa 
tendrá que hacer lo siguiente:

1 Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
2 Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
3 Preguntar por el NIF del cliente y mostrar sus datos.
4 Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
5 Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
6 Terminar el programa.
'''

from http import client


clientes = {}
continuar = True

while continuar:
    respuesta = input('''\n¿Qué desea realizar?\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5)Listar clientes preferentes\n(6)Terminar\nRespuesta: ''')
    #Respuesta 1: Añadir cliente
    if respuesta.lower() == "1":
        nif = input("\nIngrese el NIF del usuario: ")
        datos_cliente = {}
        datos_cliente["nombre"] = input("Ingrese el nombre del cliente: ")
        datos_cliente["dirección"] = input("ingrese la dirección del cliente: ")
        datos_cliente["teléfono"] = input("Ingrese el teléfono del cliente: ")
        datos_cliente["correo"] = input("Ingrese el correo del cliente: ")        
        preferente = input("El cliente es preferente (si/no): ")
        if preferente.lower() == "si":
            datos_cliente["preferente"] = True
        else:
            datos_cliente["preferente"] = False
        clientes[nif] = datos_cliente
        print("\nCliente añadido con éxito...")
    #Respuesta 2: Eliminar cliente
    elif respuesta.lower() == "2":
        nif = input("\nIngrese el NIF del usuario a eliminar: ")
        #Si el NIF se encuentra en el diccionario
        if nif in clientes:
            resultado = clientes.pop(nif, True)
            print("\nEl usuario %s fue eliminado de la base de datos" % nif)
        else:
            print("\nEl usuario no se encuentra en la base de datos")            
    #Respuesta 3: Mostrar cliente
    elif respuesta.lower() == "3":
        nif = input("\nIngrese el NIF del usuario a mostrar: ")
        #Si el nif se encuentra en el diccionario
        if nif in clientes:
            usuario = clientes[nif]
            print("\nNombre: %s\nDirección: %s\nTeléfono: %s\nCorreo: %s\nPreferente: %s" % (usuario['nombre'], usuario['dirección'], usuario['teléfono'], usuario['correo'], str(usuario['preferente'])))
        else:
            print("El usuario no se encuentra en la base de datos")
    #Respuesta 4: Listar todos los clientes
    elif respuesta.lower() == "4":
        print("")
        for nif in list(clientes.keys()):
            print("\nNIF: %s" % nif)
            datos = clientes[nif]
            #Imprimiendo los datos del usuario
            print("Nombre: %s" % (datos['nombre']))
            print("Dirección: %s" % datos['dirección'])
            print("Teléfono: %s" % datos['teléfono'])
            print("Correo: %s" % datos['correo'])
            print("Preferente: %s" % str(datos['preferente']))    
    #Respuesta 5: Listar clientes preferentes
    elif respuesta.lower() == "5":
        print("")
        for nif in list(clientes.keys()):
            datos = clientes[nif]
            #Si el cliente es preferente, se imprimen sus datos
            if datos['preferente']:
                print("NIF: %s" % nif)
                print("Nombre: %s" % (datos['nombre']))
                print("Dirección: %s" % datos['dirección'])
                print("Teléfono: %s" % datos['teléfono'])
                print("Correo: %s" % datos['correo'])
                print("Preferente: %s" % str(datos['preferente']))  
    #Respuesta 6: Terminar aplicación
    elif respuesta.lower() == "6":
        continuar = False
    #No selecciona una opción válidad
    else:
        print("\nDebes seleccionar una opción válida...")
    