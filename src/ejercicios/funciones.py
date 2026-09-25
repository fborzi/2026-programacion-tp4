def es_par(numero: int):
    """
    Toma un entero y devuelve true/false cuando es par.

    Args:
        numero: es un entero

    Returns:
        retorna True si numero es par y False si es impar
    """
    if numero % 2 == 0:
        return True
    else:
        return False
