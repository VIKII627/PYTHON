## Programa de Gestión de Clientes

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
    
    # Manejo de error si la entrada no es un número o está fuera de rango
    opcion = input("Elige una opción (1-6): ")
    if not opcion.isdigit():
        print("Opción inválida. Introduce un número del 1 al 6.")
        continue
    opcion = int(opcion)
    if opcion < 1 or opcion > 6:
        print("Opción inválida. Introduce un número del 1 al 6.")
        continue

    # --- (1) Añadir cliente ---
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
        
        # Almacena el cliente
        clientes[nif] = datos_cliente
        print(f"Cliente {nombre} ({nif}) añadido/actualizado correctamente.")

    # --- (2) Eliminar cliente ---
    elif opcion == 2:
        nif_eliminar = input("Dime el NIF del cliente que deseas eliminar: ").upper()
        
        if nif_eliminar in clientes:
            nombre_eliminado = clientes[nif_eliminar]["nombre"]
            del clientes[nif_eliminar]
            print(f"Cliente {nombre_eliminado} ({nif_eliminar}) eliminado correctamente.")
        else:
            print(f"Error: No se encontró ningún cliente con el NIF {nif_eliminar}.")

    # --- (3) Mostrar cliente ---
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

    # --- (4) Listar todos los clientes ---
    elif opcion == 4:
        if clientes:
            print("\n--- Listado de Todos los Clientes ---")
            # Iterar sobre la base de datos
            for nif, datos in clientes.items():
                print(f"NIF: {nif}, Nombre: {datos['nombre']}")
            print("-------------------------------------")
        else:
            print("La base de datos de clientes está vacía.")

    # --- (5) Listar clientes preferentes ---
    elif opcion == 5:
        preferentes_encontrados = False
        print("\n--- Listado de Clientes Preferentes ---")
        
        # Iterar sobre la base de datos principal y filtrar
        for nif, datos in clientes.items():
            if datos["preferente"]:
                print(f"NIF: {nif}, Nombre: {datos['nombre']}")
                preferentes_encontrados = True
        
        if not preferentes_encontrados:
            print("No hay clientes marcados como preferentes.")
        print("---------------------------------------------")

    # --- (6) Terminar ---
    elif opcion == 6:
        print("Saliendo del programa. ¡Hasta pronto!")
        break