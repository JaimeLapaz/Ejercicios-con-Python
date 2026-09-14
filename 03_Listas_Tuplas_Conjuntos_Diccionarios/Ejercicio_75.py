"""
Enunciado:

75. Diseña un programa que elimine todas las claves con valores
pares de un diccionario.

Solución:
"""


def eliminar_valores_pares(diccionario: dict) -> dict:
    """
    Elimina las claves cuyos valores sean pares.

    Args:
        diccionario (dict): Diccionario con valores enteros.

    Returns:
        dict: Nuevo diccionario sin valores pares.
    """
    resultado = {}

    for clave, valor in diccionario.items():
        if valor % 2 != 0:
            resultado[clave] = valor

    return resultado


if __name__ == "__main__":
    numeros = {"a": 10, "b": 7, "c": 14, "d": 3, "e": 9}

    resultado = eliminar_valores_pares(numeros)

    print("Diccionario original:")
    print(numeros)

    print("\nSin valores pares:")
    print(resultado)
