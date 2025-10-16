edad = int(input("Por favor, ingrese su edad: "))

if edad < 4:
    print("Puede entrar GRATIS.")
elif edad >= 4 and edad <= 18:
    print("Debe pagar 5 euros.")
elif edad > 18:
    print("Debe pagar 10 euros.")