from funciones import usuario, contrasenia_por_defecto
nombre = input("ingrese nombre completo: ")

while "juan" not in nombre.upper() and "maria" not in nombre.upper():
    dni = int(input("Ingrese DNI: "))

    print("usuario:", usuario(nombre))
    print("contrasenia:", contrasenia_por_defecto(dni))

    nombre = input("ingrese nombre completo: ")