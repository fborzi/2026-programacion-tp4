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