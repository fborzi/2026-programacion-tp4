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
    


def maximo(num_1, nume_2):
    """(Calcula y retorna el maximo entre dos numeros positivos)"""
    if num_1 > nume_2:
        return num_1
    else:
        return nume_2


def usuario(nombre):
    """(Recibe como parametro el nombre de un usuario y retorna el nombre)"""
    nombre = nombre.lower()
    partes = nombre.replace(",", "").split()

    return partes[1] + partes[0]

def contrasenia_por_defecto(dni):
    """(Recibe un dni y retorna una cadena con los ultimos 4 numeros)"""
    dni = str(dni)
    return dni[-4:]


def titulo(cadena):
    palabras = cadena.lower().split()
    resultado = ""

    for palabra in palabras:
        resultado = resultado + palabra[0].upper() + palabra[1:] + " "

    return resultado.strip()

