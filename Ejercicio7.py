peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))
imc = peso / (altura ** 2)
print("Tu indice de mas corporal es: {:.2f}".format(imc))