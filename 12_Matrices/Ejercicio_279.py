"""Ejercicio 279 — Matrices Simétricas.

Enunciado:
    Implementa un algoritmo para verificar si una matriz es simétrica o no.

Solución:
    Una matriz real es simétrica si es cuadrada y A[i][j] == A[j][i]
    para todas las posiciones. Se comparan solo los elementos situados
    sobre la diagonal, con tolerancias opcionales para números decimales.
"""
from collections.abc import Sequence
from math import isclose, isfinite

Matriz = Sequence[Sequence[int | float]]


def es_simetrica(
    matriz: Matriz, tolerancia: float = 0.0
) -> bool:
    """Indicar si la matriz es cuadrada, finita y simétrica.

    La tolerancia absoluta permite pequeñas diferencias de redondeo.
    Una matriz vacía o no cuadrada no se considera simétrica.
    """
    if not isfinite(tolerancia) or tolerancia < 0:
        raise ValueError("La tolerancia debe ser finita y no negativa")
    n = len(matriz)
    if n == 0 or any(len(fila) != n for fila in matriz):
        return False
    if any(
        isinstance(valor, bool)
        or not isinstance(valor, (int, float))
        or not isfinite(valor)
        for fila in matriz for valor in fila
    ):
        raise ValueError("Todos los elementos deben ser números reales finitos")
    return all(
        isclose(matriz[i][j], matriz[j][i], rel_tol=0.0, abs_tol=tolerancia)
        for i in range(n) for j in range(i + 1, n)
    )


if __name__ == '__main__':
    assert es_simetrica([[1, 2], [2, 3]])
    assert es_simetrica([[7]])
    assert es_simetrica([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
    assert not es_simetrica([[1, 2], [3, 4]])
    assert not es_simetrica([[1, 2, 3], [4, 5, 6]])
    assert not es_simetrica([])
    assert not es_simetrica([[]])
    assert es_simetrica([[1.0, 0.3], [0.1 + 0.2, 2.0]], 1e-12)
    assert not es_simetrica([[1.0, 0.3], [0.1 + 0.2, 2.0]])
    for matriz_invalida in ([[float('nan')]], [[True]]):
        try:
            es_simetrica(matriz_invalida)
        except ValueError:
            pass
        else:
            raise AssertionError("Se aceptó una matriz inválida")
    try:
        es_simetrica([[1]], -1)
    except ValueError:
        pass
    else:
        raise AssertionError("Se aceptó una tolerancia negativa")
    print("Ejercicio 279: pruebas superadas")
