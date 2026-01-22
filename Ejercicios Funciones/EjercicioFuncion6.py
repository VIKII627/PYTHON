# Escribir una función que reciba una muestra de números en una lista y devuelva su media

def funMedia(lista):
    if not lista:
        return 0
    suma = sum(lista)
    media = suma / len(lista)
    return media

print(funMedia([10, 20, 30, 40, 50]))