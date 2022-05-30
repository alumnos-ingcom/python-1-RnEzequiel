################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas ejercicio 4.
"""

from src.ejercicio4 import suma_lenta

def test_suma_lenta_positivo():
    """
    Prueba la suma de dos valores enteros positivos.
    """
    resultado = suma_lenta(3, 5)
    assert isinstance(resultado, int)
    assert resultado > 0
    assert resultado == 8

def test_suma_lenta_negativo():
    """
    Prueba la suma entre un primer valor negativo y un segundo positivo.
    """
    resultado = suma_lenta(-2, 6)
    assert isinstance(resultado, int)
    assert resultado > 0
    assert resultado == 4

def test_suma_lenta_resta_positivo():
    """
    Prueba la suma entre un primer valor positivo y un segundo negativo.
    """
    resultado = suma_lenta(4, -10)
    assert isinstance(resultado, int)
    assert resultado < 0
    assert resultado == -6

def test_suma_lenta_resta_negativo():
    """
    Prueba la suma entre dos valores negativos.
    """
    resultado = suma_lenta(-9, -3)
    assert isinstance(resultado, int)
    assert resultado < 0
    assert resultado == -12

def test_suma_lenta_cero_izq():
    """
    Prueba la suma entre un primer valor igual a 0 y un segundo cualquiera.
    """
    resultado = suma_lenta(0, 5)
    assert isinstance(resultado, int)
    assert resultado > 0
    assert resultado == 5

def test_suma_lenta_negativo():
    """
    Prueba la suma entre un primer valor cualquiera y un segundo igual a 0.
    """
    resultado = suma_lenta(-1, 0)
    assert isinstance(resultado, int)
    assert resultado < 0
    assert resultado == -1
