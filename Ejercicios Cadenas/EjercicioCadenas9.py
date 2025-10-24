#Ejercicio 9
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
#dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
#anterior para que también funcione cuando el día o el mes se introduzcan con un
#solo carácter.

fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
dia = fecha.split("/")[0]
mes = fecha.split("/")[1]
anio = fecha.split("/")[2]
print("Día: ", dia)
print("Mes: ", mes)
print("Año: ", anio)