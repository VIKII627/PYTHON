# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función. 

def funArea(radio):
    areaC = (radio * radio) * 3.14
    return areaC

def funVolumen(radio, altura):
    areaV = funArea(radio)
    volumen = areaV * altura
    return volumen

print(funArea(5))
print(funVolumen(5, 10))