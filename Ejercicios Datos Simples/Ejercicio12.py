#Ejercicio 12
#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
#un descuento del 60%. Escribir un programa que comience leyendo el número de
#barras vendidas que no son del día. Después el programa debe mostrar el precio
#habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
#coste final total.

barras_vendidas = int(input("Introduce el número de barras vendidas que no son del día: "))
precio_barradepan = 3.49
descuento = 0.60
precio_descuento = precio_barradepan * descuento
coste_final = (precio_barradepan - precio_descuento) * barras_vendidas

print("El precio habitual de una barra de pan es de:", precio_barradepan, "€")
print("El descuento que se le hace por no ser fresca es de:", round(precio_descuento, 2), "€")
print("El coste final total es de:", round(coste_final, 2), "€")