canciones = ["Luz", "Viaje", "Luz", "Norte"]

canciones.append("Casa")
canciones.append("Sol")

canciones.remove("Luz")

orden_alfabetico = sorted(canciones)

cantidad_luz = canciones.count("Luz")
primera_luz = canciones.index("Luz")

print("Playlist actual:", canciones)
print("Playlist ordenada:", orden_alfabetico)
print("Veces que aparece Luz:", cantidad_luz)
print("Primera posicion de Luz:", primera_luz)