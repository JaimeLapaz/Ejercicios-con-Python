"""
Enunciado:

79. Implementa una función que encuentre la tupla con la mayor
suma de elementos en una lista de tuplas.

Solución:
"""


def tupla_mayor_suma(tuplas: list):
    """
    Encuentra la tupla cuya suma de elementos es mayor.

    Args:
        tuplas (list): Lista de tuplas numéricas.

    Returns:
        tuple | None: Tupla con la mayor suma o None si la lista
        está vacía.
    """
    if not tuplas:
        return None

    mayor = tuplas[0]

    for tupla in tuplas[1:]:
        if sum(tupla) > sum(mayor):
            mayor = tupla

    return mayor


if __name__ == "__main__":
    numeros = [(1, 2, 3), (10, 5), (4, 4, 4), (7, 8, 2)]

    resultado = tupla_mayor_suma(numeros)

    print("Tupla con mayor suma:", resultado)

    if resultado is not None:
        print("Suma:", sum(resultado))
