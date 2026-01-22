# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

def funMostrar(lista):
    if not lista:
        return 0
    n = len(lista)
    media = sum(lista) / n
    varianza = sum((x - media) ** 2 for x in lista) / n
    desviacionT = varianza ** 0.5
    resultado = {
        'media': media,
        'varianza': varianza,
        'desviacion_tipica': desviacionT
    }
    return resultado

print (funMostrar([10, 20, 30, 40, 50]))