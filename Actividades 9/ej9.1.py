precio = float(input("Introduce el precio: "))
unidades = int(input("Introduce las unidades: "))
descuento = float(input("Introduce el descuento (%): "))

iva = 21
envio_gratis = 50

subtotal = precio * unidades
importe_descuento = subtotal * descuento / 100
base = subtotal - importe_descuento
importe_iva = base * iva / 100
total = base + importe_iva

print("Subtotal:", f"{subtotal:.2f}")
print("Descuento:", f"{importe_descuento:.2f}")
print("IVA:", f"{importe_iva:.2f}")
print("Total:", f"{total:.2f}")

if total >= envio_gratis:
    print("El pedido tiene envio gratuito")
else:
    print("El pedido no tiene envio gratuito")