"""
Importamos la funcion creada en funciones.py 
se solicita un nombre de usuario, lo convertimos en minuscula para que sea mas facil
de comparar, comprobamos si el nombre tiene juan o maria, solicitamos el dni 
y generamos el usuario y la contraseña. Mostramos los datos, y si el nombre contiene
juan o maria se termina la lectura.
"""

from funciones import usuario, contrasenia_por_defecto

nombre_completo = input("Ingrese APELLIDO, NOMBRE: ")
nombre_minusculas = nombre_completo.lower()

if "juan" not in nombre_minusculas and "maria" not in nombre_minusculas and "maría" not in nombre_minusculas:
    
    dni = int(input("Ingrese el DNI: "))
    nombre_generado = usuario(nombre_completo)
    contrasenia = contrasenia_por_defecto(dni)

    print("Usuario:", nombre_generado)
    print("Contrasenia:", contrasenia)

else:
    print("Se encontró Juan o María. Fin del programa.")
