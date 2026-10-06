incidencia = input("Escribe la incidencia: ")

incidencia = incidencia.strip()

formato_titulo = incidencia.title()
formato_guiones = incidencia.lower().replace(" ", "-")
numero_errores = incidencia.lower().count("error")
numero_caracteres = len(incidencia)

print("Descripcion limpia:", incidencia)
print("Formato titulo:", formato_titulo)
print("Formato con guiones:", formato_guiones)
print("Numero de veces que aparece error:", numero_errores)
print("Numero de caracteres:", numero_caracteres)