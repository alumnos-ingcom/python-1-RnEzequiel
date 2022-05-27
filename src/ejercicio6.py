################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. Ordenar 3 valores
"""

def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Recibe 3 valores float y los devuelve ordenados de menor a mayor
    """
    if uno > dos:
        uno, dos = dos, uno
    if uno > tres:
        uno, tres = tres, uno
    if dos > tres:
        dos, tres = tres, dos
    return uno, dos, tres

def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Recibe 3 valores float y los devuelve ordenados de mayor a menor
    """
    if uno < dos:
        uno, dos = dos, uno
    if uno < tres:
        uno, tres = tres, uno
    if dos < tres:
        dos, tres = tres, dos
    return uno, dos, tres


def principal():
    """
    Escribir una función que a partir de tres variables de tipo entero retorne una tupla
    con dichos valores ordenados de menor a mayor. Y Viceversa
    """
    valor_uno = float(input("Ingrese el primer valor: "))
    valor_dos = float(input("Ingrese el segundo valor: "))
    valor_tres = float(input("Ingrese el tercer valor: "))
    valores_ascendentes = ordenar_menor_a_mayor(valor_uno, valor_dos, valor_tres)
    valores_descendentes = ordenar_mayor_a_menor(valor_uno, valor_dos, valor_tres)
    print(f"ascendente = {valores_ascendentes}")
    print(f"descendente = {valores_descendentes}")

if __name__ == "__main__":
    principal()
