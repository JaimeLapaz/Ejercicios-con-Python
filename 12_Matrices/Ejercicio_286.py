"""Ejercicio 286 — Interpolación de Matrices.

Enunciado:
    Diseña una función que realice interpolación de matrices para
    estimar valores faltantes en una matriz.

Solución:
    Representar los valores faltantes con None y estimarlos mediante
    ponderación por el inverso de la distancia euclídea al cuadrado.
    Solo se utilizan observaciones originales, evitando que el orden
    de recorrido influya en las estimaciones. Se supone una cuadrícula
    regular con igual separación entre filas y columnas.
"""
from collections.abc import Sequence
from math import fsum, isfinite, isclose

Matriz = Sequence[Sequence[float | None]]


def interpolar_matriz(matriz: Matriz) -> list[list[float]]:
    """Rellena los huecos mediante IDW sin modificar la matriz original.

    Los valores conocidos se conservan. En los bordes también se
    estiman valores, aunque allí pueden constituir extrapolaciones.
    El coste temporal es O(F*C + K*H), con K datos conocidos y H huecos.
    """
    if not matriz or not matriz[0]:
        raise ValueError("La matriz no puede estar vacía")
    columnas = len(matriz[0])
    if any(len(fila) != columnas for fila in matriz):
        raise ValueError("La matriz debe ser rectangular")

    conocidos: list[tuple[int, int, float]] = []
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor is not None:
                numero = float(valor)
                if not isfinite(numero):
                    raise ValueError("Los valores conocidos deben ser finitos")
                conocidos.append((i, j, numero))
    if not conocidos:
        raise ValueError("Se necesita al menos un valor conocido")

    resultado: list[list[float]] = []
    for i, fila in enumerate(matriz):
        nueva: list[float] = []
        for j, valor in enumerate(fila):
            if valor is not None:
                nueva.append(float(valor))
                continue
            # La distancia nunca es cero: esta posición es un hueco.
            pesos = [1.0 / ((i - f)**2 + (j - c)**2)
                     for f, c, _ in conocidos]
            total = fsum(pesos)
            estimacion = fsum((peso / total) * dato
                              for peso, (_, _, dato) in zip(pesos, conocidos))
            nueva.append(estimacion)
        resultado.append(nueva)
    return resultado


if __name__ == '__main__':
    matriz = [[0, 2, 4], [2, None, 6], [4, 6, 8]]
    resultado = interpolar_matriz(matriz)
    assert isclose(resultado[1][1], 4.0)
    assert matriz[1][1] is None
    assert interpolar_matriz([[0, None, 10]]) == [[0.0, 5.0, 10.0]]
    assert interpolar_matriz([[7, None], [None, None]]) == [[7.0, 7.0], [7.0, 7.0]]
    assert interpolar_matriz([[1, 2]]) == [[1.0, 2.0]]
    # Distancias diferentes: pesos 1 y 1/4.
    assert isclose(interpolar_matriz([[0, None, None, 10]])[0][1], 2.0)
    # Varios huecos: las estimaciones no se reutilizan.
    assert isclose(interpolar_matriz([[0, None, None, 10]])[0][2], 8.0)
    for invalida in ([], [[]], [[None]], [[1], [2, 3]], [[float('nan')]]):
        try:
            interpolar_matriz(invalida)
        except ValueError:
            pass
        else:
            raise AssertionError("Entrada inválida no rechazada")
    print("Matriz interpolada:")
    for fila in resultado:
        print(fila)
    print("Ejercicio 286: pruebas superadas")
