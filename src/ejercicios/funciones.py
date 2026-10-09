def es_par(numero):
    
    if numero % 2 == 0:
        return True
    else:
        return False
    
def ej1403():
    cont_par = 0
    
    while cont_par < 8:
        numero = int(input("ingrese numeros: "))
        if es_par(numero):
            print("el numero ingresado es par")
            cont_par +=1
        else:
            print("el numero ingresado es impar")
            
    if  num_positivo(numero):
        
            print("los numeros pares ingresados son positivos")
    else: print("los pares ingresados no fueron todos positivos")
    
        
def num_positivo(numero):
        cont_positivo = 0
        if cont_positivo == numero >= 0:
                cont_positivo +1
                
    
