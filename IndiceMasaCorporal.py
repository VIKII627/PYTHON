#Escribir un programa en python que pida al usuario su peso (en kg) y su altura (en metros), calcule su indice de masa corporal y lo almacene en una variable
# y muestre por pantalla la frase "Tu indice de masa corporal es <imc>" donde <imc> es el indice de masa corporal calculado con dos decimales.

peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
imc = peso / (altura ** 2)
print("Tu indice de mas corporal es: {:.2f}".format(imc))