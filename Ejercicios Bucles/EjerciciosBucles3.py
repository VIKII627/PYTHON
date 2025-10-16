numero = int(input("Introduce un número entero positivo: "))

for i in range(1, numero + 1, 2):
    if i < numero - 1:
        print(i, end = ", ")
    else:
        print(i)