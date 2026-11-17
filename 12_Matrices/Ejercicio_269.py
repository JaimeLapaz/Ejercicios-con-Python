"""Ejercicio 269 — Producto de Matrices.

Enunciado:
    Implementa una función para multiplicar dos matrices y obtener
    el producto.

Solución:
    Comprobar que las matrices sean rectangulares y que el número de
    columnas de la primera coincida con las filas de la segunda.
    Calcular cada elemento mediante productos escalares.
    Complejidad O(filas_a × columnas_a × columnas_b).
"""
from collections.abc import Sequence

Numero = int | float
Matriz = Sequence[Sequence[Numero]]


def dimensiones(matriz: Matriz) -> tuple[int, int]:
    """Validar la forma rectangular de una matriz."""
    filas = len(matriz)
    columnas = len(matriz[0]) if filas else 0
    if any(len(fila) != columnas for fila in matriz):
        raise ValueError("La matriz debe ser rectangular")
    return filas, columnas


def multiplicar_matrices(a: Matriz, b: Matriz) -> list[list[Numero]]:
    """Calcular A × B sin modificar las matrices originales."""
    filas_a, columnas_a = dimensiones(a)
    filas_b, columnas_b = dimensiones(b)
    if columnas_a != filas_b:
        raise ValueError("Columnas de A y filas de B deben coincidir")
    return [
        [
            sum(a[i][k] * b[k][j] for k in range(columnas_a))
            for j in range(columnas_b)
        ]
        for i in range(filas_a)
    ]


if __name__ == "__main__":
    assert multiplicar_matrices(
        [[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]
    ) == [[58, 64], [139, 154]]
    assert multiplicar_matrices([[2, 3]], [[4], [5]]) == [[23]]
    assert multiplicar_matrices([[1, 2], [3, 4]], [[1, 0], [0, 1]]) == [
        [1, 2], [3, 4]
    ]
    assert multiplicar_matrices([], []) == []
    assert multiplicar_matrices([[], []], []) == [[], []]
    try:
        multiplicar_matrices([[1, 2]], [[3, 4]])
    except ValueError:
        pass
    else:
        raise AssertionError("Deben rechazarse dimensiones incompatibles")
    try:
        multiplicar_matrices([[1]], [[2], [3, 4]])
    except ValueError:
        pass
    else:
        raise AssertionError("Deben rechazarse matrices irregulares")
    print("Ejercicio 269: pruebas superadas")
