"""Ejercicio 277 — Descomposición QR.

Enunciado:
    Crea una función que realice la descomposición QR de una matriz.

Solución:
    Aplicar Gram-Schmidt modificado a las columnas de una matriz real
    de m filas y n columnas (m >= n) con rango completo. Devolver
    Q (m x n), de columnas ortonormales, y R (n x n) triangular
    superior, tales que A = QR. Rechazar matrices degeneradas.
"""
from collections.abc import Sequence
from math import isclose, isfinite, sqrt

Numero = int | float
Matriz = Sequence[Sequence[Numero]]


def descomposicion_qr(matriz: Matriz, tolerancia: float = 1e-12) -> tuple[list[list[float]], list[list[float]]]:
    """Calcular la QR reducida mediante Gram-Schmidt modificado.

    Requiere m >= n y columnas linealmente independientes. La tolerancia
    es relativa a la norma de cada columna original.
    """
    m = len(matriz)
    if m == 0:
        raise ValueError("La matriz no puede estar vacía")
    n = len(matriz[0])
    if n == 0 or m < n or any(len(fila) != n for fila in matriz):
        raise ValueError("Se requiere una matriz rectangular con m >= n > 0")
    if not isfinite(tolerancia) or tolerancia <= 0:
        raise ValueError("La tolerancia debe ser positiva y finita")

    a = [[float(valor) for valor in fila] for fila in matriz]
    if any(not isfinite(valor) for fila in a for valor in fila):
        raise ValueError("Los elementos deben ser finitos")

    columnas = [[a[i][j] for i in range(m)] for j in range(n)]
    normas = [sqrt(sum(valor * valor for valor in columna)) for columna in columnas]
    q_columnas: list[list[float]] = []
    r = [[0.0] * n for _ in range(n)]

    for j in range(n):
        vector = columnas[j][:]
        for i, q in enumerate(q_columnas):
            coeficiente = sum(x * y for x, y in zip(q, vector))
            r[i][j] = coeficiente
            vector = [x - coeficiente * y for x, y in zip(vector, q)]
        norma = sqrt(sum(x * x for x in vector))
        if not isfinite(norma) or norma <= tolerancia * normas[j]:
            raise ValueError("Las columnas deben ser linealmente independientes")
        r[j][j] = norma
        q_columnas.append([valor / norma for valor in vector])

    q_matriz = [[q_columnas[j][i] for j in range(n)] for i in range(m)]
    return q_matriz, r


def multiplicar(a: Matriz, b: Matriz) -> list[list[float]]:
    """Multiplicar matrices compatibles para comprobar la factorización."""
    if not a or not b or not b[0] or len(a[0]) != len(b):
        raise ValueError("Dimensiones incompatibles")
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


if __name__ == "__main__":
    for original in (
        [[5]],
        [[1, 0], [0, 1]],
        [[1, 1], [1, -1], [0, 1]],
        [[12, -51, 4], [6, 167, -68], [-4, 24, -41]],
    ):
        q, r = descomposicion_qr(original)
        producto = multiplicar(q, r)
        assert all(isclose(x, y, rel_tol=1e-9, abs_tol=1e-9)
                   for fila_x, fila_y in zip(producto, original)
                   for x, y in zip(fila_x, fila_y))
        n = len(r)
        assert all(isclose(r[i][j], 0, abs_tol=1e-10)
                   for i in range(n) for j in range(i))
        assert all(isclose(sum(q[k][i] * q[k][j] for k in range(len(q))),
                           float(i == j), abs_tol=1e-9)
                   for i in range(n) for j in range(n))

    for invalida in ([], [[]], [[1, 2]], [[1, 2], [2, 4]], [[float('nan')]]):
        try:
            descomposicion_qr(invalida)
        except ValueError:
            pass
        else:
            raise AssertionError("Entrada inválida no rechazada")
    print("Ejercicio 277: pruebas superadas")
