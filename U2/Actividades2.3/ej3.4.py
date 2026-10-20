aforo = 0
accion = ""

while accion != "fin":
    accion = input("Accion (entra, sale, fin): ").strip().lower()

    match accion:
        case "entra":
            if aforo < 8:
                aforo += 1
                print("Persona admitida")
            else:
                print("Sala llena")

        case "sale":
            if aforo > 0:
                aforo -= 1
                print("Persona fuera")
            else:
                print("La sala esta vacia")

        case "fin":
            print("Control finalizado")

    if accion != "fin":
        print("Personas dentro:", aforo)

print("Personas restantes:", aforo)