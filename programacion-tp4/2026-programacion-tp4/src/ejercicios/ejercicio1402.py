
def es_par(numero):
    return numero % 2 == 0


numero = int(input())

if es_par(numero):
    print("El numero ingresado es: PAR")
else:
    print("El numero ingresado es: IMPAR")

