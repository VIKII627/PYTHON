# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal. 

def funConvertir(numero):
    def decimal_a_binario(n):
        return bin(n).replace("0b", "")

    def binario_a_decimal(b):
        return int(b, 2)

    return decimal_a_binario(numero), binario_a_decimal(str(numero))

resultado_binario, resultado_decimal = funConvertir(10)
print("Decimal a Binario:", resultado_binario)
print("Binario a Decimal:", resultado_decimal)