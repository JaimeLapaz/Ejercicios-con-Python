"""
Enunciado:

86. Crea una función que calcule la unión de múltiples conjuntos.

Solución:
"""


def unir_conjuntos(conjuntos: list) -> set:
    """
    Calcula la unión de múltiples conjuntos.

    Args:
        conjuntos (list): Lista que contiene conjuntos.

    Returns:
        set: Conjunto con todos los elementos sin duplicados.
    """
    resultado = set()

    for conjunto in conjuntos:
        for elemento in conjunto:
            resultado.add(elemento)

    return resultado


if __name__ == "__main__":
    conjuntos = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}, {7, 8, 9}]

    resultado = unir_conjuntos(conjuntos)

    print("Unión:", resultado)
