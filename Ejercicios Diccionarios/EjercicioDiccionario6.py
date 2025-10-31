#Ejercicio 6 Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
#(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario.
#Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario. 

persona = {}

nombre = input("Ingrese su nombre: ")
persona['Nombre'] = nombre
print(persona)
edad = input("Ingrese su edad: ")
persona['Edad'] = edad
print(persona)
sexo = input("Ingrese su sexo: ")
persona['Sexo'] = sexo
print(persona)
telefono = input("Ingrese su teléfono: ")
persona['Teléfono'] = telefono
print(persona)
correo = input("Ingrese su correo electrónico: ")
persona['Correo electrónico'] = correo
print(persona)
print("Información completa de la persona:")

for clave, valor in persona.items():
    print(f"{clave}: {valor}")