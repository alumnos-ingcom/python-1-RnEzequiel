################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas ejercicio 9.
"""

from src.ejercicio9 import factores_primos

def test_factores_primos_1():
    """
    Prueba la devolución de un mismo valor primo ingresado en una tuple.
    """
    resultado = factores_primos(3)
    assert isinstance(resultado, tuple)
    assert resultado == (3,)

def test_factores_primos_3():
    """
    Prueba la devolución de tres factores primos en una tuple.
    """
    resultado = factores_primos(12)
    assert isinstance(resultado, tuple)
    assert resultado == (2, 2, 3)

def test_factores_primos_4():
    """
    Prueba la devolución de cuatro factores primos en una tuple.
    """
    resultado = factores_primos(90)
    assert isinstance(resultado, tuple)
    assert resultado == (2, 3, 3, 5)
