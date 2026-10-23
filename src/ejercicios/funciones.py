""" determina si un numero entero es par.
    recibe por parametro un numero y evalua mediante una operacion si es par o no
    retornando un booleano """
    
def es_par(numero:int):
    if numero % 2 == 0:
       return True
    else:
        return False

""" separa los digitos de un numero ingresado y suma el valor total de cada uno de ellos
    recibe un numero entero por parametro,
    toma el valor de cada digito y lo suma para retornar el valor total"""    
    
def suma_digitos(numero:int):
    suma_total=0
    while numero>0:
        digito= numero%10
        suma_total = suma_total + digito
        numero = numero//10
    return suma_total

""" implementa la funcion suma_digitos y retorna mediante un print el valor total de la suma"""

def mostrar_suma_digitos(numero:int):
    suma = suma_digitos(numero)
    print(f"La suma de los digitos es: {suma}")
### la diferencia entre la funcion suma_digitos y la funcion mostrar suma digitos, es que la primera retorna un 
### valor, que puedo usar despues porque queda guardado. En cambio, la segunda al no tener un return solo muestra un mensaje con el print

""" evalua el numero maximo ingresado entre dos numeros,
    recibe por parametros dos numeros enteros,
    evalua cual de los dos es el de mayor valor y retorna el mismo"""
    
def maximo(num1: int, num2: int):
    max : int
    if num1 > num2:
        max = num1
    else:
        max= num2
    return max

""" genera un nombre de usuario de forma predeterminada
    recibe por parametro un string nombre completo
    reemplaza mediante el metodo replece las comas y los espacios para juntar toda la cadena,
    mediante el metodo lowe lo pasa todo a minusculas, y luego se muestran los caracteres de forma inversa
    para mostrarlo de atras hacia adelante,
    retorna la nueva cadena como nombre de usuario"""
    
def usuario(nombre):
    nombre_minuscula = nombre.lower().replace(",", "")
    nombre_ingresado = nombre_minuscula.split()
    nombre_al_reves = nombre_ingresado[::-1]
    usuario = "".join(nombre_al_reves)
    return usuario

""" genera una contraseña de forma predeterminada
    recibe por parametro un numero entero,
    selecciona los 4 ultimos numeros y los muestra como la nueva contraseña retornando ese valor"""
    
def contrasenia_por_defecto(dni:int):
    ultimos= str(dni)[-4:]
    contrasenia= int(ultimos)
    return contrasenia

""" simula el metodo title() devolviendo una cadena con cada palabra ingresada en mayusculas
    recibe por parametro una cadena
    mediante el metodo split se separan las palabras en una lista
    con el metodo capitalize se pone en mayuscula la primer letra de cada palabra
    luego con el metodo join se unen poniendo un " " entre cada palabra
    y se retorna la nueva cadena """
def titulo(cadena):
    palabras_separadas= cadena.split()
    primer_mayusc = [letra.capitalize() for letra in palabras_separadas]
    titulo= " ".join(primer_mayusc)
    if titulo.replace(" ","").isalpha():
        return titulo
    else:
        return "el nombre ingresado tiene un error"
# el metodo isalpha() sirve para corroborar si alguna palabra contiene un numero.
