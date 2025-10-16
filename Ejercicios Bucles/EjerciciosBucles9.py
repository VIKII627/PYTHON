contraseña = "hola"
entrada = input("Introduce la contraseña: ")

while entrada != contraseña:
    print("Contraseña incorrecta. Inténtalo de nuevo.")
    entrada = input("Introduce la contraseña: ")
print("Contraseña correcta. ¡Acceso concedido!")