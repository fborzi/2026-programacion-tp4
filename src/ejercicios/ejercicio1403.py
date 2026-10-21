
contador = 0
todos_positivos = True

while contador < 8:
    numero= int(input("Ingrese un numero entero: "))
    if numero % 2 == 0:
        contador += 1

        if numero <= 0:
            todos_positivos = False

print("Todos los numeros ingresados son positivos:", todos_positivos)