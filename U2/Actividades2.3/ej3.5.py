import random

titular = "kevin"
saldo = random.randint(0, 1000)
estado = True
operacion = ""

while operacion != "salir":
    print("Operaciones: ingresar, retirar, consultar, cerrar cuenta, abrir cuenta, salir")
    operacion = input("Introduce una operacion: ").strip().lower()

    match operacion:
        case "ingresar":
            if estado:
                cantidad = float(input("Cantidad a ingresar: "))
                if cantidad > 0:
                    saldo += cantidad
                    print("Ingreso realizado")
                else:
                    print("Cantidad no valida")
            else:
                print("La cuenta esta cerrada")

        case "retirar":
            if estado:
                cantidad = float(input("Cantidad a retirar: "))
                if cantidad <= 0:
                    print("Cantidad no valida")
                else:
                    if cantidad <= saldo:
                        saldo -= cantidad
                        print("Retirada realizada")
                    else:
                        print("Saldo insuficiente")
            else:
                print("La cuenta esta cerrada")

        case "consultar":
            print("Titular:", titular)
            print("Saldo:", saldo, "euros")
            print("Cuenta activa:", estado)

        case "cerrar cuenta":
            if estado and saldo == 0:
                estado = False
                print("Cuenta cerrada")
            else:
                print("No se puede cerrar la cuenta")

        case "abrir cuenta":
            if not estado:
                estado = True
                saldo = 0
                print("Cuenta abierta correctamente")
            else:
                print("Ya existe una cuenta activa")

        case "salir":
            print("Saliendo del banco")

        case _:
            print("Operacion no valida")

print("----- ESTADO FINAL -----")
print("Titular:", titular)
print("Saldo:", saldo, "euros")
print("Cuenta activa:", estado)