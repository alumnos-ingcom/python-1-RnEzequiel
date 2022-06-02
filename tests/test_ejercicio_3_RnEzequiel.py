################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas ejercicio 3.
"""

from src.ejercicio3 import compara

def test_compara_mayor():
    """
    Prueba la devolución del valor "1" cuando el primer número es mayor que el segundo.
    """
    resultado = compara(8, 2.5)
    assert isinstance(resultado, int)
    assert resultado == 1

def test_compara_igual():
    """
    Prueba la devolución del valor "0" cuando ambos numeros son iguales.
    """
    resultado = compara(3, 3)
    assert isinstance(resultado, int)
    assert resultado == 0

def test_compara_menor():
    """
    Prueba la devolución del valor "-1" cuando el primer número es menor que el segundo.
    """
    resultado = compara(-4, 7)
    assert isinstance(resultado, int)
    assert resultado == -1
