#Ejercicio 7 Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
#y muestre por pantalla la lista resultante. 
import string

abecedario = list(string.ascii_lowercase)
abecedario_filtrado = [letra for indice, letra in enumerate(abecedario) 
                       if (indice + 1) % 3 != 0]

print("Abecedario después de eliminar las letras en posiciones múltiplos de 3:")
print(abecedario_filtrado)
