# Escribir una función que reciba un número entero positivo y devuelva su factorial. 

def funFactorial(numero):
    if numero < 0:
        return "El número debe ser un entero positivo."
    elif numero == 0 or numero == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, numero + 1):
            factorial *= i
        return factorial

print(funFactorial(5))