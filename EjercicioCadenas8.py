precio = input("Introduce el precio del producto (con dos decimales): ")
euros = precio.split(".")[0]
centimos =  precio.split(".")[1]
print("El precio del producto es de",euros,"euros y",centimos,"céntimos.")