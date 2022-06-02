################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
8. Números primos
"""

def es_primo(numero):
    """
    Recibe un valor como int y devuelve un valor booleano: True si el valor primo y False
    si no lo es.
    """
    numero = abs(numero)
    numero_tiene_divisores = False
    divisor = 2
    while divisor <= numero / 2:
        if numero % divisor == 0:
            numero_tiene_divisores = True
        divisor = divisor + 1
    return not numero_tiene_divisores


def principal():
    """
    Escribir una función que indique con True si un numero indicado es Primo.
    """
    valor = int(input("Ingrese un valor: "))
    if es_primo(valor):
        print(f"{valor} es un número primo")
    else:
        print(f"{valor} no es un número primo")

if __name__ == "__main__":
    principal()
