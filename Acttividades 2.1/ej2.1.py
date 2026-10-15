import random

titular = "kevin"
saldo = random.radiant(0,1000)
estado = True

print ("Titular:", titular)
print ("Dispone de un saldo de:", saldo, "euros")

operacion = input ("Operacion: ingresar, retirar, abrir_cuenta, cerrar cuenta o consultar")
operacion_limpia = operacion.lower().strip()

match operacion_limpia:
    case "ingresar":
        cantidad = int(input("Dinero a ingresar:"))
        if cantidad > 0:
            saldo += cantidad
        else:
            print("Cantidad no valida")
    case "retirar":
        cantidad = int(input("Cantidad a retirar:"))
        if cantidad > 0 and saldo >= cantidad:
            saldo -= cantidad
        else:
            print("Cantidad no valida")
    case "abrir_cuenta":
       if not estado:
           estado = True
    case "cerrar cuenta":
        if estado and saldo == 0:
            estado = False
            print("Cuenta cerrada")
        else:
            print("La cuenta ya esta cerrada")
    case "consultar":
        print(titular, "tu saldo es: ", saldo)
    case _:
        print("Operacion no valida")

