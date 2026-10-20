
def usuario(nombre):
    partes = nombre.split(",")

    apellido = partes[0]
    nombres = partes[1]

    nombre_usuario = (nombres + apellido).replace(" ", "")
    return nombre_usuario.lower()


def contrasenia_por_defecto(dni):
    return str(dni)[-4:]


while True:
    nombre = input()

    nombre_minuscula = nombre.lower()

    if "juan" in nombre_minuscula or "maría" in nombre_minuscula or "maria" in nombre_minuscula:
        break

    dni = int(input())

    print("Usuario:", usuario(nombre))
    print("Contrasenia:", contrasenia_por_defecto(dni))
