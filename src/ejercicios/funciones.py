# ejercicio 1:

def es_par(numero: int ):
    if numero % 2 == 0: 
       return True
    else:
       return False 

#ejercicio 4 suma de 4 digitos 

def suma_digitos(numero: int) :
    suma = 0
    while numero > 0:
         digito = numero % 10
         suma = suma + digito
         numero = numero // 10
    return suma
 
print (suma_digitos(438))


#ejercicio 5 mostar suma de digitos 

def mostrar_suma_digitos(numero: int):
    suma = 0

    while numero > 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10

    print("la suma de los digitos es:", suma)
   
resultado = mostrar_suma_digitos(438)
print(resultado) 
""" resultado es None porque la funcion no tiene un return, solo imprime el resultado.
    en el anterio si tiene retun por eso impreme el resultado de la suma de los digitos. """

#ejercicio 7 maximo entre dos numeros
def maximo(num_1: int, num_2: int):
    if num_1 > num_2:
        return num_1
    else:
        return num_2
print(maximo(10, 25))  

"""ejercicio 8 generador de usario y contraseña"""
def usuario(nombre: str):
    apellido, nombres = nombre.split(",", 1)
    usuario_generado = (nombres + apellido).replace(" ", "").lower()
    return usuario_generado

def contrasenia_por_defecto(dni: int):
    return str(dni)[-4:]
print(usuario("GARCIA, MARAIA VERONICA"))
print(contrasenia_por_defecto(12345678))
#EJERCIO 10 CAPITALIZAR COMO TITULO 

def titulo(cadena: str):
    palabras = cadena.split()
    resultado = ""

    for palabra in palabras:
        if palabra.isalpha():
            palabra = palabra[0].upper() + palabra[1:].lower()

        resultado = resultado + palabra + " "

    return resultado.strip()
print(titulo("esto es una prueba"))

