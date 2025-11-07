#Ejercicio 9 Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
#Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura.
#El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
#Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
#Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 
#Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

facturas = {}
cantidad_cobrada = 0.0

#Antes de procesar la acción, mostramos el estado actual tanto del dinero que nos queda por cobrar como del que ya hemos cobrado

while True:
    cantidad_pendiente = sum(facturas.values())
    print(f"Cantidad cobrada hasta el momento: {cantidad_cobrada:.2f}")
    print(f"Cantidad pendiente de cobro: {cantidad_pendiente:.2f}")
    accion = input("¿Quieres añadir una nueva factura (a), pagar una existente (p) o terminar (t)? ").lower()

    if accion == 'a':
        numero_factura = input("Introduce el número de factura: ")
        coste_factura = float(input("Introduce el coste de la factura: "))
        facturas[numero_factura] = coste_factura
        print(f"Factura {numero_factura} añadida con coste {coste_factura:.2f}.")

    elif accion == 'p':
        numero_factura = input("Introduce el número de factura a pagar: ")
        if numero_factura in facturas:
            cantidad_cobrada += facturas[numero_factura]
            del facturas[numero_factura]
            print(f"Factura {numero_factura} pagada.")
        else:
            print("La factura no existe.")

    elif accion == 't':
        break

    else:
        print("Acción no válida. Por favor, elige 'a', 'p' o 't'.")

    cantidad_pendiente = sum(facturas.values())
    print(f"Cantidad cobrada hasta el momento: {cantidad_cobrada:.2f}")
    print(f"Cantidad pendiente de cobro: {cantidad_pendiente:.2f}")

print("Programa terminado.")