#Ejercicio 8
#Escribir un programa que pida al usuario un número entero y muestre por pantalla
#un triángulo rectángulo como el de más abajo.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

altura = int(input("Introduce la altura del triángulo: "))

for i in range(1, altura + 1):  
    for j in range(2 * i - 1, 0, -2):
        if j > 1:
            print(j, end = " ")
        else:
            print(j)