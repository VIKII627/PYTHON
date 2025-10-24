#Ejercicio 6
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
#el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
#los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
#programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
#que le corresponde.

nombre = input("Por favor, ingrese su nombre: ")
sexo = input("Por favor, ingrese su sexo (M/F): ").upper()

if (sexo == 'F' and nombre[0].upper() < 'M'):
    print("Pertenece al grupo A.")
elif (sexo == 'M' and nombre[0].upper() > 'N'):
    print("Pertenece al grupo B.")