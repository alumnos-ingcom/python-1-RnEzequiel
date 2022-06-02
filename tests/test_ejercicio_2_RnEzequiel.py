################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas ejercicio 2.
"""

from src.ejercicio2 import signo

def test_signo_positivo():
    """
    Prueba la devolución del valor "1" ante un número positivo.
    """
    resultado = signo(4)
    assert isinstance(resultado, int)
    assert resultado == 1

def test_signo_cero():
    """
    Prueba la devolución del valor "0" ante un valor de cero.
    """
    resultado = signo(0)
    assert isinstance(resultado, int)
    assert resultado == 0

def test_signo_negativo():
    """
    Prueba la devolución del valor "-1" ante un número negativo.
    """
    resultado = signo(-8)
    assert isinstance(resultado, int)
    assert resultado == -1
