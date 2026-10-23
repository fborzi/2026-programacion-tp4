from funciones import maximo

numero = int(input("ingresa un numero: "))
mayor = numero

contador = 1

while contador < 5:
    numero = int(input("Ingresa un numero: "))
    mayor = maximo(mayor, numero)
    contador += 1

print("el maximo numero leido es:", mayor)