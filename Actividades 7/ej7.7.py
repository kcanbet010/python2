archivo = input("Introduce el nombre del archivo: ")

archivo_limpio = archivo.strip().lower()

empieza_correcto = archivo_limpio.startswith("act_")
termina_correcto = archivo_limpio.endswith(".py")
posicion_guion = archivo_limpio.find("_")

print("Empieza por act_:", empieza_correcto)
print("Termina en .py:", termina_correcto)
print("Posicion del primer guion bajo:", posicion_guion)