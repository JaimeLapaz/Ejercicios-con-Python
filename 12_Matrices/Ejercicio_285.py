"""Ejercicio 285 — Reducción de Dimensión.

Enunciado:
    Desarrolla un algoritmo de reducción de dimensión como Análisis de
    Componentes Principales (PCA) utilizando matrices.

Solución:
    Centrar las observaciones, calcular su matriz de covarianza muestral
    y diagonalizarla mediante el método de Jacobi del ejercicio 278.
    Seleccionar los eigenvectores de mayor eigenvalor y proyectar los
    datos centrados sobre ellos. No se estandarizan las variables:
    las de mayor varianza tienen más influencia.
"""
from collections.abc import Sequence
from math import isfinite, isclose
from Ejercicio_278 import eigenvalores_eigenvectores

Matriz = Sequence[Sequence[float]]


def pca(datos: Matriz, n_componentes: int) -> tuple[
    list[list[float]], list[list[float]], list[float], list[float]
]:
    """Devuelve proyección, componentes (por filas), medias y varianza explicada.

    Cada fila de datos es una observación y cada columna una variable.
    La varianza explicada se expresa como fracción de la varianza total.
    """
    n = len(datos)
    if n < 2 or not datos[0]:
        raise ValueError("Se requieren al menos dos observaciones y una variable")
    m = len(datos[0])
    if any(len(fila) != m for fila in datos):
        raise ValueError("La matriz debe ser rectangular")
    if (isinstance(n_componentes, bool) or not isinstance(n_componentes, int)
            or not 1 <= n_componentes <= m):
        raise ValueError("Número de componentes fuera de rango")
    x = [[float(v) for v in fila] for fila in datos]
    if any(not isfinite(v) for fila in x for v in fila):
        raise ValueError("Los datos deben ser finitos")

    medias = [sum(columna) / n for columna in zip(*x)]
    centrados = [[v - media for v, media in zip(fila, medias)] for fila in x]
    covarianza = [[0.0] * m for _ in range(m)]
    for i in range(m):
        for j in range(i, m):
            valor = sum(fila[i] * fila[j] for fila in centrados) / (n - 1)
            covarianza[i][j] = covarianza[j][i] = valor

    valores, vectores = eigenvalores_eigenvectores(covarianza)
    orden = sorted(range(m), key=lambda i: valores[i], reverse=True)
    seleccion = orden[:n_componentes]
    componentes = [[vectores[j][i] for j in range(m)] for i in seleccion]
    # Los pequeños eigenvalores negativos por redondeo se tratan como cero.
    varianzas = [max(0.0, valor) for valor in valores]
    total = sum(varianzas)
    explicada = [varianzas[i] / total if total else 0.0 for i in seleccion]
    proyeccion = [
        [sum(a * b for a, b in zip(fila, componente))
         for componente in componentes]
        for fila in centrados
    ]
    return proyeccion, componentes, medias, explicada


def reconstruir(
    proyeccion: Matriz, componentes: Matriz, medias: Sequence[float]
) -> list[list[float]]:
    """Reconstruye aproximadamente los datos a partir de su proyección PCA."""
    if not componentes or any(len(c) != len(medias) for c in componentes):
        raise ValueError("Dimensiones incompatibles de componentes y medias")
    if any(len(fila) != len(componentes) for fila in proyeccion):
        raise ValueError("Dimensiones incompatibles de la proyección")
    return [
        [media + sum(fila[k] * componentes[k][j] for k in range(len(fila)))
         for j, media in enumerate(medias)]
        for fila in proyeccion
    ]


if __name__ == '__main__':
    datos = [[1, 2], [2, 4], [3, 6], [4, 8]]
    z, c, medias, explicada = pca(datos, 1)
    assert medias == [2.5, 5.0]
    assert isclose(explicada[0], 1.0)
    assert isclose(sum(fila[0] for fila in z), 0.0, abs_tol=1e-9)
    assert isclose(sum(v * v for v in c[0]), 1.0)
    for original, recuperada in zip(datos, reconstruir(z, c, medias)):
        assert all(isclose(a, b, abs_tol=1e-9)
                   for a, b in zip(original, recuperada))

    # Dos variables independientes con varianzas diferentes.
    datos2 = [[-2, -1], [-2, 1], [2, -1], [2, 1]]
    z, c, medias, explicada = pca(datos2, 2)
    assert isclose(explicada[0], 0.8)
    assert isclose(explicada[1], 0.2)
    assert isclose(sum(a * b for a, b in zip(*c)), 0.0, abs_tol=1e-9)
    for original, recuperada in zip(datos2, reconstruir(z, c, medias)):
        assert all(isclose(a, b, abs_tol=1e-9)
                   for a, b in zip(original, recuperada))
    assert pca([[3, 3], [3, 3]], 1)[3] == [0.0]
    assert pca([[1], [2]], 1)[3] == [1.0]
    for invalida, k in [([], 1), ([[1], [2, 3]], 1),
                        ([[1], [2]], 2), ([[1], [float('nan')]], 1)]:
        try:
            pca(invalida, k)
        except ValueError:
            pass
        else:
            raise AssertionError("Entrada inválida no rechazada")
    print("Proyección PCA:", pca(datos, 1)[0])
    print("Ejercicio 285: pruebas superadas")
