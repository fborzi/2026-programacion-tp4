from funciones import maximo
otro_numero = 0

for i  in  range(5): 
    numero = int(input("Ingrese un numero entero: "))
    maximo_numero = maximo(numero, otro_numero)
    nuevo_numero = otro_numero 
    nuevo_numero = maximo(numero, nuevo_numero)

print("el maximo numero leido es: ", maximo_numero)