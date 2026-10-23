def es_par(numero: int):
    """ 
    determina si la funcion es par o no
    args: 
        numero: entero
    returns: 
        bool - retorna si el numero ingresado es par o no
    """
    if numero % 2 == 0:
        return True
    else:
        return False

def es_par2(numero: int):
    """
    """
    return numero % 2 == 0



def suma_digitos(numero):
    """
    suma los digitos del numero entero ingresado 
    primer digitos + segundo digito y asi 
    args: 
    numero :
      entero 
    returns : 
     int - retorna la suma de los 3 digitos del numero 
    """
    suma = 0
    while numero !=0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
        return suma 

def mostrar_suma_digitos(numero: int):
    """
    esta funcion define un numero entero como argumento e 
    imprime en pantalla la suma de sus digitos
    args:
    numero: entero 
    returns: int- la suma de los digitos
    """
    def mostrar_suma_digitos(numero):
     suma = 0

    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    print("La suma de los digitos es:", suma)



def maximo(num_1: int, num_2: int):
    """ 
    esta funcion define maximo con num_1 y num_2 y
      pide que retorne el maximo de los dos
      args:
      maximo : entero
      returns: int - el maximo de los dos 
    """
    if num_1 > num_2:
        return num_1 
    else: 
        return num_2

def usuario(nombre):
 """
 esta funcion define usuario y pide un nombre y apellido
    args:
    usuario: String
    returns: nombre y apellido sin comas, espacios y en minuscula
 """
 nombre_completo = input("ingrese nombre completo: ")
 apellido, nombres = nombres.split(", ")
 usuario = nombres + apellido
 usuario = usuario.replace(" ", "")
 usuario = usuario.lower()
 return usuario


def contrasenia_por_defecto(dni):
    """
    esta funcion define contrasenia por defecto al dni que se ingrese
    args:
    Integer
    returns: los ultimos 4 digitos ded dni
    """
    return str(dni)[-4:]


def titulo(cadena):
    """
    esta funcion define a titulo como una cadena de Strings que luego 
    como tittle pasara a tener todas las primeras letras de cada palabra en mayuscula
    args:
    titulo: String
    returns: las palabras con la primera letra en mayuscula con el metodo isalpha() q comprueba si un 
    caracter es una letra, si el usuario escribe un numero dentro de una palabra devuelve false
    """

    resultado = ""
    nueva_palabra = True

    for caracter in cadena:
        if caracter == " ":
            resultado = resultado + caracter
            nueva_palabra = True
        elif nueva_palabra and caracter.isalpha():
            resultado = resultado + caracter.upper()
            nueva_palabra = False
        else:
            resultado = resultado + caracter.lower()
            if caracter.isalpha():
                nueva_palabra = False

    return resultado
    