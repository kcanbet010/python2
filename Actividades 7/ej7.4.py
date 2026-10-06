entrada = " Python, Redes , Sistemas, Python "

lista_asignaturas = entrada.split(",")

asignaturas = set()

for asignatura in lista_asignaturas:
    asignaturas.add(asignatura.strip())

asignaturas.add("Bases de datos")
asignaturas.discard("Redes")

resultado = sorted(asignaturas)

print("Asignaturas:", " ".join(resultado))