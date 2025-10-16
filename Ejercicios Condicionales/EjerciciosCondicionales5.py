edad = int(input("Por favor, ingrese su edad: "))
ingresosM = float(input("Por favor, ingrese sus ingresos mensuales: "))

if edad > 16 and ingresosM >= 1000:
    print("Puede tributar.")
else:
    print("No puede tributar.")