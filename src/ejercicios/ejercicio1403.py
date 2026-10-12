from funciones import es_par

num_pares = 0
todos_positivos = True

while num_pares < 8:
    numero=int(input("Ingrese un numero entero: "))
    if es_par(numero):
        num_pares = num_pares + 1
        if numero < 0:
          todos_positivos=False
     
print(f"Todos los números pares ingresados fueron positivos: {todos_positivos}")
