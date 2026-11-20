"""Ejercicio 275 — Ecuaciones Lineales.

Enunciado:
    Diseña una función que resuelva un sistema de ecuaciones lineales
    utilizando matrices y la regla de Cramer.

Solución:
    Para A·x = b, sustituir cada columna de A por b y calcular
    x_j = det(A_j) / det(A). La eliminación gaussiana con pivoteo
    parcial calcula cada determinante sin modificar las entradas.
    La regla de Cramer requiere una matriz cuadrada no singular.
"""
from collections.abc import Sequence
from math import isclose, isfinite

Numero = int | float
Matriz = Sequence[Sequence[Numero]]


def determinante(matriz: list[list[float]]) -> float:
    """Calcular un determinante por eliminación y pivoteo parcial."""
    n = len(matriz)
    datos = [fila.copy() for fila in matriz]
    resultado = 1.0
    for columna in range(n):
        pivote = max(range(columna, n), key=lambda i: abs(datos[i][columna]))
        if datos[pivote][columna] == 0:
            return 0.0
        if pivote != columna:
            datos[columna], datos[pivote] = datos[pivote], datos[columna]
            resultado = -resultado
        valor = datos[columna][columna]
        resultado *= valor
        for i in range(columna + 1, n):
            factor = datos[i][columna] / valor
            for j in range(columna + 1, n):
                datos[i][j] -= factor * datos[columna][j]
            datos[i][columna] = 0.0
    return resultado


def resolver_cramer(matriz: Matriz, terminos: Sequence[Numero]) -> list[float]:
    """Resolver A·x=b mediante la regla de Cramer."""
    n = len(matriz)
    if n == 0 or len(terminos) != n or any(len(fila) != n for fila in matriz):
        raise ValueError("Se requiere una matriz cuadrada no vacía y n términos")
    datos = [[float(valor) for valor in fila] for fila in matriz]
    b = [float(valor) for valor in terminos]
    if not all(isfinite(x) for fila in datos for x in fila) or not all(
        isfinite(x) for x in b
    ):
        raise ValueError("Los coeficientes y términos deben ser finitos")
    det = determinante(datos)
    if det == 0:
        raise ValueError("El sistema no tiene solución única")
    soluciones = []
    for columna in range(n):
        sustituida = [
            [b[i] if j == columna else datos[i][j] for j in range(n)]
            for i in range(n)
        ]
        soluciones.append(determinante(sustituida) / det)
    return soluciones


if __name__ == "__main__":
    assert resolver_cramer([[2]], [8]) == [4.0]
    resultado = resolver_cramer([[2, 1], [1, -1]], [5, 1])
    assert all(isclose(a, b, abs_tol=1e-10) for a, b in zip(resultado, [2, 1]))
    resultado = resolver_cramer([[0, 1], [2, 3]], [4, 14])
    assert all(isclose(a, b, abs_tol=1e-10) for a, b in zip(resultado, [1, 4]))
    for matriz, b in (([], []), ([[1, 2]], [3]), ([[1, 2], [2, 4]], [3, 6])):
        try:
            resolver_cramer(matriz, b)
        except ValueError:
            pass
        else:
            raise AssertionError("Entrada inválida no rechazada")
    print("Ejercicio 275: pruebas superadas")
