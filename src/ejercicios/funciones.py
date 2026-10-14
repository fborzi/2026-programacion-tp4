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

def mostrar_suma_digitos(numero: int):
    suma_total = 0
    while numero > 0:
        digito = numero % 10
        suma_total = suma_total + digito
        numero = numero // 10
    print(f"La suma de los digitos es: {suma_total}")
### la diferencia entre la funcion suma_digitos y la funcion mostrar suma digitos, es que la primera retorna un 
### valor, que puedo usar despues porque queda guardado. En cambio, la segunda al no tener un return solo muestra un mensaje con el print

