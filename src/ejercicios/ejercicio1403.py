"""
Importamos la funcion creada en funciones.py que identifica numeros pares
contamos cuantos numero pares ingresamos.
suponemos que inicialmente que todos los pares son positivos
repetimos hasta ingresar ocho numeros pares
"""

from funciones import leer_ocho_pares

resultado = leer_ocho_pares()
print("Todos los pares ingresados fueron positivos:")
print(resultado)
