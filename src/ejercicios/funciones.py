# 1401 Funcion es_par

def es_par(numero: int) -> bool:
    """Determina si un número entero es par.

    Args:
        numero: es un entero.

    Returns:
        True si el número es par, False en caso contrario.
    """
    return numero % 2 == 0


# 1404 Funcion suma_digitos

def suma_digitos(numero: int) -> int:
    """Calcula la suma de los dígitos de un número entero.

    Args:
        numero: es un entero.

    Returns:
        La suma de los dígitos del número como entero.
    """
    numero = abs(numero)
    suma: int = 0
    while numero > 0:
        suma += numero % 10
        numero //= 10
    return suma


#1405 funcion mostrar_suma_digitos
def mostrar_suma_digitos(numero: int) -> None:
    """Muestra por pantalla la suma de los dígitos de un número entero.

    Args:
        numero: es un entero.
    """
    print(f"La suma de los digitos es: {suma_digitos(numero)}")
# esta funcion retorna none porque no tiene return solo imprime en pantalla
# suma_digitos devuelve el valor ´para poder usarlo despues, pero en mostrar suma el valor se pierde despues de imprimirlo


#1407 Maximo entre dos numeros
def maximo(num_1: int, num_2: int) -> int:
    """Calcula el máximo entre dos números enteros positivos.

    Args:
        num_1: es un entero positivo.
        num_2: es un entero positivo.

    Returns:
        El mayor de los dos números como entero.
    """
    if num_1 > num_2:
        return num_1
    return num_2


#1408 funcion generador de usuarios y contraseñas
def usuario(nombre: str) -> str:
    """Genera el nombre de usuario a partir del nombre completo.

    Args:
        nombre: es una cadena con el formato 'APELLIDO, NOMBRE'.

    Returns:
        Los nombres seguidos de los apellidos, sin espacios, sin comas,
        sin tildes y en minúsculas.
    """
    apellido, nombres = nombre.split(",")
    completo: str = (nombres + apellido).replace(" ", "").lower()
    sin_tildes = str.maketrans("áéíóúü", "aeiouu")
    return completo.translate(sin_tildes)


# 1408 Funcion contrasenia_por_defecto
def contrasenia_por_defecto(dni: int) -> str:
    """Genera la contraseña por defecto a partir del DNI.

    Args:
        dni: es un entero.

    Returns:
        Una cadena con los últimos 4 dígitos del DNI.
    """
    return str(dni)[-4:]


# 1410 Capitalizar como titulo
# Si el usuario tipea un número, este corta la palabra: como no es letra la letra siguiente va en mayúscula
# ("hola2mundo" -> "Hola2Mundo"),
# isalpha() devuelve True si el carácter es una letra. Lo uso para saber
# si el carácter anterior era letra y decidir si el actual va en mayúscula o en minúscula.

def titulo(cadena: str) -> str:
    """Capitaliza una cadena como título, igual que el método title().

    Args:
        cadena: es una cadena de caracteres.

    Returns:
        La cadena con la primera letra de cada palabra en mayúscula
        y el resto en minúscula.
    """
    resultado: str = ""
    anterior_es_letra: bool = False
    for caracter in cadena:
        if anterior_es_letra:
            resultado += caracter.lower()
        else:
            resultado += caracter.upper()
        anterior_es_letra = caracter.isalpha()
    return resultado
