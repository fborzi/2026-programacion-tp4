from funciones import suma_digitos,es_par
"""Solicito el ingreso de numeros enteros finalizando luego de leer un numero
la cual la sumade sus digitos sea menor que 10 o mayor que 50"""

numero = int(input("Ingrese un numero entero: "))
impares = 0
while suma_digitos(numero) >= 10 and suma_digitos(numero) <= 50:
    numero = int(input("Ingrese un numero entero: "))
    if  es_par(numero) == False:
        impares += 1
print(f"La cantidad de numeros impares leidos es: {impares}")