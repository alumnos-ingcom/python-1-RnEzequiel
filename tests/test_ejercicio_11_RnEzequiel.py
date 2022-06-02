################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas ejercicio 11.
"""

from src.ejercicio11 import es_multiplo

def test_es_multiplo_verdadero():
    """
    Prueba la devolución de un booleano True ante un número y uno de sus divisores.
    """
    resultado = es_multiplo(20, 2)
    assert isinstance(resultado, bool)
    assert resultado == True

def test_es_multiplo_falso():
    """
    Prueba la devolución de un booleano False ante un número y otro que no sea divisor suyo.
    """
    resultado = es_multiplo(60, 11)
    assert isinstance(resultado, bool)
    assert resultado == False
