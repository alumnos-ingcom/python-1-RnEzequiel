################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo
"""

def es_palindromo(texto):
    """
    Recibe una palabra como string y devuelve True si es un palíndromo o False en caso contrario.
    """
    caracter = 0
    simetria = True
    while caracter < len(texto) / 2:
        if texto[caracter] != texto[-caracter - 1]:
            simetria = False
        caracter = caracter + 1
    return simetria


def principal():
    """
    Escribir una función que indique con True si una palabra o frase ingresada se trata de un
    palindromo. Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.
    """
    palabra = input("Ingrese una palabra: ")
    if es_palindromo(palabra):
        print(f"{palabra} es un palíndromo!")
    else:
        print(f"{palabra} no es un palíndromo")

if __name__ == "__main__":
    principal()
