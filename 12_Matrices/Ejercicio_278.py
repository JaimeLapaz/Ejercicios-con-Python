"""Ejercicio 278 — Eigenvalores y Eigenvectores.

Enunciado:
    Diseña un programa que calcule los eigenvalores y eigenvectores de una matriz.

Solución:
    Para matrices reales simétricas, aplicar rotaciones de Jacobi hasta
    diagonalizar la matriz. La diagonal contiene los eigenvalores y las
    columnas de la matriz ortogonal acumulada son eigenvectores unitarios.
    El método no necesita dependencias externas. Se rechazan matrices
    no simétricas, que requieren un algoritmo más general.
"""
from collections.abc import Sequence
from math import atan2, cos, isclose, isfinite, sin

Matriz = Sequence[Sequence[int | float]]


def eigenvalores_eigenvectores(
    matriz: Matriz, tolerancia: float = 1e-12, max_iteraciones: int | None = None
) -> tuple[list[float], list[list[float]]]:
    """Devolver eigenvalores ordenados y eigenvectores por columnas."""
    n = len(matriz)
    if n == 0 or any(len(fila) != n for fila in matriz):
        raise ValueError("Se requiere una matriz cuadrada no vacía")
    if not isfinite(tolerancia) or tolerancia <= 0:
        raise ValueError("La tolerancia debe ser positiva y finita")
    if max_iteraciones is None:
        max_iteraciones = 100 * n * n
    if isinstance(max_iteraciones, bool) or not isinstance(max_iteraciones, int) or max_iteraciones < 0:
        raise ValueError("El límite de iteraciones debe ser un entero no negativo")

    a = [[float(valor) for valor in fila] for fila in matriz]
    if any(not isfinite(x) for fila in a for x in fila):
        raise ValueError("Los elementos deben ser finitos")
    escala = max(abs(x) for fila in a for x in fila)
    if any(not isclose(a[i][j], a[j][i], rel_tol=tolerancia, abs_tol=tolerancia * escala)
           for i in range(n) for j in range(i + 1, n)):
        raise ValueError("El método de Jacobi requiere una matriz simétrica")
    for i in range(n):
        for j in range(i + 1, n):
            a[i][j] = a[j][i] = (a[i][j] + a[j][i]) / 2
    v = [[float(i == j) for j in range(n)] for i in range(n)]
    umbral = tolerancia * escala

    for iteracion in range(max_iteraciones + 1):
        p, q = 0, 0
        mayor = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > mayor:
                    mayor, p, q = abs(a[i][j]), i, j
        if mayor <= umbral:
            break
        if iteracion == max_iteraciones:
            raise ValueError("No se alcanzó la convergencia")
        angulo = 0.5 * atan2(2 * a[p][q], a[q][q] - a[p][p])
        c, s = cos(angulo), sin(angulo)
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        a[p][p] = c * c * app - 2 * c * s * apq + s * s * aqq
        a[q][q] = s * s * app + 2 * c * s * apq + c * c * aqq
        a[p][q] = a[q][p] = 0.0
        for k in range(n):
            if k != p and k != q:
                akp, akq = a[k][p], a[k][q]
                a[k][p] = a[p][k] = c * akp - s * akq
                a[k][q] = a[q][k] = s * akp + c * akq
            vkp, vkq = v[k][p], v[k][q]
            v[k][p], v[k][q] = c * vkp - s * vkq, s * vkp + c * vkq

    orden = sorted(range(n), key=lambda i: a[i][i])
    return [a[i][i] for i in orden], [[v[fila][i] for i in orden] for fila in range(n)]


if __name__ == '__main__':
    ejemplos = (
        [[7]],
        [[2, 1], [1, 2]],
        [[4, 0, 0], [0, 1, 0], [0, 0, 3]],
        [[4, 1, 2], [1, 3, 0], [2, 0, 2]],
        [[0, 0], [0, 0]],
    )
    for original in ejemplos:
        valores, vectores = eigenvalores_eigenvectores(original)
        n = len(original)
        for j in range(n):
            for i in range(n):
                lhs = sum(original[i][k] * vectores[k][j] for k in range(n))
                rhs = valores[j] * vectores[i][j]
                assert isclose(lhs, rhs, rel_tol=1e-9, abs_tol=1e-9)
            assert isclose(sum(vectores[i][j] ** 2 for i in range(n)), 1, abs_tol=1e-9)
        for j in range(n):
            for k in range(j + 1, n):
                assert isclose(sum(vectores[i][j] * vectores[i][k] for i in range(n)), 0, abs_tol=1e-9)
    assert eigenvalores_eigenvectores([[2, 1], [1, 2]])[0] == [1.0, 3.0]
    for invalida in ([], [[1, 2]], [[1, 2], [3, 4]], [[float('nan')]]):
        try:
            eigenvalores_eigenvectores(invalida)
        except ValueError:
            pass
        else:
            raise AssertionError('Entrada inválida no rechazada')
    try:
        eigenvalores_eigenvectores([[2, 1], [1, 2]], max_iteraciones=0)
    except ValueError:
        pass
    else:
        raise AssertionError('No se detectó la falta de convergencia')
    print('Ejercicio 278: pruebas superadas')
