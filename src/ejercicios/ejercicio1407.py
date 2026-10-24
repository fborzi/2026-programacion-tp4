#ejercio 1407 maximo entre ddos numeros 

def maximo(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2



mayor = int(input("ingresa un numero positivo: "))

for i in range(4):
    numero = int(input("ingresaotro numero positivo: "))
    mayor = maximo(mayor, numero)

print("el maximo numero leido es:", mayor)