from funciones import maximo

maximo_leido: int = int(input())

for _ in range(4):
    numero: int = int(input())
    maximo_leido = maximo(maximo_leido, numero)

print(f"El maximo numero leido es: {maximo_leido}")
