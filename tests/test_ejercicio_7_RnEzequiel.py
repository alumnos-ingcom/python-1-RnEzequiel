################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas ejercicio 7.
"""

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal

def test_sexadecimal_a_decimal():
    """
    Prueba la conversión de horas, minutos y segundos a su total en segundos.
    """
    resultado = sexadecimal_a_decimal(2, 5, 10)
    assert isinstance(resultado, int)
    assert resultado > 0
    assert resultado == 7510

def test_decimal_a_sexadecimal():
    """
    Prueba la conversión de un total de segundos a horas, minutos y segundos.
    """
    resultado = decimal_a_sexadecimal(3661)
    assert isinstance(resultado, tuple)
    assert resultado[0] >= 0
    assert resultado[1] >= 0
    assert resultado[2] >= 0
    assert resultado == (1, 1, 1)
