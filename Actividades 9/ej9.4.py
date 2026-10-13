plazas = 12

plazas -= 3
plazas += 1

estado = "Hay plazas" if plazas > 0 else "Completo"

print("Plazas disponibles:", plazas)
print("Estado:", estado)