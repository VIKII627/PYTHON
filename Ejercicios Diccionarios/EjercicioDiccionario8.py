#Ejercicio 8 Escribir un programa que cree un diccionario de traducción español-inglés. 
#El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada 
#par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. 
#Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
#Si una palabra no está en el diccionario debe dejarla sin traducir. 

traducciones_input = input("Introduce las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas: ")
traducciones_lista = traducciones_input.split(',')
diccionario_traduccion = {}

for item in traducciones_lista:
    palabra_es, palabra_en = item.split(':')
    diccionario_traduccion[palabra_es.strip()] = palabra_en.strip()

frase_espanol = input("Introduce una frase en español para traducir: ")
palabras_frase = frase_espanol.split()
frase_traducida = []

for palabra in palabras_frase:
    traduccion = diccionario_traduccion.get(palabra, palabra)
    frase_traducida.append(traduccion)
frase_final = ' '.join(frase_traducida)

print("Frase traducida:", frase_final)