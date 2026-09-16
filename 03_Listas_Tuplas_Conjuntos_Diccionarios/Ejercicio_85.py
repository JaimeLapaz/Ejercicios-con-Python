"""
Enunciado:

85. Diseña un programa que encuentre todos los elementos únicos
en una lista y los almacene en un conjunto.

Solución:
"""


def obtener_elementos_unicos(elementos: list) -> set:
    """
    Obtiene los elementos únicos de una lista.

    Args:
        elementos (list): Lista que puede contener duplicados.

    Returns:
        set: Conjunto sin elementos repetidos.
    """
    unicos = set()

    for elemento in elementos:
        unicos.add(elemento)

    return unicos


if __name__ == "__main__":
    numeros = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]

    resultado = obtener_elementos_unicos(numeros)

    print("Lista original:")
    print(numeros)

    print("\nElementos únicos:")
    print(resultado)
