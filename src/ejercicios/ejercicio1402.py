from funciones import es_par
"""Este ejercicio evalua si el numero ingresado por teclado es par o impar
utilizando al funcion es_par"""
numero=int(input("Ingrese un numero: "))
if es_par(numero):
    print("El numero ingresado es : PAR")
else:
    print("El numero ingresado es : IMPAR")