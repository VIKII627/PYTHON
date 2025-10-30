#Ejercicio 8 Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
palabra = input("Introduce una palabra: ")
if palabra == palabra[::-1]:
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")