def maximo(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2


mayor = int(input())

for i in range(4):
    numero = int(input())
    mayor = maximo(mayor, numero)

print("El maximo numero leido es:", mayor)
