"""
Pruebas ejercicio 1.
"""

import src.ejercicio1 as ej1

def test_convervtir_a_fahrrenheit_positivo():
    """
    Prueba la conversión de un número positivo de centígrados a fahrenheit.
    """
    resultado = ej1.convertir_a_fahrrenheit(14)
    assert isinstance(resultado, float)
    assert resultado > 0
    assert resultado == 57.2

def test_convertir_a_fahrrenheit_negativo():
    """
    Prueba la conversión de un número negativo de centígrados a fahrenheit.
    """
    resultado = ej1.convertir_a_fahrrenheit(-20)
    assert isinstance(resultado, float)
    assert resultado < 0
    assert resultado == -4.0

def test_convertir_a_centigrados_positivo():
    """
    Prueba la conversión de un número positivo de fahrenheit a centígrados.
    """
    resultado = ej1.convertir_a_centigrados(41)
    assert isinstance(resultado, float)
    assert resultado > 0
    assert resultado == 5.0

def test_convertir_a_centigrados_negativo():
    """
    Prueba la conversión de un número negativo de fahrenheit a centígrados.
    """
    resultado = ej1.convertir_a_centigrados(-8.5)
    assert isinstance(resultado, float)
    assert resultado < 0
    assert resultado == -22.5
