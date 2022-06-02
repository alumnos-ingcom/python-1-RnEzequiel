################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversión de temperaturas

"""

def convertir_a_fahrrenheit(centigrados):
    """
    Ingresa los grados centigrados como float y devuelve la misma temperatura
    en grados fahrenheit como float
    """
    resultado = (centigrados * 9 / 5) + 32
    return resultado

def convertir_a_centigrados(fahrenheit):
    """
    Ingresa los grados fahrenheit como float y devuelve la misma temperatura
    en grados centigrados como float
    """
    resultado = 5 / 9 * (fahrenheit - 32)
    return resultado


def principal():
    """
    Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

    Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit
    como un número decimal, utilice esta formula para calcular los grados centígrados y
    retorne el resultado obtenido. Y viceversa.
    """
    valor = float(input("Ingrese un valor en grados centígrados: "))
    valor_resultado = convertir_a_fahrrenheit(valor)
    print(f'{valor}°C es igual a {valor_resultado}°F')
    valor = float(input("Ingrese un valor en grados fahrenheit: "))
    valor_resultado = convertir_a_centigrados(valor)
    print(f'{valor}°C es igual a {valor_resultado}°F')

if __name__ == "__main__":
    principal()
