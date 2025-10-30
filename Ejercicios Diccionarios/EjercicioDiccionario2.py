#Ejercicio 2 Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
#Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>. 
diccionario = {}
nombre = input("¿Cual es su nombre?: ")
edad = input("¿Cual es su edad?: ")
direccion = input("¿Cual es su dirección?: ")
telefono = input("¿Cual es su número de teléfono?: ")

diccionario ['Nombre'] = nombre
diccionario ['Edad'] = edad
diccionario ['Dirección'] = direccion
diccionario ['Teléfono'] = telefono