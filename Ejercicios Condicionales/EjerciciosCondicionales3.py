num1 = float(input("Ingrese el primer número (dividendo): "))   
num2 = float(input("Ingrese el segundo número (divisor): "))

if num2 != 0:
    resultado = num1 / num2
    print ("El resultado de la división es:", resultado)
else:
    print ("Error: No se puede dividir por cero.")
