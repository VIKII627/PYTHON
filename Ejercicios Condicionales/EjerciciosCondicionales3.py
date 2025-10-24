#Ejercicio 3
#Escribir un programa que pida al usuario dos números y muestre por pantalla su
#división. Si el divisor es cero el programa debe mostrar un error.

num1 = float(input("Ingrese el primer número (dividendo): "))   
num2 = float(input("Ingrese el segundo número (divisor): "))

if num2 != 0:
    resultado = num1 / num2
    print ("El resultado de la división es:", resultado)
else:
    print ("Error: No se puede dividir por cero.")
