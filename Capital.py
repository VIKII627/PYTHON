#Escribir un programa que pregunte al usuario una cantidad a invertir, el interes anual y el nunmero de años, y muestre por pantalla el capital obtenido en la inversion.

capital = float(input("Cantidad a invertir: "))
Tinteres = float(input("Interes anual (en porcentaje): "))
años = int(input("Numero de años: "))
interes = capital * ((Tinteres / 100) * años)
print("El capital obtenido en la inversion es: {:.2f} euros".format(capital + interes))