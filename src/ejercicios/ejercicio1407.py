from funciones import maximo

numero = int(input("Ingrese un numero: "))
mayor = numero

for i in range(4):
    numero = int(input("Ingrese un numero: "))
    mayor = maximo(mayor, numero)

print("El maximo numero leido es:", mayor)
