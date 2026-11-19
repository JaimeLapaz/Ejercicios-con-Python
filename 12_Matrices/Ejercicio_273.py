"""Ejercicio 273 — Inversa de una Matriz.

Enunciado:
    Implementa un algoritmo para calcular la matriz inversa de una matriz cuadrada.

Solución:
    Aplicar Gauss-Jordan con pivoteo parcial a la matriz aumentada [A | I].
    Al reducir A a la identidad, el bloque derecho es A⁻¹.
    Se rechazan matrices no cuadradas o singulares. O(n³) tiempo y O(n²) espacio.
"""
from collections.abc import Sequence
from math import isclose, isfinite

Numero = int | float
Matriz = Sequence[Sequence[Numero]]


def inversa(matriz: Matriz, tolerancia: float = 1e-12) -> list[list[float]]:
    """Devolver una nueva matriz inversa sin alterar la entrada.

    La tolerancia es relativa a la escala máxima de cada columna activa.
    """
    n = len(matriz)
    if n == 0 or any(len(fila) != n for fila in matriz):
        raise ValueError("La matriz debe ser cuadrada y no vacía")
    if not isfinite(tolerancia) or tolerancia < 0:
        raise ValueError("La tolerancia debe ser finita y no negativa")

    aumentada = []
    for i, fila in enumerate(matriz):
        valores = [float(valor) for valor in fila]
        if not all(isfinite(valor) for valor in valores):
            raise ValueError("Los elementos deben ser finitos")
        aumentada.append(valores + [float(i == j) for j in range(n)])

    for columna in range(n):
        pivote = max(range(columna, n),
                     key=lambda i: abs(aumentada[i][columna]))
        escala = max(abs(aumentada[i][columna]) for i in range(n))
        if escala == 0 or abs(aumentada[pivote][columna]) <= tolerancia * escala:
            raise ValueError("La matriz es singular")
        aumentada[columna], aumentada[pivote] = (
            aumentada[pivote], aumentada[columna]
        )
        divisor = aumentada[columna][columna]
        aumentada[columna] = [valor / divisor for valor in aumentada[columna]]

        for i in range(n):
            if i == columna:
                continue
            factor = aumentada[i][columna]
            aumentada[i] = [
                actual - factor * referencia
                for actual, referencia in zip(aumentada[i], aumentada[columna])
            ]

    return [fila[n:] for fila in aumentada]


if __name__ == "__main__":
    assert inversa([[5]]) == [[0.2]]
    resultado = inversa([[4, 7], [2, 6]])
    esperado = [[0.6, -0.7], [-0.2, 0.4]]
    assert all(isclose(a, b, abs_tol=1e-12)
               for fila_a, fila_b in zip(resultado, esperado)
               for a, b in zip(fila_a, fila_b))
    assert inversa([[0, 1], [1, 0]]) == [[0.0, 1.0], [1.0, 0.0]]
    original = [[1, 2], [3, 4]]
    inversa(original)
    assert original == [[1, 2], [3, 4]]
    for invalida in ([], [[1, 2]], [[1, 2], [2, 4]]):
        try:
            inversa(invalida)
        except ValueError:
            pass
        else:
            raise AssertionError("La matriz debería rechazarse")
    print("Ejercicio 273: pruebas superadas")
