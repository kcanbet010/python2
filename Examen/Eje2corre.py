#1 Pedir los nombres
nombres = "srv-03, srv-02, srv-02, srv-01, srv-01"
lista_limpia = []
lista_ordenada = []

separados = nombres.split(",")
for n in separados:
    n = n.strip().lower()
    if n!="" and n not in lista_limpia:
        lista_limpia.append(n)

lista_ordenada = sorted(lista_limpia)

print(f"La lista limpia es: {lista_ordenada} y contiene {len(lista_ordenada)} elementos.")

equipo = input("Dime un euqipo: ")
if equipo in lista_ordenada:
    print("El equipo esta en la lista.")
else:
    print("El equipo NO esta.")