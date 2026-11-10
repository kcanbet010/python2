productos = ["pan", "leche", "huevos"]
precios = [0.85, 1.20, 2.50] 
carrito = []             


#1
def mostrar_menu():
    print("Supermercado")
    print("1. Añadir")
    print("2. Quitar")
    print("3. Repartir la cuenta")
    print("4. Salir")

def convertir_numero(texto):
    try:
        numero = int(texto)
        if numero < 0:
            raise ValueError("El numero no puede ser negativo") 
    except ValueError as error:
        print(f"Error: {error}")

#2
def anadir(carrito,numero):
    if numero not in [0,1,2]:
        raise ValueError("El producto no existe")
    else:
        carrito.append(precios[numero])

#3


#4
def calcular_total (carrito):
    try:
        producto1 = int("Sumando: ", [0,1,2])
        valor = producto1
    except ValueError:
        print("Los dos valores deben ser enteros")
    except Exception:
        print("No puede salir negativo")
    else:
        print(valor)

#5

#MAIN
def main():
    opcion = 1
    while opcion != 4:
        mostrar_menu()
        try:
            opcion = convertir_numero(input("Que quieres hacer: "))
        except ValueError as error:
            print("Error ",error)  

        match opcion:
            case 1:
                print("0. Pan")
                print("1.Leche")
                print("2. Huevos")
                try:
                     producto = int(input("¿Que producto quieres añadir?"))
                     anadir(carrito,producto)
                except Exception as error:
                    print("Error ",error)

            case 2:
                print("¿Que desea quitar?")