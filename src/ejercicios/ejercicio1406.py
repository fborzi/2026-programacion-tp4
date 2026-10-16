from funciones import es_par
from funciones import suma_digitos

cantidad_impares = 0
numero = int(input("Ingrese un número: "))

while suma_digitos(numero) >= 10 and suma_digitos(numero) <= 50:

    if not es_par(numero):
     cantidad_impares = cantidad_impares + 1

    numero = int(input("Ingrese un número: "))
print("Cantidad de numeros impares leidos:", cantidad_impares)