from funciones import maximo
i=0
maximo_final= 0

while i < 5:
    numeroIngresado = (int(input("Ingrese un numero entero: ")))
    if i==0:
        num1= numeroIngresado
    elif i==1:
        num2=numeroIngresado
        maximo_final = maximo(num1,num2)
    elif i>1:
      maximo_final= maximo(maximo_final, numeroIngresado)
    i+=1  
     
print(f"El maximo numero leido es: {maximo_final}")
