producto = "gta6"
precio_unitario = 100
cantidad = 4

IVA = 0.21

subtotal = precio_unitario * cantidad
total = subtotal + (subtotal * IVA)

print("Producto:", producto)
print("Subtotal:", subtotal)
print("Total con IVA:", total)

cantidad = 7

subtotal = precio_unitario * cantidad
total = subtotal + (subtotal * IVA)

print("Nueva cantidad:", cantidad)
print("Nuevo subtotal:", subtotal)
print("Nuevo total con IVA:", total)