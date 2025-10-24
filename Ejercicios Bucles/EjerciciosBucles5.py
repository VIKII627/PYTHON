#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
#año que dura la inversión.

cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (en %): "))
años = int(input("Introduce el número de años: "))

for i in range(1, años + 1):
    cantidad += cantidad * (interes / 100)
    print("Después de", i, "años, el capital es:", round(cantidad, 2))