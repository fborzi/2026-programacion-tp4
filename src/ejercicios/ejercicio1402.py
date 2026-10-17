from funciones import es_par
""" Este programa determina si un numero entero ingresado por el usuario es PAR o IMPAR utilizando
la funcion es_par"""

numero = int(input("Ingrese un numero entero: "))

if es_par(numero):
 print ("El numero ingresado es PAR")
else:
 print ("El numero ingresado es IMPAR")
