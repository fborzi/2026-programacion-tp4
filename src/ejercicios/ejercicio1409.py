#EJERCICIO 9 Lectura de usario


def generar_usuario(nombre_completo):
    partes = nombre_completo.lower().split(",")

    apellido = partes[0].strip()
    nombres = partes[1].strip().split()

    usuario = "".join(nombres) + apellido

    usuario = usuario.replace("á", "a")
    usuario = usuario.replace("e", "e")
    usuario = usuario.replace("i", "i")
    usuario = usuario.replace("o", "o")
    usuario = usuario.replace("u", "u")
    usuario = usuario.replace("n", "n")

    return usuario


def generar_contrasena(numero):
    return str(numero)[-4:]


def leer_usuarios():
    nombre = input("ingresa apellido y nombre: ")

    if "juan" in nombre.lower() or "maria" in nombre.lower() or "maría" in nombre.lower():
        return

    numero = input("ingresa el numero: ")

    usuario = generar_usuario(nombre)
    contrasena = generar_contrasena(numero)

    print("usuario:", usuario)
    print("contraseña:", contrasena)

    leer_usuarios()


leer_usuarios()