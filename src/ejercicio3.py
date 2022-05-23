################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Comparación de números
"""

def compara(numero, otro_numero):
    """
    Recibe dos valores como float y devuelve 1 si el primero es mayor al segundo,
    -1 si el primero es menor al segundo y 0 si son iguales
    """
    resultado = 0
    resta_ordenada = numero - otro_numero
    resta_inversa = otro_numero - numero
    if resta_ordenada > resta_inversa:
        resultado = 1
    elif resta_inversa > resta_ordenada:
        resultado = -1
    return resultado


def principal():
    """
    Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:
    Retornar -1 si el primero es menor que el segundo
    Retornar 0 si son iguales
    Retornar 1 si el primero es mayor que el segundo
    """
    valor_uno = float(input("Ingrese un valor: "))
    valor_dos = float(input("Ingrese otro valor a comparar: "))
    relacion = compara(valor_uno, valor_dos)
    if relacion == 1:
        print(f"{valor_uno} es mayor que {valor_dos}")
    elif relacion == -1:
        print(f"{valor_dos} es mayor que {valor_uno}")
    elif relacion == 0:
        print(f"{valor_uno} y {valor_dos} son iguales")

if __name__ == "__main__":
    principal()
