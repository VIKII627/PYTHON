#Ejercicio 6
#Escribir un programa que lea un entero positivo, , introducido por el usuario y
#después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La
#suma de los primeros enteros positivos puede ser calculada de la siguiente forma:

numero = int(input("Introduce un número entero positivo: "))
suma = numero * (numero + 1) / 2
print("La suma de los números enteros desde 1 hasta", numero, "es:", str(suma))