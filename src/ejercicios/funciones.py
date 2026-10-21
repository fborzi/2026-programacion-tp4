def es_par (numero: int):
    """(Determina si un numero entero es impar o par) 
    -Args:
    numero: int - numero ingresado por teclado
    returns:
    bool - True si es par. False si no lo es
    """
    if numero % 2 == 0:
        return True
    else:
        return False 


def suma_digitos(numero: int):
    """(Retorna la suma de los digitos de un numero entero)"""
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito 
        numero = numero // 10
    return suma

def mostrar_suma_digitos(numero: int):
    """(Muestra en pantalla la suma de digitos enteros)"""
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero = numero // 10
    print("La suma de los digitos es:", suma)
