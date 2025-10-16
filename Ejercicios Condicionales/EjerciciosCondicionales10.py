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