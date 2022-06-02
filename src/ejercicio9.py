################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores Primos
"""

def factores_primos(numero):
    """
    Recibe un número positivo como int y devuelve una tuple con todos sus factores primos.
    """
    divisor = 2
    factores = ()
    while divisor < numero:
        if numero % divisor == 0:
            factores = factores + (divisor,)
            numero = numero // divisor
            divisor = 2
        else:
            divisor = divisor + 1
    factores = factores + (numero,)
    return factores


def principal():
    """
    Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
    """
    valor_numero = int(input("Ingrese un número: "))
    resultado = factores_primos(valor_numero)
    print(f"Los factores de {valor_numero} son {resultado}")

if __name__ == "__main__":
    principal()
