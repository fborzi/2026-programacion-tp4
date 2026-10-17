from funciones import es_par

cantidad_pares = 0
todos_positivos = True

while cantidad_pares < 8:
    numero = int(input("Ingrese un numero entero: "))
    
    if es_par(numero):
        cantidad_pares += 1

        if numero <= 0:
            todos_positivos= False

print("Todos los pares ingresados fueron positivos:", todos_positivos)
