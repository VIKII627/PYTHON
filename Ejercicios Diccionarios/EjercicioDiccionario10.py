# Ejercicio 10 Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor 
# será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
# donde preferente tendrá el valor True si se trata de un cliente preferente. 
# El programa debe preguntar al usuario por una opción del siguiente menú: 
# (1) Añadir cliente, 
# (2) Eliminar cliente, 
# (3) Mostrar cliente, 
# (4) Listar todos los clientes, 
# (5) Listar clientes preferentes, 
# (6) Terminar. 
#
# En función de la opción elegida el programa tendrá que hacer lo siguiente: 
# 1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos. 
# 2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos. 
# 3. Preguntar por el NIF del cliente y mostrar sus datos. 
# 4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre. 
# 5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre. 
# 6. Terminar el programa. 

clientes = {}
datos_cliente = {}

while True:
    print("\nMenú de opciones:")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        nif = input("Introduce NIF del cliente: ")
        nombre = input("Introduce el nombre del cliente: ")
        direccion = input("Introduce la dirección del cliente: ")
        telefono = input("Introduce el teléfono del cliente: ")
        correo = input("Introduce el correo del cliente: ")
        preferente_input = input("¿Es un cliente preferente? (s/n): ")
        preferente = True if preferente_input.lower() == "s" else False

        datos_cliente = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "preferente": preferente
        }

    if opcion == 2:
        eliminar = input("Dime el NIF del cliente que deseas eliminar: ")
        clientes.pop(eliminar)

    if opcion == 3:
        mostrar = input("Dime el NIF del cliente que deseas mostrar: ")
        print(clientes[mostrar])

    if opcion == 4:
        print(clientes)

    if opcion == 5:
        if datos_cliente.get("preferente"):
            print(f"NIF: {nif}, Nombre: {datos_cliente.get('nombre')}")
    
    if opcion == 6:
        print("Saliedo del programa")
        break