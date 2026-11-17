"""Ejercicio 268 — Suma de Matrices.

Enunciado:
    Escribe una función que sume dos matrices y devuelva el resultado.

Solución:
    Validar que ambas matrices sean rectangulares y tengan las mismas
    dimensiones. Sumar sus elementos posición a posición sin alterar
    las entradas. Complejidad O(filas × columnas).
"""
from collections.abc import Sequence

Numero = int | float
Matriz = Sequence[Sequence[Numero]]


def dimensiones(matriz: Matriz) -> tuple[int, int]:
    """Devolver (filas, columnas) y rechazar filas de distinta longitud."""
    filas = len(matriz)
    columnas = len(matriz[0]) if filas else 0
    if any(len(fila) != columnas for fila in matriz):
        raise ValueError("La matriz debe ser rectangular")
    return filas, columnas


def sumar_matrices(a: Matriz, b: Matriz) -> list[list[Numero]]:
    """Sumar dos matrices de idénticas dimensiones."""
    if dimensiones(a) != dimensiones(b):
        raise ValueError("Las matrices deben tener las mismas dimensiones")
    return [
        [valor_a + valor_b for valor_a, valor_b in zip(fila_a, fila_b)]
        for fila_a, fila_b in zip(a, b)
    ]


if __name__ == "__main__":
    assert sumar_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [
        [6, 8], [10, 12]
    ]
    assert sumar_matrices([], []) == []
    assert sumar_matrices([[], []], [[], []]) == [[], []]
    assert sumar_matrices([[1.5]], [[2]]) == [[3.5]]
    try:
        sumar_matrices([[1, 2]], [[1]])
    except ValueError:
        pass
    else:
        raise AssertionError("Deben rechazarse dimensiones incompatibles")
    try:
        sumar_matrices([[1], [2, 3]], [[4], [5]])
    except ValueError:
        pass
    else:
        raise AssertionError("Deben rechazarse matrices irregulares")
    print("Ejercicio 268: pruebas superadas")
