################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Multiplos de
"""

def es_multiplo(numero, multiplo):
    """
    Recibe 2 valores en forma de int y devuelve True si el primero es multiplo del segundo.
    """
    numero = abs(numero)
    multiplo = abs(multiplo)
    while numero >= multiplo:
        numero = numero - multiplo
    resto_cero = numero == 0
    return resto_cero


def principal():
    """
    Escribir una función que indique con True si un número entero es multiplo de otro,
    utilizando sumas y restas.
    """
    valor_numero = int(input("Ingrese un número: "))
    valor_multiplo = int(input("Ingrese un múltiplo a verificar: "))
    if es_multiplo(valor_numero, valor_multiplo):
        print(f"{valor_numero} es múltiplo de {valor_multiplo}")
    else:
        print(f"{valor_numero} no es múltiplo de {valor_multiplo}")

if __name__ == "__main__":
    principal()
