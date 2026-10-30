def imprimir():
    print("1. Introducir")
    print("0. Salir")

def media(a, b):
    if b == 0:
        return 0
    else:
        return a/b

def main():

    opcion = 1
    numero_incidencias = 0
    prioridad_alta = 0
    tiempo_total = 0

    while opcion != 0:
        imprimir()
        opcion = int(input("¿Que quieres hacer? "))
        
        match opcion:
            case 1: #Pedir datos de incidencia y hacer comprobaciones
                prioridad = int(input("Dime la prioridad: "))
                if prioridad not in [1,2,3]:
                    print("Prioridad no valida")
                else:
                    minutos = int(input("Dime los minutos: "))
                    if minutos > 0:
                        tiempo_total+=minutos
                    numero_incidencias+=1
                    if prioridad == 3:
                        prioridad_alta+=1
                    else:
                        print("Minutos no validos no se tienen en cuenta")
            case 0: #Mostrar resumen y acabar
                print("\nRESUMEN")
                print("Incidencias registradas: ", numero_incidencias)
                print("Incidencias de prioridad alta: ", prioridad_alta)
                print("Tiempo medio: ", media(tiempo_total,numero_incidencias))

            case _: #Volver a pedir la opcion
                print("Opcion no valida")

if __name__ == "__main__":
    main()