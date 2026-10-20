numero = int(input("Introduce un numero mayor que 1: "))
primo = True

for divisor in range(2, numero):
    if numero % divisor == 0:
        primo = False

if numero <= 1:
    print("El numero debe ser mayor que 1")
else:
    if primo:
        print("El numero es primo")
    else:
        print("El numero no es primo")