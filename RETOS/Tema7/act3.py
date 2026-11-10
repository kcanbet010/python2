#Dificultad Media Grande, pequeño o en medio
print("Introduce 3 numeros")
numero1 = int(input("Escriba el primer numero: "))
numero2 = int(input("Escriba el segundo numero: "))
numero3 = int(input("Escriba el tercer numero: "))

mayor = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

for numero in [numero1, numero2, numero3]:
    if numero == mayor:
        print(numero,"es el mayor")
    else:
        if numero == menor:
            print(numero, "es el menor")
        else:
            print(numero, "es el de en medio")