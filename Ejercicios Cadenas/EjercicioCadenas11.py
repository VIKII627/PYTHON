nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
unidades = int(input("Introduce el número de unidades: "))
coste_total = precio * unidades
print(f"{nombre}: {precio:9.2f}€ x {unidades:3d} = {coste_total:10.2f}€")