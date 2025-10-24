#Ejercicio 11
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
#una a una las letras de la palabra introducida empezando por la última.

palabra = input("Introduce una palabra: ")
longitud = len(palabra) 

while longitud > 0:
    print(palabra[longitud - 1])
    longitud -= 1
    