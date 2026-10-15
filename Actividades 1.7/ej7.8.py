from array import array

temperaturas = array("i", [18, 20, 21, 19, 22])

temperaturas.append(23)

temperaturas[2] = 20

print("Temperaturas:", list(temperaturas))
print("Tipo de estructura:", type(temperaturas))