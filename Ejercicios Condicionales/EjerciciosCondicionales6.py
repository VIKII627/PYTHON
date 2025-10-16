nombre = input("Por favor, ingrese su nombre: ")
sexo = input("Por favor, ingrese su sexo (M/F): ").upper()

if (sexo == 'F' and nombre[0].upper() < 'M'):
    print("Pertenece al grupo A.")
elif (sexo == 'M' and nombre[0].upper() > 'N'):
    print("Pertenece al grupo B.")