#Ejercicio 12
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
#muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
contador = 0

i = 0
while i < len(frase):
    if frase[i] == letra:
        contador += 1
    i += 1

print(f"La letra '{letra}' aparece {contador} veces en la frase.")