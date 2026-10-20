intentos = 0
codigo = ""

while intentos < 3 and codigo != "4826":
    codigo = input("Introduce el codigo: ")
    intentos += 1
    if codigo != "4826":
        print("Intentos restantes:", 3 - intentos)

print("Acceso autorizado" if codigo == "4826" else "Acceso bloqueado")