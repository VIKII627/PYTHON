#Ejercicio 6 Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
#en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa 
#debe mostrar por pantalla las asignaturas que el usuario tiene que repetir. 
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = {}

for asignatura in asignaturas:
    nota = float(input(f"Introduce la nota de {asignatura}: "))
    notas[asignatura] = nota
asignaturas_repetir = [asignatura for asignatura in asignaturas if notas[asignatura] < 5]

print("Asignaturas que tienes que repetir:")

for asignatura in asignaturas_repetir:
    print(asignatura)
