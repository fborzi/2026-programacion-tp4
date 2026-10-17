def es_par(numero:int):

 """ Determina si un número entero recibido por parametro es par.
 Args:
    numero: int- numero ingresado por teclado
 Returns:
    booleano- True si es par o False si no lo es"""

 if numero % 2 == 0:
   return True
 else:
   return False

def mostrar_suma_digitos(numero:int):
   
 """ Calcula y muestra en pantalla la suma de los dígitos de un número entero.
 Args:
  numero: int - número entero recibido por parámetro
 Returns:
  None - no retorna ningún valor, solamente muestra la suma en pantalla."""
    
 suma = 0

 for digito in str(numero):
        suma += int(digito)

 print("La suma de los digitos es:", suma)

def suma_digitos(numero: int):

 """ Calcula la suma de los dígitos de un número entero recibido por parámetro.
 Args:

 numero: int - número entero recibido por parámetro

 Returns:

 int - la suma de los dígitos del número."""
    
 suma = 0

 for digito in str(numero):
        suma += int(digito)

 return suma

def maximo(num_1: int, num_2: int):

 """ Calcula el máximo entre dos números positivos.

 Args:
 num_1: int - primer número entero
 num_2: int - segundo número entero

 Returns:
 int - el mayor de los dos números """

 if num_1 > num_2:
        return num_1
 else:
        return num_2

def usuario(nombre: str):
      
 """Genera el nombre de usuario a partir del nombre completo.

 Args:
 nombre: str - nombre completo con formato APELLIDO, NOMBRE

 Returns:
 str - nombres y apellidos en minúsculas, sin espacios ni comas """
    
 partes = nombre.split(",")
 apellido = partes[0]
 nombres = partes[1]

 nombre_usuario = (nombres + apellido).replace(" ", "").lower()

 nombre_usuario = nombre_usuario.replace("á", "a")
 nombre_usuario = nombre_usuario.replace("é", "e")
 nombre_usuario = nombre_usuario.replace("í", "i")
 nombre_usuario = nombre_usuario.replace("ó", "o")
 nombre_usuario = nombre_usuario.replace("ú", "u")
 return nombre_usuario


def contrasenia_por_defecto(dni: int):

 """ Genera una contraseña con los últimos 4 dígitos del DNI.

 Args:
 dni: int - número de DNI del usuario

 Returns:
 str - los últimos 4 dígitos del DNI """
    
 dni = str(dni)
 return dni[-4:]

def titulo(cadena: str):
    
 """Convierte la primera letra de cada palabra a mayúscula.

 Args:
 cadena: str - cadena de caracteres recibida por parámetro

 Returns:
 str - cadena con la primera letra de cada palabra en mayúscula 
 
 Nota:
 Se utiliza isalpha() para comprobar si el primer carácter
 de cada palabra es una letra antes de convertirlo a mayúscula."""
    
 palabras = cadena.split()
 resultado = ""

 palabras = cadena.split()
   
 resultado = ""

 for palabra in palabras:
        palabra = palabra.lower()

        if palabra[0].isalpha():
            palabra = palabra[0].upper() + palabra[1:]

        resultado += palabra + " "
 
 return resultado.strip()
