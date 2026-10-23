TIEMPO_CINE = 2
DINERO_CINE = 6
TIEMPO_COMER = 2
DINERO_COMER = 14
TIEMPO_MUSEO = 1
DINERO_MUSEO = 10
TIEMPO_DEPORTE = 1
DINERO_DEPORTE = 5
TIEMPO_QUEDARME = 3
DINERO_QUEDARME = 1

def mostrar_opciones():
    print("1. Ir al cine (6€ / 2 horas)")
    print("2. Salir a comer (14€ / 2 horas) ")
    print("3. Visitar un museo (10€ / 1 hora)")
    print("4. Salir a hacer deporte (5€ / 1 hora)")
    print("5. Quedarse en casa (0€ / 3 horas)")

def main():

    dinero = int(input("Cuanto dinero quieres gastarte como maximo?"))
    tiempo = int(input("Cuanto tiemp quieres invertir como maximo?"))
    actvidades = ""

    while dinero > 0 and tiempo > 0:
        mostrar_opciones()
        opcion = int(input("Que quieres hacer"))

        opcion = input ("Elige una actividad")

        match opcion:
            case "1":
                precio -= DINERO_CINE
                horas -= TIEMPO_CINE
                actvidades += "Ir al cine (6€ / 2 horas)\n"

            case "2":
                precio -= DINERO_COMER
                horas -= TIEMPO_COMER
                actvidades += "Salir a comer (14€ / 2 horas)\n"

            case "3":
                precio -= DINERO_MUSEO
                horas -= TIEMPO_MUSEO
                actvidades += "Visitar un museo (10€ / 1 hora)\n"

            case "4":
                precio -= DINERO_DEPORTE
                horas -= TIEMPO_DEPORTE
                actvidades += "Salir a hacer deporte (5€ / 1 hora)\n"

            case "5":
                precio -= DINERO_QUEDARME
                horas -= TIEMPO_QUEDARME
                actvidades += " -Quedarse en casa (0€ / 3 horas)\n"

            case _:
                print(actvidades)

if __name__ == "__main__":
    main()