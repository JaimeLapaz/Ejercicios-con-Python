"""Ejercicio 281 — Matriz de Covarianza.

Enunciado:
    Diseña un programa que calcule la matriz de covarianza a partir
    de un conjunto de datos.

Solución:
    Cada fila representa una observación y cada columna una variable.
    Se centran las columnas y se calculan sus productos cruzados.
    La covarianza muestral divide por n - 1 y la poblacional por n.
"""
from collections.abc import Sequence
from math import fsum, isfinite

Matriz = Sequence[Sequence[int | float]]


def matriz_covarianza(datos: Matriz, muestral: bool = True) -> list[list[float]]:
    """Calcular las covarianzas entre todas las parejas de variables."""
    n = len(datos)
    if n == 0 or len(datos[0]) == 0:
        raise ValueError("Se requieren observaciones y variables")
    p = len(datos[0])
    if any(len(fila) != p for fila in datos):
        raise ValueError("Todas las observaciones deben tener igual longitud")
    if any(isinstance(x, bool) or not isinstance(x, (int, float))
           or not isfinite(x) for fila in datos for x in fila):
        raise ValueError("Los datos deben ser números reales finitos")
    divisor = n - 1 if muestral else n
    if divisor == 0:
        raise ValueError("La covarianza muestral requiere dos observaciones")

    medias = [fsum(fila[j] / n for fila in datos) for j in range(p)]
    centradas = [[fila[j] - medias[j] for j in range(p)] for fila in datos]
    resultado = [[0.0] * p for _ in range(p)]
    # La matriz es simétrica: basta calcular un triángulo.
    for i in range(p):
        for j in range(i, p):
            cov = fsum(fila[i] * fila[j] / divisor for fila in centradas)
            resultado[i][j] = resultado[j][i] = cov
    return resultado


if __name__ == '__main__':
    from math import isclose

    datos = [[1, 2, 7], [2, 4, 7], [3, 6, 7]]
    esperado = [[1, 2, 0], [2, 4, 0], [0, 0, 0]]
    assert matriz_covarianza(datos) == esperado
    poblacional = matriz_covarianza(datos, muestral=False)
    for i in range(3):
        for j in range(3):
            assert isclose(poblacional[i][j], esperado[i][j] * 2 / 3)
    assert matriz_covarianza([[1, 3], [2, 2], [3, 1]]) == [[1, -1], [-1, 1]]
    assert matriz_covarianza([[5]], muestral=False) == [[0.0]]
    assert datos == [[1, 2, 7], [2, 4, 7], [3, 6, 7]]

    for invalidos in ([], [[]], [[1]], [[1], [2, 3]], [[1], [float('nan')]]):
        try:
            matriz_covarianza(invalidos)
        except ValueError:
            pass
        else:
            raise AssertionError("Se aceptaron datos inválidos")
    print("Ejercicio 281: pruebas superadas")
