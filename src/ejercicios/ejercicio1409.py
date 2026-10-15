from funciones import usuario, contrasenia_por_defecto

nombre= input("Ingrese un nombre")
dni= input(("Ingrese un numero: "))


while not ("juan" in nombre.lower() or "maría" in nombre.lower()):
    print("Usuario: "+ usuario(nombre))
    print("Contrasenia: "+ contrasenia_por_defecto(dni))
    nombre= input("Ingrese un nombre")
    dni= input(("Ingrese un numero: "))