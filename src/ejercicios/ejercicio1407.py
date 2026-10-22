"""
Importamos la funcion creada en funciones.py maximo
solicitamos el primer numero, leemos los cuatro numeros restantes,
se solicita otro numero y comparamos el numero ingresado con el
maximo actual, y se muestra el maximos de los cinco numeros.
"""

from funciones import maximo

mayor = int(input("Ingrese un número positivo: "))

for i in range(4):
    numero = int(input("Ingrese otro número positivo: "))
    mayor = maximo(mayor, numero)
print("El maximo numero leido es:", mayor)
