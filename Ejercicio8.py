n = int(input("Introduce un numero entero n: "))
m = int(input("Introduce un numero entero m: "))

c = n // m
r = n % m

print("{} entre {} da un cociente {} y un resto {}".format(n, m, c, r))