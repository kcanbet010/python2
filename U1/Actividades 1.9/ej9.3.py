matriculada = True
autorizacion = False
edad = 17

acceso = (matriculada and edad >= 18) or autorizacion

print("Puede acceder:", acceso)

# Segundo caso
edad = 18

acceso = (matriculada and edad >= 18) or autorizacion

print("Puede acceder:", acceso)