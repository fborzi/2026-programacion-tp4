#ejercico 1406 corte por suma de digitos#

from funciones import es_par, suma_digitos

cantidad_impares = 0
numero = int(input("Ingresa un numero: "))

while suma_digitos(numero) >= 10 and suma_digitos(numero) <= 50:
    if not es_par(numero):
        cantidad_impares += 1

    numero = int(input("ingresa un numero: "))

print("cantidad de numeros impares leidos:", cantidad_impares)
