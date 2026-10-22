"""
Importamos la funcion creada en funciones.py
solicitamos al usuario un numero entero
llamamos a la funcion para saber si el numero es par, si
devuelve true es par y si devuelve false es impar.
"""
from funciones import es_par
numero = int(input("Ingrese un numero entero: "))

if es_par(numero):
    print("El numero ingresado es: PAR")
else:
    print("El numero Ingresado es: IMPAR")