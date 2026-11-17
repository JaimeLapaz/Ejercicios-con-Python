"""Ejercicio 270 — Matriz Traspuesta.

Enunciado:
    Desarrolla una función que calcule la matriz traspuesta de una
    matriz dada.

Solución:
    Validar que la matriz sea rectangular y construir otra matriz
    intercambiando filas y columnas, sin modificar la original.
    Complejidad O(filas × columnas).
"""
from collections.abc import Sequence

Numero = int | float
Matriz = Sequence[Sequence[Numero]]


def trasponer_matriz(matriz: Matriz) -> list[list[Numero]]:
    """Devolver la traspuesta de una matriz rectangular."""
    if not matriz:
        return []
    columnas = len(matriz[0])
    if any(len(fila) != columnas for fila in matriz):
        raise ValueError("La matriz debe ser rectangular")
    return [
        [matriz[fila][columna] for fila in range(len(matriz))]
        for columna in range(columnas)
    ]


if __name__ == "__main__":
    original = [[1, 2, 3], [4, 5, 6]]
    assert trasponer_matriz(original) == [[1, 4], [2, 5], [3, 6]]
    assert original == [[1, 2, 3], [4, 5, 6]]
    assert trasponer_matriz([[7]]) == [[7]]
    assert trasponer_matriz([[1], [2], [3]]) == [[1, 2, 3]]
    assert trasponer_matriz([]) == []
    assert trasponer_matriz([[], []]) == []
    assert trasponer_matriz(trasponer_matriz(original)) == original
    try:
        trasponer_matriz([[1, 2], [3]])
    except ValueError:
        pass
    else:
        raise AssertionError("Deben rechazarse matrices irregulares")
    print("Ejercicio 270: pruebas superadas")
