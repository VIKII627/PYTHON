#Ejercicio 10
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
#Los ingredientes para cada tipo de pizza aparecen a continuación.
#● Ingredientes vegetarianos: Pimiento y tofu.
#● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
#en función de su respuesta le muestre un menú con los ingredientes disponibles
#para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
#tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
#pizza elegida es vegetariana o no y todos los ingredientes que lleva.

tipo = input("Por favor, ingrese el tipo de pizza que desea (vegetariana/no vegetariana): ").lower()

if tipo == "vegetariana":
    print("Ingredientes vegetarianos disponibles: Pimiento y Tofu.")
    ingrediente = input("Elija un ingrediente (Pimiento/Tofu): ").lower()
    if ingrediente == "pimiento":
        print("Ha elegido una pizza vegetariana con los siguientes ingredientes: Mozzarella, Tomate y", ingrediente)
    elif ingrediente == "tofu":
        print("Ha elegido una pizza vegetariana con los siguientes ingredientes: Mozzarella, Tomate y", ingrediente)

if tipo == "no vegetariana":
    print("Ingredientes no vegetarianos disponibles: Peperoni, Jamón y Salmón.")
    ingrediente = input("Elija un ingrediente (Peperoni/Jamón/Salmón): ").lower()
    if ingrediente == "peperoni":
        print("Ha elegido una pizza no vegetariana con los siguientes ingredientes: Mozzarella, Tomate y", ingrediente)
    elif ingrediente == "jamon":
        print("Ha elegido una pizza no vegetariana con los siguientes ingredientes: Mozzarella, Tomate y", ingrediente)
    elif ingrediente == "salmon":
        print("Ha elegido una pizza no vegetariana con los siguientes ingredientes: Mozzarella, Tomate y", ingrediente)