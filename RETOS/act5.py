PLANTILLA = "ABCDABCDAB"

import math

n_alumnos = 0
alumnos = []
respuestas = []
notas = []

def respuesta():
    respuesta = input("Respuestas: ").strip()

    while len(respuesta) != 10:
        respuesta = input("Como minimo debe tener 10 caracteres").strip()
        return respuesta

def corregir(respuesta):
    nota = 0
    for respuesta in respuestas:
        nota = 0
        pos = 0
        for letra in respuesta:
            if letra == "-":
                if letra == PLANTILLA[pos]:
                    nota +=1
                elif letra != PLANTILLA[pos]:
                    nota -= 0.25
        pos +=1
    
    notas.append(nota)
    return nota

def nota_media(notas):
    media = math.average(notas)
    return media

def mejor_nota(notas):
    mejor = max(notas)
    return mejor

def main():
    n_alumnos = int(input("Cuantos alumnos hay: "))

    for a in range(n_alumnos):
        alumnos.append(input("Nombre: "))
        respuestas.append(respuesta())

    for alumno in alumnos:
        print(f"{alumno}: {corregir(respuestas)}")

        print("Nota media: ", nota_media(notas))
        print("Mejor nota: ", mejor_nota(notas))

if __name__ == "__main__":
    main()