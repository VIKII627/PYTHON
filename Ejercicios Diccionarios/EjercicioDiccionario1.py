#Ejercicio 1 Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario 
#por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
Diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("¿Cual es su divisa? (Escriba un simbolo o un mensaje): ")

if divisa in Diccionario:
    print("El simbolo de la divisa es: ", Diccionario[divisa])
else:
    print("La divisa no está en el diccionario.")