from funciones import usuario, contrasenia_por_defecto

nombre: str = input()
nombre_usuario: str = usuario(nombre)

while "juan" not in nombre_usuario and "maria" not in nombre_usuario:
    dni: int = int(input())
    print(f"Usuario: {nombre_usuario}")
    print(f"Contrasenia: {contrasenia_por_defecto(dni)}")
    nombre = input()
    nombre_usuario = usuario(nombre)
    