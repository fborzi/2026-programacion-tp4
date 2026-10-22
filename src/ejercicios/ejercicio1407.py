from funciones import maximo

maximo_leido = 0
for i in range(5):
    numero = int(input("Ingrese un numero: "))
    maximo_leido = maximo(maximo_leido, numero)
    
print("El maximo numero leido es:", maximo_leido)