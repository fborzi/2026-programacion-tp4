# EJERCICIO 1401, 1402 y 1403
# Funcion que determina si un numero es par

def es_par(numero):
    return numero % 2 == 0


# EJERCICIO 1404
# Funcion que suma los digitos de un numero

def suma_digitos(numero):
    numero = abs(numero)
    suma = 0

    while numero > 0:
        suma += numero % 10
        numero //= 10

    return suma


# EJERCICIO 1405
# Funcion que muestra la suma de los digitos

def mostrar_suma_digitos(numero):
    print("La suma de los digitos es:", suma_digitos(numero))


# EJERCICIO 1407
# Funcion que devuelve el maximo entre dos numeros

def maximo(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2


# EJERCICIO 1408 y 1409
# Funcion que genera el nombre de usuario

def usuario(nombre):
    partes = nombre.split(",")

    apellido = partes[0]
    nombres = partes[1]

    resultado = (nombres + apellido).replace(" ", "")

    return resultado.lower()


# Funcion que genera la contrasena con los ultimos 4 digitos del DNI

def contrasenia_por_defecto(dni):
    return str(dni)[-4:]


# EJERCICIO 1410
# Funcion que convierte una cadena a formato titulo

def titulo(cadena):
    resultado = ""
    inicio_palabra = True

    for caracter in cadena:
        if caracter.isalpha():
            if inicio_palabra:
                resultado += caracter.upper()
            else:
                resultado += caracter.lower()

            inicio_palabra = False
        else:
            resultado += caracter
            inicio_palabra = True

    return resultado
