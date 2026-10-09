incidencia = input ("Escribe la incidencia:")

incidencia_espacio = incidencia.strip()
formato_titulo  = incidencia_espacio.title()
formato_guiones = incidencia_espacio.lower().replace(" ", "-")
errores = incidencia_espacio.lower().count("error")
caracteres = len(incidencia_espacio)

print ("Descripcion limpia", incidencia_espacio)
print ("Formato", formato_titulo)
print ("Formato de los guiones:", formato_guiones)
print ("Numero de errores:", errores)
print ("Numero de caracteres:", caracteres)