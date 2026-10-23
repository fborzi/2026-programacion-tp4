#EJERCICIO 9 Lectura de usario
from funciones import usuario, contrasenia_por_defecto

nombre = input("ingresa apellido y nombre: ")

while "juan" not in nombre.lower() and "maria" not in nombre.lower() and "maria" not in nombre.lower():
    dni = int(input("ingresa el DNI: "))

    print("Usuario:", usuario(nombre))
    print("contraseña:", contrasenia_por_defecto(dni))

    nombre = input("ingresa apellido y nombre: ")
