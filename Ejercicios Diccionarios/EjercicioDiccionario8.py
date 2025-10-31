#Ejercicio 8 Escribir un programa que cree un diccionario de traducción español-inglés. 
#El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada 
#par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. 
#Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
#Si una palabra no está en el diccionario debe dejarla sin traducir. 

traduccion = {}
entrada = input("Introduce las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas: ")
pares = entrada.split(',')

for par in pares:
    palabra_es, palabra_en = par.split(':')
    traduccion[palabra_es.strip()] = palabra_en.strip()

frase_es = input("Introduce una frase en español para traducir: ")
palabras_es = frase_es.split()
frase_en = []

for palabra in palabras_es:
    if palabra in traduccion:
        frase_en.append(traduccion[palabra])
    else:
        frase_en.append(palabra)

print("Frase traducida:", ' '.join(frase_en))