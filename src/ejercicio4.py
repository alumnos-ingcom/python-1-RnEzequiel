################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Suma lenta
"""

from ejercicio2 import signo

def suma_lenta(numero, otro_numero):
    """
    Recibe 2 valores en forma de int y los suma agregándole valores de a 1 al primer valor
    una cantidad de veces igual al segundo valor respetando el signo de este último.
    """
    signo_de_otro_numero = signo(otro_numero)
    otro_numero = abs(otro_numero)
    while otro_numero > 0:
        numero = numero + (1 * signo_de_otro_numero)
        otro_numero = otro_numero - 1
    return numero


def principal():
    """
    Escribir una función que haga la suma entre dos números enteros sin hacer la operación
    de manera directa. Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones
    resultantes deberán ser 4+1+1+1.
    La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
    """
    valor_uno = int(input("Ingrese un valor: "))
    valor_dos = int(input("Ingrese otro valor a sumar: "))
    suma_de_valores = suma_lenta(valor_uno, valor_dos)
    print(f"La suma de {valor_uno} y {valor_dos} es igual a {suma_de_valores}")

if __name__ == "__main__":
    principal()
