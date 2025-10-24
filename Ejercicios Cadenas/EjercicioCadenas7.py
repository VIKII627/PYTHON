#Ejercicio 7
#Escribir un programa que pregunte el correo electrónico del usuario en la consola y
#muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante
#de la arroba @) pero con dominio ceu.es.

email=input("Introduce tu correo electrónico: ")
nombre=email.split("@")[0]  
nuevo_email=nombre+"@ceu.es"
print("Tu nuevo correo es:",nuevo_email)