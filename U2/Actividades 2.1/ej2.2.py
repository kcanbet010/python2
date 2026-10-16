
edad = int(input("Introduce tu edad: "))

match edad:
    case valor if valor < 0:
        print("Error: edad negativa")

    case valor:
        dia = input("Introduce el dia: ").strip().lower()
        sesion_3d = input("La sesion es 3D? (si/no): ").strip().lower()

        match edad:
            case valor if valor < 12:
                precio = 5
                print("Entrada infantil: 5 €")

            case valor if valor >= 65:
                precio = 6
                print("Entrada mayores: 6 €")

            case _:
                precio = 8
                print("Entrada general: 8 €")

        if dia == "miercoles":
            precio -= 1
            print("Descuento miercoles: -1 €")

        if sesion_3d == "si":
            precio += 2
            print("Suplemento 3D: +2 €")

        print("Precio final:", precio, "€")


