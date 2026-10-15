lista_compra = ["pan", "leche", "manzanas", "leche"]

lista_compra.append("arroz")
lista_compra.append("cafe")

lista_compra.remove("manzanas")
lista_compra.sort()

cantidad_leche = lista_compra.count("leche")

print("Lista de compra:", lista_compra)
print("Cantidad de leche:", cantidad_leche)