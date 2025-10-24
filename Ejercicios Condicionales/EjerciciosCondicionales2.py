#Ejercicio 2
#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña e imprima por pantalla si la
#contraseña introducida por el usuario coincide con la guardada en la variable sin
#tener en cuenta mayúsculas y minúsculas.

contraseña = "HolaMundo123"
entrada = input("Por favor, ingrese la contraseña: ")   

if entrada.lower() == contraseña.lower():
    print ("Contraseña correcta.")
else:
    print ("Contraseña incorrecta.")   