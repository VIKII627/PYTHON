#Ejercicio 13 Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y 
#muestre por pantalla su media y desviación típica.
import statistics
numeros = input("Introduce una muestra de números separados por comas: ")
numeros1 = [float(num) for num in numeros.split(",")]
media = statistics.mean(numeros1)
desviacionT = statistics.stdev(numeros1)

print(f"La media de los números es: {media}")
print(f"La desviación típica de los números es: {desviacionT}")