"""Ejercicio 272 — Determinante de una Matriz.

Enunciado:
    Crea una función que calcule el determinante de una matriz cuadrada.

Solución:
    Validar que la matriz sea cuadrada y calcular su determinante
    mediante eliminación gaussiana con pivoteo parcial. Cada
    intercambio de filas cambia el signo del determinante.
    Una columna sin pivote indica determinante cero.
    Complejidad temporal O(n³) y espacial O(n²).
"""
from collections.abc import Sequence

Numero = int | float
Matriz = Sequence[Sequence[Numero]]


def determinante(matriz: Matriz, tolerancia: float = 1e-12) -> float:
    """Calcular el determinante sin modificar la matriz original.

    Se rechazan matrices vacías, irregulares o no cuadradas.
    La tolerancia solo se usa para decidir si un pivote es cero
    numéricamente; puede ajustarse a la escala de los datos.
    """
    orden = len(matriz)
    if orden == 0 or any(len(fila) != orden for fila in matriz):
        raise ValueError("La matriz debe ser cuadrada y no vacía")
    if tolerancia < 0:
        raise ValueError("La tolerancia no puede ser negativa")

    datos = [[float(valor) for valor in fila] for fila in matriz]
    signo = 1
    producto = 1.0

    for columna in range(orden):
        pivote = max(range(columna, orden),
                     key=lambda fila: abs(datos[fila][columna]))
        if abs(datos[pivote][columna]) <= tolerancia:
            return 0.0

        if pivote != columna:
            datos[columna], datos[pivote] = datos[pivote], datos[columna]
            signo *= -1

        valor_pivote = datos[columna][columna]
        producto *= valor_pivote
        for fila in range(columna + 1, orden):
            factor = datos[fila][columna] / valor_pivote
            datos[fila][columna] = 0.0
            for j in range(columna + 1, orden):
                datos[fila][j] -= factor * datos[columna][j]

    return signo * producto


if __name__ == "__main__":
    from math import isclose

    assert isclose(determinante([[7]]), 7)
    assert isclose(determinante([[1, 2], [3, 4]]), -2)
    assert isclose(determinante([[0, 1], [1, 0]]), -1)
    assert isclose(determinante([[1, 2], [2, 4]]), 0)
    assert isclose(determinante([[2, 0, 0], [0, 3, 0], [0, 0, 4]]), 24)
    assert isclose(determinante([[6, 1, 1], [4, -2, 5], [2, 8, 7]]), -306)
    original = [[1, 2], [3, 4]]
    determinante(original)
    assert original == [[1, 2], [3, 4]]

    for invalida in ([], [[1, 2]], [[1, 2], [3]]):
        try:
            determinante(invalida)
        except ValueError:
            pass
        else:
            raise AssertionError("Deben rechazarse matrices no cuadradas")
    print("Ejercicio 272: pruebas superadas")
