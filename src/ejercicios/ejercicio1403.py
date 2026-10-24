"""lectura hasta 8 pares este codigo  """
def leer_pares(cantidad, todos_positivos):
    numero = int(input("ingresa un numero: "))

    if numero % 2 == 0:
        if numero <= 0:
            todos_positivos = False

        cantidad = cantidad + 1

    if cantidad < 8:
        return leer_pares(cantidad, todos_positivos)

    return todos_positivos


resultado = leer_pares(0, True)
print("todos los pares ingresados fueron positivos:")
print(resultado)
