#Ejercicio 5
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
#ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que
#pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el
#usuario tiene que tributar o no.

edad = int(input("Por favor, ingrese su edad: "))
ingresosM = float(input("Por favor, ingrese sus ingresos mensuales: "))

if edad > 16 and ingresosM >= 1000:
    print("Puede tributar.")
else:
    print("No puede tributar.")