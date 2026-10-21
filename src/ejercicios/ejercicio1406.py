from funciones import es_par, suma_digitos

contador_impares = 0

numero = int(input("Ingrese un numero: "))

while suma_digitos(numero) >= 10 and suma_digitos(numero) <= 50:
    if not es_par(numero):
        contador_impares += 1
        
    numero = int(input("Ingrese un numero: "))

if not es_par(numero):
    contador_impares += 1

print("Cantidad de numeros impares leidos:", contador_impares)