ENTRADA_GENERAL = 8
ENTRADA_MAYORES = 6
ENTRADA_MENORES = 5
ENTRADA_MIERCOLES = 1 
SUPLEMENTO_3D = 2

edad = int(input("Introduzca su edad: "))
dia = input("Introduzca el dia de la semana").strip().lower()
sesion3D = input("Quiere la seison 3D: (Si/NO)").strip().lower()

match edad:
    case valor if valor < 0:
        print("Edad no valida")

    case valor if valor < 12:
        precio = ENTRADA_MENORES
        print("Entrada Infantil: 5€")

    case valor if valor > 65:
        precio = ENTRADA_MAYORES
        print("Entrada mayores: 6€")

    case _:
        precio = ENTRADA_GENERAL
        print("Entrada general: 8€")

if dia == "miercoles" :
    precio -= 1
    print("Descuento por ser miercoles")

if sesion3D == "si" :
    precio += 2
    print("Suplemento 3D: +2€")

print("El precio final sera de :", precio, "€")