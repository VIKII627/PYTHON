cantidad = float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: "))
interes = 0.04
for i in range(1,4):
    cantidad = cantidad + (cantidad * interes)
    print("Cantidad de ahorros tras el año", i, ":", round(cantidad, 2))