#Dificultad Media Convertidor entre calendarios

try:
    fecha = int(input("Introduce una año: "))
except ValueError as error:
    print("Error: ", error)

g = (32*fecha + 20526)/33
m = (33*fecha - 20526)/32

print(f"El año",fecha, "del calendario gregoriano es aproximadamente el año",m, "del calendario musulmán.")
print(f"El año",fecha, "del calendario gregoriano es aproximadamente el año",g, "del calendario gregoriano.")