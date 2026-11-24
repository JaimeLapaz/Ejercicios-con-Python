"""Ejercicio 282 — Factorización de Cholesky.

Enunciado:
    Implementa un algoritmo para la factorización de Cholesky de una
    matriz simétrica definida positiva.

Solución:
    Construir una matriz triangular inferior L tal que A = L L^T.
    Cada elemento se obtiene restando los productos ya calculados.
    Los pivotes diagonales deben ser estrictamente positivos.
"""
from collections.abc import Sequence
from math import fsum, isclose, isfinite, sqrt

Matriz = Sequence[Sequence[int | float]]


def factorizacion_cholesky(matriz: Matriz) -> list[list[float]]:
    """Devolver L sin modificar A; rechazar matrices no admisibles."""
    n = len(matriz)
    if n == 0 or any(len(fila) != n for fila in matriz):
        raise ValueError("Se requiere una matriz cuadrada no vacía")
    if any(isinstance(x, bool) or not isinstance(x, (int, float))
           or not isfinite(x) for fila in matriz for x in fila):
        raise ValueError("Los elementos deben ser números reales finitos")
    if any(matriz[i][j] != matriz[j][i]
           for i in range(n) for j in range(i)):
        raise ValueError("La matriz debe ser simétrica")

    inferior = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            producto = fsum(inferior[i][k] * inferior[j][k] for k in range(j))
            resto = matriz[i][j] - producto
            if i == j:
                if resto <= 0 or not isfinite(resto):
                    raise ValueError("La matriz no es definida positiva")
                inferior[i][j] = sqrt(resto)
            else:
                inferior[i][j] = resto / inferior[j][j]
    return inferior


if __name__ == '__main__':
    a = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]
    l = factorizacion_cholesky(a)
    assert l == [[2, 0, 0], [6, 1, 0], [-8, 5, 3]]
    assert factorizacion_cholesky([[9]]) == [[3.0]]
    for matriz in (a, [[2, 1], [1, 2]], [[1e-20, 0], [0, 2e-20]]):
        l = factorizacion_cholesky(matriz)
        n = len(matriz)
        for i in range(n):
            assert l[i][i] > 0
            for j in range(n):
                if j > i:
                    assert l[i][j] == 0
                reconstruido = fsum(l[i][k] * l[j][k] for k in range(n))
                assert isclose(reconstruido, matriz[i][j], rel_tol=1e-12,
                               abs_tol=0.0)
    assert a == [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]
    for invalida in ([], [[1, 2]], [[1, 2], [0, 1]],
                     [[1, 1], [1, 1]], [[1, 2], [2, 1]], [[-1]],
                     [[float('inf')]]):
        try:
            factorizacion_cholesky(invalida)
        except ValueError:
            pass
        else:
            raise AssertionError("Se aceptó una matriz inválida")
    print("Ejercicio 282: pruebas superadas")
