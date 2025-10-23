palabra = input("Introduce una palabra: ")
longitud = len(palabra) 

while longitud > 0:
    print(palabra[longitud - 1])
    longitud -= 1
    