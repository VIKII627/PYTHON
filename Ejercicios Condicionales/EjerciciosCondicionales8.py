puntuacion = float(input("Por favor, ingrese la puntuación obtenida (0.0, 0.4, 0.6 o más): "))

if puntuacion == 0.0:
    print ("Nivel Inaceptable. No recibe bonificación.")
elif puntuacion == 0.4:
    print ("Nivel Aceptable. Recibe una bonificación de:", 2400 * puntuacion, "euros.")
elif puntuacion >= 0.6:
    print ("Nivel Meritorio. Recibe una bonificación de:", 2400 * puntuacion, "euros.")
elif puntuacion != 0.0 and puntuacion != 0.4 and puntuacion < 0.6:
    print ("Puntuación no válida. Debe ser 0.0, 0.4, 0.6 o más.")