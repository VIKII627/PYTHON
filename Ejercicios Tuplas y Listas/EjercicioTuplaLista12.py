#Ejercicio 12 Escribir un programa que almacene las matrices en una lista y muestre por pantalla su producto. 
#Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista. 
matriz1 =   [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matriz2 =   [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

producto_matriz = [[0, 0, 0],
                   [0, 0, 0],   
                   [0, 0, 0]]

for i in range(len(matriz1)):
    for j in range(len(matriz2[0])):
        for l in range(len(matriz2)):
            producto_matriz[i][j] += matriz1[i][l] * matriz2[l][j]

print("El producto de las matrices es:")
print(producto_matriz)