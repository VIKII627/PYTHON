#Ejercicio 4
#Escribir un programa que pregunte al usuario los números ganadores de la lotería
#primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
#a mayor.

numeros = []
for i in range(6):
    numero = int(input("Introduce el número ganador " + str(i+1) + ": "))
    numeros.append(numero)
numeros.sort()

print("Los números ganadores ordenados de menor a mayor son:")

for numero in numeros:
    print(numero)
