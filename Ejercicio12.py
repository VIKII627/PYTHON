barras_vendidas = int(input("Introduce el número de barras vendidas que no son del día: "))
precio_barradepan = 3.49
descuento = 0.60
precio_descuento = precio_barradepan * descuento
coste_final = (precio_barradepan - precio_descuento) * barras_vendidas

print("El precio habitual de una barra de pan es de:", precio_barradepan, "€")
print("El descuento que se le hace por no ser fresca es de:", round(precio_descuento, 2), "€")
print("El coste final total es de:", round(coste_final, 2), "€")