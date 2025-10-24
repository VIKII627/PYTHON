#Ejercicio 4
#Los teléfonos de una empresa tienen el siguiente formato
#prefijo-número-extension donde el prefijo es el código del país +34, y la
#extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un
#programa que pregunte por un número de teléfono con este formato y muestre por
#pantalla el número de teléfono sin el prefijo y la extensión.

telefono = input("Introduce un número de teléfono con el formato +34-913724710-56: ")
print("El número de teléfono sin el prefijo y la extensión es:", telefono[4:-3])