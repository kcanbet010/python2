#Dificultad Media Ripios
palabra1 = input("Introduce la primera palabra").strip().lower()
palabra2 = input("Introduce la segunda palabra").strip().lower()

if palabra1[-3:] == palabra2[-3:]:
    print(f"Las palabras", palabra1, "y", palabra2, "riman.")
else:
    if palabra1[-2: ] == palabra2 [-2:]:
        print(f"Las palabras riman un poco")
    else: print(f"Las palabras no riman")