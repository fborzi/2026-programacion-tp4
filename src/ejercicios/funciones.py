def es_par(numero:int):
    if numero % 2 == 0:
       return True
    else:
        return False
    
def suma_digitos(numero:int):
    suma_total=0
    while numero>0:
        digito= numero%10
        suma_total= suma_total+ digito
        numero = numero//10
    return suma_total

def mostrar_suma_digitos(numero:int):
    suma = suma_digitos(numero)
    print(f"La suma de los digitos es: {suma}")
### la diferencia entre la funcion suma_digitos y la funcion mostrar suma digitos, es que la primera retorna un 
### valor, que puedo usar despues porque queda guardado. En cambio, la segunda al no tener un return solo muestra un mensaje con el print

def maximo(num1: int, num2: int):
    max : int
    if num1 > num2:
        max = num1
    else:
        max= num2
    return max

def usuario(nombre):
    nombre_minuscula = nombre.lower().replace(",", "")
    nombre_ingresado = nombre_minuscula.split()
    nombre_al_reves = nombre_ingresado[::-1]
    usuario = "".join(nombre_al_reves)
    return usuario

def contrasenia_por_defecto(dni:int):
    ultimos= str(dni)[-4:]
    contrasenia= int(ultimos)
    return contrasenia

def titulo(cadena):
    palabras_separadas= cadena.split()
    primer_mayusc = [letra.capitalize() for letra in palabras_separadas]
    titulo= " ".join(primer_mayusc)
    if titulo.replace(" ","").isalpha():
        return titulo
    else:
        return "el nombre ingresado tiene un error"
# el metodo isalpha() sirve para corroborar si alguna palabra contiene un numero.