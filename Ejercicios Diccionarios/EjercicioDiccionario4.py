#Ejercicio 4 Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha 
#en formato dd de <mes> de aaaa donde <mes> es el nombre del mes. 
fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
dia, mes, anio = fecha.split('/')

meses = {'01': 'enero', '02': 'febrero', '03': 'marzo', '04': 'abril', '05': 'mayo', '06': 'junio',
         '07': 'julio', '08': 'agosto', '09': 'septiembre', '10': 'octubre', '11': 'noviembre', '12': 'diciembre'}

if mes in meses:
    nombre_mes = meses[mes]
    print(f"La fecha es: {dia} de {nombre_mes} de {anio}")
else:
    print("Mes inválido.")  