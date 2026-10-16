from typing import Final

NOMBRE_CATALOGO: Final = "Equipamiento de aula"

productos_iniciales = [" teclado ", "RATON", "monitor", "Raton"]

productos = set()

for producto in productos_iniciales:
    productos.add(producto.strip().capitalize())

producto1 = input("Introduce un producto nuevo: ")
producto2 = input("Introduce otro producto nuevo: ")

productos.add(producto1.strip().capitalize())
productos.add(producto2.strip().capitalize())

productos.discard("Monitor")

productos_ordenados = sorted(productos)

print("Catalogo:", NOMBRE_CATALOGO)
print("Productos:", ", ".join(productos_ordenados))
print("Numero de productos:", len(productos_ordenados))