"""Ejercicio 1404: suma de los dígitos de un número entero."""


def suma_digitos(numero: int) -> int:
    """Devuelve la suma de los dígitos de un número entero.

    Por ejemplo, para 438 devuelve 15 (4 + 3 + 8).
    """
    if numero < 0:
        numero = -numero

    suma = 0
    while numero > 0:
        ultimo_digito = numero % 10
        suma = suma + ultimo_digito
        numero = numero // 10

    return suma


def es_par(numero):
    
    if numero % 2 == 0:
        return True
    else:
        return False
    
def ej1403():
    cont_par = 0
    
    while cont_par < 8:
        numero = int(input("ingrese numeros: "))
        if es_par(numero):
            print("el numero ingresado es par")
            cont_par +=1
        else:
            print("el numero ingresado es impar")
            
    if  num_positivo(numero):
        
            print("los numeros pares ingresados son positivos")
    else: print("los pares ingresados no fueron todos positivos")
    
        
def num_positivo(numero):
        cont_positivo = 0
        if cont_positivo == numero >= 0:
                cont_positivo +1
                
    
