import math

print("Calculo de Areas")
print("Elija una figura geometrica")
print("a) Triangulo")
print("b) Circulo")
figura = input("¿Que figura quieres calcular (Escribe T o C)? ").lower()

match figura:
        case "t":
                try:
                    base = int(input("Dime la base"))
                    altura = int(input("Dime la altura"))
                except ValueError as error:
                    print("Error: ", error)
                else: 
                    area = (base*altura)/2
                    print(f"Un triangulo que tiene una base de {base} y altura {altura} tiene un area de {area}")
                finally:
                    print("Operaicon finalizada")

        case "c":
                try:
                    radio =float(input("Escriba el radio: "))
                except ValueError as error:
                      print("Error: ",error)
                else:
                    area = math.PI*radio*radio
                    print(f"Un circulo de radio {radio} tiene un area de {area}")
                finally:
                    print("Operaicon finalizada")
        case _:
            print("Eso no lo puedo hacer")