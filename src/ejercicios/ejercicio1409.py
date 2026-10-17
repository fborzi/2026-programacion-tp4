from funciones import usuario, contrasenia_por_defecto

nombre = input("Ingrese el nombre completo: ")

while "JUAN" not in nombre.upper() and "MARÍA" not in nombre.upper():

    dni = int(input("Ingrese el DNI: "))

    print("Usuario:", usuario(nombre))
    print("Contrasenia:", contrasenia_por_defecto(dni))

    nombre = input("Ingrese el nombre completo: ")
