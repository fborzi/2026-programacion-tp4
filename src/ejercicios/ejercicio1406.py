from funciones import es_par, suma_digitos

impares: int = 0
numero: int = int(input())

while 10 <= suma_digitos(numero) <= 50:
    if not es_par(numero):
        impares += 1
    numero = int(input())

print(f"Cantidad de numeros impares leidos: {impares}")
