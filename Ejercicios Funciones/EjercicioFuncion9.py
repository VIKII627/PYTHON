# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo. 

def funCalcular(numero1, numero2):
    def mcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def mcm(a, b):
        return abs(a * b) // mcd(a, b)

    return mcd(numero1, numero2), mcm(numero1, numero2)

resultado_mcd, resultado_mcm = funCalcular(12, 15)
print("Máximo Común Divisor (MCD):", resultado_mcd)
print("Mínimo Común Múltiplo (MCM):", resultado_mcm)