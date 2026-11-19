"""Ejercicio 274 — Matriz de Cofactores.

Enunciado:
    Desarrolla una función que calcule la matriz de cofactores de una matriz dada.

Solución:
    Cada cofactor C[i,j] es (-1)^(i+j) por el determinante de la
    submatriz obtenida al eliminar la fila i y la columna j.
    Se calcula el determinante mediante eliminación con pivoteo parcial.
    Para matrices 1×1 el cofactor es 1 (determinante de la matriz vacía).
"""
from collections.abc import Sequence
from math import isclose, isfinite

Numero = int | float
Matriz = Sequence[Sequence[Numero]]


def determinante(datos: list[list[float]]) -> float:
    """Calcular el determinante de una matriz cuadrada, incluida la vacía."""
    n = len(datos)
    if n == 0:
        return 1.0
    copia = [fila.copy() for fila in datos]
    signo = 1
    resultado = 1.0
    for columna in range(n):
        pivote = max(range(columna, n),
                     key=lambda i: abs(copia[i][columna]))
        if copia[pivote][columna] == 0:
            return 0.0
        if pivote != columna:
            copia[pivote], copia[columna] = copia[columna], copia[pivote]
            signo *= -1
        valor = copia[columna][columna]
        resultado *= valor
        for i in range(columna + 1, n):
            factor = copia[i][columna] / valor
            for j in range(columna + 1, n):
                copia[i][j] -= factor * copia[columna][j]
            copia[i][columna] = 0.0
    return signo * resultado


def matriz_cofactores(matriz: Matriz) -> list[list[float]]:
    """Calcular todos los cofactores sin modificar la matriz original."""
    n = len(matriz)
    if n == 0 or any(len(fila) != n for fila in matriz):
        raise ValueError("La matriz debe ser cuadrada y no vacía")
    datos = [[float(valor) for valor in fila] for fila in matriz]
    if not all(isfinite(valor) for fila in datos for valor in fila):
        raise ValueError("Los elementos deben ser finitos")

    return [
        [
            (-1 if (i + j) % 2 else 1) * determinante([
                [datos[fila][col] for col in range(n) if col != j]
                for fila in range(n) if fila != i
            ])
            for j in range(n)
        ]
        for i in range(n)
    ]


if __name__ == "__main__":
    assert matriz_cofactores([[7]]) == [[1.0]]
    assert matriz_cofactores([[1, 2], [3, 4]]) == [[4.0, -3.0], [-2.0, 1.0]]
    obtenido = matriz_cofactores([[1, 2, 3], [0, 4, 5], [1, 0, 6]])
    esperado = [[24, 5, -4], [-12, 3, 2], [-2, -5, 4]]
    assert all(isclose(a, b, abs_tol=1e-10)
               for fila_a, fila_b in zip(obtenido, esperado)
               for a, b in zip(fila_a, fila_b))
    original = [[1, 2], [3, 4]]
    matriz_cofactores(original)
    assert original == [[1, 2], [3, 4]]
    for invalida in ([], [[1, 2]], [[1, 2], [3]]):
        try:
            matriz_cofactores(invalida)
        except ValueError:
            pass
        else:
            raise AssertionError("La matriz debería rechazarse")
    print("Ejercicio 274: pruebas superadas")
