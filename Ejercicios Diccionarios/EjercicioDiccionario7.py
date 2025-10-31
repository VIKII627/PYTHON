#Ejercicio 7 Escribir un programa que cree un diccionario simulando una cesta de la compra.
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
# Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato Lista de la compra  
# Artículo 1 Precio Artículo 2 Precio Artículo 3 Precio … … Total Coste 

cesta_compra = {}

while True:
    articulo = input("Introduce el artículo (o escribe 'terminar' para finalizar): ")
    if articulo.lower() == 'terminar':
        break
    precio = float(input(f"Introduce el precio de {articulo}: "))
    cesta_compra[articulo] = precio

print("\nLista de la compra:")
total_coste = 0

for articulo, precio in cesta_compra.items():
    print(f"{articulo}: {precio:.2f} euros")
    total_coste += precio

print(f"Total Coste: {total_coste:.2f} euros")