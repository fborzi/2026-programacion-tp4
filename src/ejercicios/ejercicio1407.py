from funciones import maximo,es_positivo
"""Solicito el ingreso de 5 numeros enteros y determino cual es el mayor"""

mayor = 0
for i in range(5):
    numero = int(input("Ingrese un numero entero: "))
    if es_positivo(numero) == True:
        mayor = maximo(mayor,numero)
print(f"El mayor numero positivo ingresado es: {mayor}")