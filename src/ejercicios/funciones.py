def es_par(numero:int):
 """Determina si un numero es par o impar
 Args:numero-int:numero ingresado por teclado
 returns:True-si el numero es par, False-si el numero es impar"""
 if numero % 2 == 0:
    return True
 else:
   return False 

def es_positivo(numero:int):
 """Determina si un numero es positivo o negativo
 Args:numero-int:numero ingresado por teclado
 returns:True-si el numero es positivo, False-si el numero es negativo"""
 if numero > 0:
    return True
 else:
   return False

def suma_digitos(numero:int):
 """Suma los digitos de un numero
 Args:numero-int:numero ingresado por teclado
 returns:int:la suma de los digitos del numero"""
 suma = 0
 while numero > 0:
    suma += numero % 10
    numero //= 10
 return suma

def mostrar_suma_digitos(numero:int):
 """Muestra la suma de los digitos de un numero
 Args:numero-int:numero ingresado por teclado"""
 suma = suma_digitos(numero)
 print(f"La suma de los digitos del numero {numero} es: {suma}")
 

def maximo(numero1:int,numero2:int):
 """Determina el numero mayor entre dos numeros
 Args:numero1-int:primer numero ingresado por teclado
       numero2-int:segundo numero ingresado por teclado
 returns:int:el numero mayor entre los dos numeros"""
 if numero1 > numero2:
    return numero1
 else:
   return numero2


def usuario(nombre:str):
   """
      Retorna el usuario del usuario
   
      Args:nombre-str:nombre ingresado por teclado


      returns:str:el usuario del usuario
   """
   nombre_completo = nombre.split(",")
   nombre = (nombre_completo[1]+nombre_completo[0])
   nombre = nombre.replace(",","")
   nombre = nombre.replace(" ","")
   return nombre.lower().lstrip()

def contrasenia_por_defecto(dni:int):
   """
      Retorna la contraseña por defecto del usuario
      Args:dni-int:dni ingresado por teclado
      returns:str:la contraseña por defecto del usuario
   """
   dni_str = str(dni)
   if len(dni_str) < 8:
      dni_str = dni_str.zfill(8)
   return dni_str[-4:]

def titulo(cadena:str):
   """
   Retorna la cadena con la primera letra de cada palabra en mayuscula
   Args:cadena-str:cadena ingresada por teclado
   returns:str:la cadena con la primera letra de cada palabra en mayuscula

   Se utiliza isalpha() para comprobar si el primer carácter
   de cada palabra es una letra antes de convertirlo a mayúscula.
   """

   resultado = ""
   anterior_es_letra = False

   for caracter in cadena:
         if caracter.isalpha():
               if anterior_es_letra:
                  resultado += caracter.lower()
               else:
                  resultado += caracter.upper()
               anterior_es_letra = True
         else:
               resultado += caracter
               anterior_es_letra = False

   return resultado


  