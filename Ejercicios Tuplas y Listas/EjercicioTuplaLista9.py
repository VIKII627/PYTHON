#Ejercicio 9 Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
palabra = input("Introduce una palabra: ").lower()
vocales = "aeiou"
conteo_vocales = {vocal: palabra.count(vocal) for vocal in vocales}
for vocal, conteo in conteo_vocales.items():
    print(f"La vocal '{vocal}' aparece {conteo} veces.") 