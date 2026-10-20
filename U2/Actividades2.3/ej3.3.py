precio = 170
pagado = 0

while pagado < precio:
    moneda = int(input("Introduce una moneda (10, 20, 50, 100): "))

    if moneda == 10 or moneda == 20 or moneda == 50 or moneda == 100:
        pagado += moneda
        print("Importe pagado:", pagado, "centimos")
    else:
        print("Moneda no aceptada")

cambio = pagado - precio

print("Producto entregado")
print("Cambio:", cambio, "centimos")
print("Cambio en euros:", cambio / 100, "€")