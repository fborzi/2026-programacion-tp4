from funciones import usuario,  contrasenia_por_defecto

nombre = input("Ingrese el nombre completo: ")
dni = int(input("Ingrese el DNI: "))

while "JUAN" not in nombre.upper() and "MARIA" not in nombre.upper():
    contrasenia = contrasenia_por_defecto(dni)
    nombre_usuario = usuario(nombre)

    nombre = input("Ingrese el nombre completo: ")

    if "JUAN" not in nombre.upper() and "MARIA" not in nombre.upper():
        dni = int(input("Ingrese el DNI: "))

print("Usuario:", nombre_usuario)
print("Contraseña:", contrasenia) 
