################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas ejercicio 5.
"""

from src.ejercicio5 import division_lenta

def test_division_lenta_positivo():
    """
    Prueba la división entre dos valores enteros positivos.
    """
    resultado = division_lenta(13, 5)
    assert isinstance(resultado, tuple)
    assert resultado[0] > 0
    assert resultado == (2, 3)

def test_division_lenta_negativo_izq():
    """
    Prueba la división entre un primer valor negativo y un segundo positivo.
    """
    resultado = division_lenta(-17, 4)
    assert isinstance(resultado, tuple)
    assert resultado[0] < 0
    assert resultado == (-4, 1)

def test_division_lenta_negativo_der():
    """
    Prueba la división entre un primer valor positivo y un segundo negativo.
    """
    resultado = division_lenta(90, -3)
    assert isinstance(resultado, tuple)
    assert resultado[0] < 0
    assert resultado == (-30, 0)

def test_division_lenta_negativo():
    """
    Prueba la división entre dos valores enteros negativos.
    """
    resultado = division_lenta(-9, -2)
    assert isinstance(resultado, tuple)
    assert resultado[0] > 0
    assert resultado == (4, 1)

def test_division_lenta_dividendo_cero():
    """
    Prueba una división con dividendo igual a 0.
    """
    resultado = division_lenta(0, 12)
    assert isinstance(resultado, tuple)
    assert resultado == (0, 0)

def test_division_lenta_divisor_cero():
    """
    Prueba una división con divisor igual a 0.
    """
    resultado = division_lenta(34, 0)
    assert isinstance(resultado, tuple)
    assert resultado == (None, None)
