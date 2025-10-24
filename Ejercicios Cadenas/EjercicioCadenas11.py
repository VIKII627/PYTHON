#Ejercicio 11
#Escribir un programa que pregunte el nombre el un producto, su precio y un número
#de unidades y muestre por pantalla una cadena con el nombre del producto seguido
#de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
#tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
unidades = int(input("Introduce el número de unidades: "))
coste_total = precio * unidades
print(f"{nombre}: {precio:9.2f}€ x {unidades:3d} = {coste_total:10.2f}€")