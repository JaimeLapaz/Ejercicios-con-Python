"""Ejercicio 271 — Identificar Matriz Diagonal.

Enunciado:
    Diseña una función que determine si una matriz cuadrada es diagonal o no.

Solución:
    Comprobar que la matriz sea cuadrada y que todos los elementos
    fuera de la diagonal principal sean cero. Los valores de la
    diagonal pueden ser cualesquiera, incluido cero.
    Complejidad temporal O(n²) y espacial O(1).
"""
from collections.abc import Sequence

Numero = int | float
Matriz = Sequence[Sequence[Numero]]


def es_matriz_diagonal(matriz: Matriz) -> bool:
    """Indicar si una matriz cuadrada es diagonal.

    Una matriz vacía no se considera cuadrada en este ejercicio.
    Las matrices irregulares o no cuadradas devuelven False.
    """
    orden = len(matriz)
    if orden == 0 or any(len(fila) != orden for fila in matriz):
        return False

    return all(
        valor == 0
        for i, fila in enumerate(matriz)
        for j, valor in enumerate(fila)
        if i != j
    )


if __name__ == "__main__":
    assert es_matriz_diagonal([[3, 0], [0, -2]])
    assert es_matriz_diagonal([[0]])
    assert es_matriz_diagonal([[0, 0], [0, 0]])
    assert es_matriz_diagonal([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
    assert not es_matriz_diagonal([[1, 2], [0, 3]])
    assert not es_matriz_diagonal([[1, 0, 0], [0, 2, 0]])
    assert not es_matriz_diagonal([[1, 0], [0]])
    assert not es_matriz_diagonal([])
    print("Ejercicio 271: pruebas superadas")
