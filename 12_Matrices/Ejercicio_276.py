"""Ejercicio 276 — Factorización LU.

Enunciado:
    Implementa un algoritmo para la factorización LU de una matriz.

Solución:
    Aplicar eliminación gaussiana con pivoteo parcial (PA = LU).
    L es triangular inferior con diagonal unitaria, U triangular
    superior y P registra los intercambios de filas. El pivoteo
    permite factorizar matrices que requieren permutar filas.
"""
from collections.abc import Sequence
from math import isclose, isfinite

Numero = int | float
Matriz = Sequence[Sequence[Numero]]


def factorizacion_lu(
    matriz: Matriz,
) -> tuple[list[list[float]], list[list[float]], list[list[float]]]:
    """Devolver (P, L, U) tales que P·A = L·U sin modificar A."""
    n = len(matriz)
    if n == 0 or any(len(fila) != n for fila in matriz):
        raise ValueError("La matriz debe ser cuadrada y no vacía")
    u = [[float(x) for x in fila] for fila in matriz]
    if not all(isfinite(x) for fila in u for x in fila):
        raise ValueError("Los elementos deben ser finitos")
    p = [[float(i == j) for j in range(n)] for i in range(n)]
    l = [[float(i == j) for j in range(n)] for i in range(n)]

    for k in range(n):
        pivote = max(range(k, n), key=lambda i: abs(u[i][k]))
        if u[pivote][k] == 0:
            raise ValueError("La matriz es singular; no admite esta LU")
        if pivote != k:
            u[k], u[pivote] = u[pivote], u[k]
            p[k], p[pivote] = p[pivote], p[k]
            for j in range(k):
                l[k][j], l[pivote][j] = l[pivote][j], l[k][j]
        for i in range(k + 1, n):
            factor = u[i][k] / u[k][k]
            l[i][k] = factor
            u[i][k] = 0.0
            for j in range(k + 1, n):
                u[i][j] -= factor * u[k][j]
    return p, l, u


def multiplicar(a: Matriz, b: Matriz) -> list[list[float]]:
    """Multiplicar dos matrices compatibles para verificar PA = LU."""
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b)))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


if __name__ == "__main__":
    for original in (
        [[5]],
        [[4, 3], [6, 3]],
        [[0, 2], [3, 4]],
        [[2, 1, 1], [4, -6, 0], [-2, 7, 2]],
    ):
        p, l, u = factorizacion_lu(original)
        pa, lu = multiplicar(p, original), multiplicar(l, u)
        assert all(isclose(x, y, abs_tol=1e-10)
                   for fila_x, fila_y in zip(pa, lu)
                   for x, y in zip(fila_x, fila_y))
        assert all(isclose(l[i][i], 1) for i in range(len(l)))
        assert all(isclose(l[i][j], 0) for i in range(len(l)) for j in range(i + 1, len(l)))
        assert all(isclose(u[i][j], 0) for i in range(len(u)) for j in range(i))
    for invalida in ([], [[1, 2]], [[1, 2], [2, 4]]):
        try:
            factorizacion_lu(invalida)
        except ValueError:
            pass
        else:
            raise AssertionError("Entrada inválida no rechazada")
    print("Ejercicio 276: pruebas superadas")
