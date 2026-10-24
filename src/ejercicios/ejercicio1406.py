#ejercico 1406 corte por suma de digitos#

def es_par(numero):
    return numero % 2 == 0


def suma_digitos(numero):
    suma = 0

    for digito in str(abs(numero)):
        suma = suma + int(digito)

    return suma


def leer_numeros(cantidad_impares):
    numero = int(input("ingresa un numero: "))
    suma = suma_digitos(numero)

    if suma < 10 or suma > 50:
        return cantidad_impares

    if not es_par(numero):
        cantidad_impares = cantidad_impares + 1

    return leer_numeros(cantidad_impares)


cantidad = leer_numeros(0)

print("cantidad de numeros impares:", cantidad)
