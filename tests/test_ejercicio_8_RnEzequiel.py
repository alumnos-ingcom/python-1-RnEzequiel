################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas ejercicio 8.
"""

from src.ejercicio8 import es_primo

def test_es_primo_verdadero_positivo():
    """
    Prueba la devolución de un booleano True ante un número primo positivo.
    """
    resultado = es_primo(7)
    assert isinstance(resultado, bool)
    assert resultado == True

def test_es_primo_verdadero_negativo():
    """
    Prueba la devolución de un booleano True ante un número primo negativo.
    """
    resultado = es_primo(-11)
    assert isinstance(resultado, bool)
    assert resultado == True

def test_es_primo_falso_positivo():
    """
    Prueba la devolución de un booleano False ante un número no primo positivo.
    """
    resultado = es_primo(4)
    assert isinstance(resultado, bool)
    assert resultado == False

def test_es_primo_falso_negativo():
    """
    Prueba la devolución de un booleano False ante un número no primo negativo.
    """
    resultado = es_primo(-16)
    assert isinstance(resultado, bool)
    assert resultado == False
