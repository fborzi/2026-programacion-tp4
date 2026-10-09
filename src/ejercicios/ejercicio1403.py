from funciones import es_par,es_positivo

numero = int(input("Ingrese un numero: "))
pares = 0
positivos = 0
while pares < 8:
    if es_par(numero) == True:
        pares+=1
    if es_positivo(numero) == True:
        positivos+=1
    numero = int(input("Ingrese un numero: "))
if pares == 8 and positivos == 8:
    print("Todos los pares ingresados fueron positivos:TRUE")
elif pares == 8 and positivos < 8:
    print("Todos los pares ingresados fueron positivos:FALSE")