numero = int(input("Introduce un número entero positivo: "))
i = 1
es_primo = True
while i <= numero:
    if numero % i == 0 and i != 1 and i != numero:
        es_primo = False
        break
    i += 1
if es_primo:
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")
