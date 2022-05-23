################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones
"""

from ejercicio2 import signo

def division_lenta(dividendo, divisor):
    """
    Recibe dos valores como int y devuelve el cociente y resto de su division como tupla
    de dos valores int. En caso de que el divisor sea 0, devuelve ambos valores como 0.
    """
    cociente = 0
    resto = 0
    if divisor != 0:
        signo_division = signo(dividendo) * signo(divisor)
        dividendo = abs(dividendo)
        divisor = abs(divisor)
        while dividendo >= divisor:
            cociente = cociente + 1
            dividendo = dividendo - divisor
        cociente = cociente * signo_division
        resto = dividendo
    return cociente, resto


def principal():
    """
    Escribir una función que mediante restas sucesivas, obtenga el valor del cociente
    y resto de dos números enteros.
    """
    valor_dividendo = int(input("Ingrese el dividendo: "))
    valor_divisor = int(input("Ingrese el divisor: "))
    valor_cociente, valor_resto = division_lenta(valor_dividendo, valor_divisor)
    print(f"El cociente de la division es {valor_cociente} y el resto es {valor_resto}")

if __name__ == "__main__":
    principal()
