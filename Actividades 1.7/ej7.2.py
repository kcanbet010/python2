nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tus apellidos: ")

nombre = nombre.strip().title()
apellido = apellido.strip().title()

nombre_completo = nombre + " " + apellido

correo = nombre.lower() + "." + apellido.lower() + "@centro.example"

print("Nombre completo:", nombre_completo)
print("Cuenta institucional:", correo)