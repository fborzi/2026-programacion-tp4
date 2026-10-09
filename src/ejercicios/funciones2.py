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