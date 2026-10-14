from funciones import suma_digitos, es_par

impares = 0

numeroIngresado = (int(input("Ingrese un numero entero: ")))

valorSumaDigitos = suma_digitos(numeroIngresado)
print(valorSumaDigitos)
# while (valorSumaDigitos > 10 and valorSumaDigitos < 50) :
#     if not es_par(numeroIngresado):
#         impares =+1
    
#     numeroIngresado = (int(input("Ingrese un numero entero: ")))
#     valorSumaDigitos = suma_digitos(numeroIngresado)