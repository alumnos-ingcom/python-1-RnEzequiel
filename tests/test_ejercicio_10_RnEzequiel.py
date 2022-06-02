################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas ejercicio 10.
"""

from src.ejercicio10 import es_palindromo

def test_es_palindromo_verdadero():
    """
    Prueba la devolución de un booleano True ante una cadena palíndromo.
    """
    resultado = es_palindromo("neuquen")
    assert isinstance(resultado, bool)
    assert resultado == True

def test_es_palindromo_falso():
    """
    Prueba la devolución de un booleano False ante una cadena no palíndromo.
    """
    resultado = es_palindromo("bariloche")
    assert isinstance(resultado, bool)
    assert resultado == False
