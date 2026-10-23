from funciones import usuario,contrasenia_por_defecto
"""Solicito el ingreso de nombre y contraseña de usuario parando cuando en la cadena 
nombre se encuentre la palabra juan o maria y muestro el nombre de usuario y la contraseña por defecto"""

nombre = input("Ingrese su nombre: ")
while "juan" not in nombre.lower() and "maria" not in nombre.lower():
    contrasenia = int(input("Ingrese su contraseña: "))
    print(f"Usuario: {usuario(nombre)}")
    print(f"Contraseña: {contrasenia_por_defecto(contrasenia)}")
    nombre = input("Ingrese su nombre: ")

