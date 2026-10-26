TIEMPO_CINE = 2
DINERO_CINE = 6
TIEMPO_COMER = 2
DINERO_COMER = 14
TIEMPO_MUSEO = 1
DINERO_MUSEO = 10
TIEMPO_DEPORTE = 1
DINERO_DEPORTE = 5
TIEMPO_QUEDARME = 3
DINERO_QUEDARME = 0


def mostrar_opciones():
    """Muestra las actividades disponibles."""
    print("1. Ir al cine (6€ / 2 horas)")
    print("2. Salir a comer (14€ / 2 horas)")
    print("3. Visitar un museo (10€ / 1 hora)")
    print("4. Salir a hacer deporte (5€ / 1 hora)")
    print("5. Quedarse en casa (0€ / 3 horas)")
    print("6. Finalizar")


def comprobar_dinero(dinero, precio):
    """Comprueba si tenemos dinero suficiente."""
    return dinero >= precio


def comprobar_tiempo(tiempo, horas):
    """Comprueba si tenemos tiempo suficiente."""
    return tiempo >= horas


def mostrar_resumen(actividades, dinero_gastado, tiempo_gastado, dinero):
    """Muestra el resumen de las actividades realizadas."""
    print("Actividades realizadas:")
    print(actividades)
    print("Dinero gastado:", dinero_gastado, "€")
    print("Tiempo utilizado:", tiempo_gastado, "horas")
    print("Dinero restante:", dinero, "€")


def main():
    """Organiza el dia segun el dinero y tiempo disponibles."""
    dinero = input("Cuanto dinero quieres gastarte como maximo? ")
    tiempo = input("Cuanto tiempo quieres invertir como maximo? ")

 # ESTE BLOQUE LO HE TENIDO QUE BUSCAR PORQUE NO TENIA NI IDEA
    while not dinero.isdigit() or not tiempo.isdigit():
        print("Introduce cantidades enteras validas")
        dinero = input("Cuanto dinero quieres gastarte como maximo? ")
        tiempo = input("Cuanto tiempo quieres invertir como maximo? ")

    dinero = int(dinero)
    tiempo = int(tiempo)

    actividades = ""
    dinero_gastado = 0
    tiempo_gastado = 0
    opcion = ""

    while opcion != "6":
        mostrar_opciones()
        opcion = input("Que quieres hacer? ").strip()

        precio = 0
        horas = 0
        actividad = ""

        match opcion:
            case "1":
                precio = DINERO_CINE
                horas = TIEMPO_CINE
                actividad = "Ir al cine (6€ / 2 horas)\n"

            case "2":
                precio = DINERO_COMER
                horas = TIEMPO_COMER
                actividad = "Salir a comer (14€ / 2 horas)\n"

            case "3":
                precio = DINERO_MUSEO
                horas = TIEMPO_MUSEO
                actividad = "Visitar un museo (10€ / 1 hora)\n"

            case "4":
                precio = DINERO_DEPORTE
                horas = TIEMPO_DEPORTE
                actividad = "Salir a hacer deporte (5€ / 1 hora)\n"

            case "5":
                precio = DINERO_QUEDARME
                horas = TIEMPO_QUEDARME
                actividad = "Quedarse en casa (0€ / 3 horas)\n"

            case "6":
                print("Finalizando programa")

            case _:
                print("Opcion no valida")

       
        if actividad != "":
            if comprobar_dinero(dinero, precio) and comprobar_tiempo(tiempo, horas):
                dinero -= precio
                tiempo -= horas
                dinero_gastado += precio
                tiempo_gastado += horas
                actividades += actividad
                print("Actividad añadida correctamente")
            else:
                print("No tienes suficiente dinero o tiempo")
                print("Puedes elegir otra actividad")

    mostrar_resumen(actividades, dinero_gastado, tiempo_gastado, dinero)


if __name__ == "__main__":
    main()