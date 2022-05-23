################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos

"""

def signo(numero):
    """
    Ingresa un número como float y devuelve 1 si es positivo, -1 si es negativo y 0 si es
    cero en forma de int.
    """
    resultado = 0
    doble = numero + numero
    if doble > numero:
        resultado = 1
    elif doble < numero:
        resultado = -1
    return resultado


def principal():
    """
    Escribir una función que reciba un número e indique si el mismo es positivo, negativo
    o cero utilizando sumas y restas.
    """
    valor = float(input("Ingrese un valor a analizar: "))
    signo_de_valor = signo(valor)
    print(f"El signo de {valor} es {signo_de_valor} (1 = positivo; -1 = negativo; 0 = cero)")

if __name__ == "__main__":
    principal()
