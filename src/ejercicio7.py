################
# Ezequiel Renolfi - @RnEzequiel
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
7. Transformación de un número
"""

def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Recibe horas, minutos y segundos como 3 valores enteros positivos en forma de int y
    devuelve su conversion a segundos como int.
    """
    minutos = minutos + horas * 60
    segundos = segundos + minutos * 60
    return segundos

def decimal_a_sexadecimal(numero):
    """
    Recibe una cantidad de segundos como int y devuelve su conversión a horas, minutos y
    segundos como 3 valores int en una tuple.
    """
    segundos = numero % 60
    minutos = numero // 60
    horas = minutos // 60
    minutos = minutos % 60
    return horas, minutos, segundos


def principal():
    """
    Escribir un programa que permita transformar un número solicitado expresado en grados,
    minutos y segundos a segundos. Y otra que haga el cambio en el sentido contrario,
    devolviendo una tuple.
    """
    valor_horas = int(input("Ingrese horas a transformar: "))
    valor_minutos = int(input("Ingrese minutos a transformar: "))
    valor_segundos = int(input("Ingrese segundos a transformar: "))
    resultado = sexadecimal_a_decimal(valor_horas, valor_minutos, valor_segundos)
    print(f"El tiempo ingresado es igual a {resultado} segundos")
    valor_segundos = int(input("Ingrese tiempo en segundos a transformar: "))
    resultado = decimal_a_sexadecimal(valor_segundos)
    print(f"{valor_segundos} en sexagesimal es igual a {resultado}")

if __name__ == "__main__":
    principal()
