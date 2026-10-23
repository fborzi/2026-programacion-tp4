"""lectura hasta 8 pares este codigo  """
from funciones import es_par

contador_pares = 0 
todos_positivos = True 
while contador_pares < 8:
    numero = int (input ("ingrese un numero: "))
    if es_par(numero):
        contador_pares += 1 
    if numero < 0:
        todos_positivos = False

print(todos_positivos)
