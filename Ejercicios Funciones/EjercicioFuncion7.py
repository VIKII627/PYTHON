# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados. 

def funCuadrados(lista):
    if not lista:
        return 0
    cuadrados = [x ** 2 for x in lista]
    return cuadrados

print(funCuadrados([1, 2, 3, 4, 5]))