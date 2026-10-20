
def es_par(numero):
    return numero % 2 == 0


def suma_digitos(numero):
    numero = abs(numero)
    suma = 0

    while numero > 0:
        suma += numero % 10
        numero //= 10

    return suma


cantidad_impares = 0

while True:
    numero = int(input())
    suma = suma_digitos(numero)

    if suma < 10 or suma > 50:
        break

    if not es_par(numero):
        cantidad_impares += 1

print("Cantidad de numeros impares leidos:", cantidad_impares)

