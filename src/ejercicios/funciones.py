
# Ejercicio 1401: determinar si un número es par.
def es_par(numero: int) -> bool:
    """
    Determina si un número es par.

    Args:
        numero: número entero recibido.

    Returns:
        True si es par, False si es impar.
    """
    # El número es par si el resto de dividirlo por 2 es cero.
    return numero % 2 == 0

# Ejercicio 1403: comprobar si los ocho pares fueron positivos.
def leer_ocho_pares() -> bool:
    """
    Solicita ocho números pares y comprueba si todos son positivos.

    Returns:
        True si todos los pares ingresados son positivos.
    """
    # Inicializamos el resultado suponiendo que todos son positivos.
    todos_positivos = True

    # Repetimos ocho veces la lectura de números pares.
    for i in range(8):

        # Solicitamos un número par.
        numero = int(input("Ingrese un número par: "))

        # Si no es par, informamos el error y volvemos a solicitarlo
        # mediante una llamada recursiva a la función.
        if not es_par(numero):
            print("El número debe ser par.")
            return leer_ocho_pares()

        # Si el número es cero o negativo, no es positivo.
        if numero <= 0:
            todos_positivos = False

    # Devolvemos el resultado final.
    return todos_positivos

# Ejercicio 1404: sumar los dígitos de un número.
def suma_digitos(numero: int) -> int:
    """
    Calcula la suma de los dígitos de un número.

    Args:
        numero: número entero recibido.

    Returns:
        La suma de sus dígitos.
    """
    # Convertimos el número a texto y quitamos el signo si es negativo.
    numero = str(abs(numero))

    # Inicializamos el acumulador.
    suma = 0

    # Recorremos cada dígito del número.
    for digito in numero:
        # Convertimos el dígito a entero y lo sumamos.
        suma += int(digito)

    # Devolvemos la suma total.
    return suma


# Ejercicio 1405: mostrar la suma de los dígitos.
def mostrar_suma_digitos(numero: int) -> None:
    """
    Muestra por pantalla la suma de los dígitos.

    Args:
        numero: número entero recibido.
    """
    # Calculamos la suma utilizando la función anterior.
    suma = suma_digitos(numero)

    # Imprimimos el resultado.
    print("La suma de los dígitos es:", suma)
    
    # Ejercicio 1406: contar impares hasta la condición de corte.
def contar_impares():
    """
    Lee números y cuenta los impares hasta que la suma de dígitos
    sea menor que 10 o mayor que 50.
    """
    # Solicitamos un número entero.
    numero = int(input("Ingrese un número entero: "))

    # Calculamos la suma de sus dígitos.
    suma = suma_digitos(numero)

    # Si se cumple la condición de corte, devolvemos cero.
    if suma < 10 or suma > 50:
        return 0

    # Contamos uno si el número es impar.
    impar = 0
    if not es_par(numero):
        impar = 1

    # Continuamos mediante una llamada recursiva.
    return impar + contar_impares()


# Ejercicio 1407: obtener el máximo entre dos números.
def maximo(num_1: int, num_2: int) -> int:
    """
    Devuelve el mayor de dos números.

    Args:
        num_1: primer número.
        num_2: segundo número.

    Returns:
        El mayor de ambos números.
    """
    # Si el primer número es mayor, lo devolvemos.
    if num_1 > num_2:
        return num_1

    # En caso contrario, devolvemos el segundo.
    return num_2


# Ejercicio 1408: generar un nombre de usuario.
def usuario(nombre: str) -> str:
    """
    Genera un usuario a partir de APELLIDO, NOMBRE.

    Args:
        nombre: apellido y nombres separados por coma.

    Returns:
        Nombres y apellido unidos, sin espacios ni comas,
        y en minúsculas.
    """
    # Separamos el apellido de los nombres.
    partes = nombre.split(",")

    # Obtenemos el apellido sin espacios.
    apellido = partes[0].replace(" ", "")

    # Obtenemos los nombres sin espacios.
    nombres = partes[1].replace(" ", "")

    # Unimos nombres y apellido y convertimos a minúsculas.
    return (nombres + apellido).lower()


# Ejercicio 1408: generar la contraseña por defecto.
def contrasenia_por_defecto(dni: int) -> str:
    """
    Devuelve los últimos cuatro dígitos del DNI.

    Args:
        dni: número de documento.

    Returns:
        Los últimos cuatro dígitos como texto.
    """
    # Convertimos el DNI a texto y extraemos los últimos cuatro caracteres.
    return str(dni)[-4:]

