################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Pruebas ejercicio 6.
"""

from src.ejercicio6 import ordenar_menor_a_mayor, ordenar_mayor_a_menor

def test_ordenar_menor_a_mayor_123():
    """
    Prueba la devolución de los 3 valores ya ordenados.
    """
    resultado = ordenar_menor_a_mayor(-4, 2, 3)
    assert isinstance(resultado, tuple)
    assert resultado == (-4, 2, 3)

def test_ordenar_menor_a_mayor_132():
    """
    Prueba la devolución de los 3 valores desordenados.
    """
    resultado = ordenar_menor_a_mayor(0.2, 7, 1)
    assert isinstance(resultado, tuple)
    assert resultado == (0.2, 1, 7)

def test_ordenar_menor_a_mayor_213():
    """
    Prueba la devolución de los 3 valores desordenados.
    """
    resultado = ordenar_menor_a_mayor(2, 1, 3)
    assert isinstance(resultado, tuple)
    assert resultado == (1, 2, 3)

def test_ordenar_menor_a_mayor_231():
    """
    Prueba la devolución de los 3 valores desordenados.
    """
    resultado = ordenar_menor_a_mayor(3, 4, 2)
    assert isinstance(resultado, tuple)
    assert resultado == (2, 3, 4)

def test_ordenar_menor_a_mayor_312():
    """
    Prueba la devolución de los 3 valores desordenados.
    """
    resultado = ordenar_menor_a_mayor(8, -15, 2.2)
    assert isinstance(resultado, tuple)
    assert resultado == (-15, 2.2, 8)

def test_ordenar_menor_a_mayor_321():
    """
    Prueba la devolución de los 3 valores al revés.
    """
    resultado = ordenar_menor_a_mayor(5, 4, 3)
    assert isinstance(resultado, tuple)
    assert resultado == (3, 4, 5)


def test_ordenar_mayor_a_menor_123():
    """
    Prueba de devolución de los 3 valores al revés.
    """
    resultado = ordenar_mayor_a_menor(-4, 2, 3)
    assert isinstance(resultado, tuple)
    assert resultado == (3, 2, -4)

def test_ordenar_mayor_a_menor_132():
    """
    Prueba la devolución de los 3 valores desordenados.
    """
    resultado = ordenar_mayor_a_menor(0.2, 7, 1)
    assert isinstance(resultado, tuple)
    assert resultado == (7, 1, 0.2)

def test_ordenar_mayor_a_menor_213():
    """
    Prueba la devolución de los 3 valores desordenados.
    """
    resultado = ordenar_mayor_a_menor(2, 1, 3)
    assert isinstance(resultado, tuple)
    assert resultado == (3, 2, 1)

def test_ordenar_mayor_a_menor_231():
    """
    Prueba la devolución de los 3 valores desordenados.
    """
    resultado = ordenar_mayor_a_menor(3, 4, 2)
    assert isinstance(resultado, tuple)
    assert resultado == (4, 3, 2)

def test_ordenar_mayor_a_menor_312():
    """
    Prueba la devolución de los 3 valores desordenados.
    """
    resultado = ordenar_mayor_a_menor(8, -15, 2.2)
    assert isinstance(resultado, tuple)
    assert resultado == (8, 2.2, -15)

def test_ordenar_mayor_a_menor_321():
    """
    Prueba la devolución de los 3 valores al revés.
    """
    resultado = ordenar_mayor_a_menor(5, 4, 3)
    assert isinstance(resultado, tuple)
    assert resultado == (5, 4, 3)
