# Ejercicio 10 Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario 
# con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor 
# True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: 
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

while True:
    print("\n--- Menú de opciones ---")
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    print("------------------------")
    
    opcion = input("Elige una opción (1-6): ")
    if not opcion.isdigit():
        print("Opción inválida. Introduce un número del 1 al 6.")
        continue
    opcion = int(opcion)
    if opcion < 1 or opcion > 6:
        print("Opción inválida. Introduce un número del 1 al 6.")
        continue

    if opcion == 1:
        nif = input("Introduce NIF del cliente: ").upper()
        
        if nif in clientes:
            print(f"El cliente con NIF {nif} ya existe. Se actualizarán sus datos.")

        nombre = input("Introduce el nombre del cliente: ")
        direccion = input("Introduce la dirección del cliente: ")
        telefono = input("Introduce el teléfono del cliente: ")
        correo = input("Introduce el correo del cliente: ")
        
        preferente_input = input("¿Es un cliente preferente? (s/n): ").lower()
        preferente = (preferente_input == "s")

        datos_cliente = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "preferente": preferente
        }

        clientes[nif] = datos_cliente
        print(f"Cliente {nombre} ({nif}) añadido/actualizado correctamente.")

    elif opcion == 2:
        nif_eliminar = input("Dime el NIF del cliente que deseas eliminar: ").upper()
        
        if nif_eliminar in clientes:
            nombre_eliminado = clientes[nif_eliminar]["nombre"]
            del clientes[nif_eliminar]
            print(f"Cliente {nombre_eliminado} ({nif_eliminar}) eliminado correctamente.")
        else:
            print(f"Error: No se encontró ningún cliente con el NIF {nif_eliminar}.")

    elif opcion == 3:
        nif_mostrar = input("Dime el NIF del cliente que deseas mostrar: ").upper()
        
        if nif_mostrar in clientes:
            datos = clientes[nif_mostrar]
            print("\n--- Datos del Cliente ---")
            print(f"NIF: {nif_mostrar}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Dirección: {datos['direccion']}")
            print(f"Teléfono: {datos['telefono']}")
            print(f"Correo: {datos['correo']}")
            print(f"Preferente: {"Sí" if datos["preferente"] else "No"}")
            print("-------------------------")
        else:
            print(f"Error: No se encontró ningún cliente con el NIF {nif_mostrar}.")

    elif opcion == 4:
        if clientes:
            print("\n--- Listado de Todos los Clientes ---")
            for nif, datos in clientes.items():
                print(f"NIF: {nif}, Nombre: {datos['nombre']}")
            print("-------------------------------------")
        else:
            print("La base de datos de clientes está vacía.")

    elif opcion == 5:
        preferentes_encontrados = False
        print("\n--- Listado de Clientes Preferentes ---")
        
        for nif, datos in clientes.items():
            if datos["preferente"]:
                print(f"NIF: {nif}, Nombre: {datos['nombre']}")
                preferentes_encontrados = True
        
        if not preferentes_encontrados:
            print("No hay clientes marcados como preferentes.")
        print("---------------------------------------------")

    elif opcion == 6:
        print("Saliendo del programa. ¡Hasta pronto!")
        break