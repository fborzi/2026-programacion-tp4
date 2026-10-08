from funciones import es_par

pares_leidos: int = 0
todos_positivos: bool = True

while pares_leidos < 8:
    numero: int = int(input())
    if es_par(numero):
        pares_leidos += 1
        if numero <= 0:
            todos_positivos = False

print(f"Todos los pares ingresados fueron positivos: {todos_positivos}")
