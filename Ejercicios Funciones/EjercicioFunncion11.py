# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia.
# Escribir otra función que reciba el diccionario generado con la función anterior 
# y devuelva una tupla con la palabra más repetida y su frecuencia. 

def funDiccionario():
    def contar_palabras(cadena):
        palabras = cadena.split()
        frecuencia = {}
        for palabra in palabras:
            palabra = palabra.lower().strip('.,!?;"()[]{}')  # Normalizar palabras
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1
        return frecuencia

    def palabra_mas_repetida(diccionario):
        max_palabra = max(diccionario, key=diccionario.get)
        return (max_palabra, diccionario[max_palabra])

    cadena = "Este es un ejemplo. Este ejemplo es simple. Simple es mejor que complicado."
    diccionario_frecuencia = contar_palabras(cadena)
    return diccionario_frecuencia, palabra_mas_repetida(diccionario_frecuencia)

diccionario_resultado, palabra_frecuente = funDiccionario()
print("Diccionario de Frecuencia de Palabras:", diccionario_resultado)
print("Palabra más Repetida y su Frecuencia:", palabra_frecuente)