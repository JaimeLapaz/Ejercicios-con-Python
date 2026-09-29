"""
Enunciado:

140. Operaciones de Matriz: Desarrolla una función de orden superior
que tome dos matrices y una función de operación binaria, y aplique
la operación a las matrices elemento por elemento.

Solución:
"""

from collections.abc import Callable

Numero = int | float
Matriz = list[list[Numero]]


def operar_matrices(
    primera: Matriz,
    segunda: Matriz,
    operacion: Callable[[Numero, Numero], Numero],
) -> Matriz:
    """Aplica una operación a matrices rectangulares de igual tamaño."""
    if not primera or not segunda or not primera[0] or not segunda[0]:
        raise ValueError("Las matrices deben tener filas y columnas.")

    filas = len(primera)
    columnas = len(primera[0])
    if len(segunda) != filas or len(segunda[0]) != columnas:
        raise ValueError("Las matrices deben tener las mismas dimensiones.")

    if any(len(fila) != columnas for fila in primera + segunda):
        raise ValueError("Todas las filas deben tener la misma longitud.")

    return [
        [operacion(a, b) for a, b in zip(fila_a, fila_b)]
        for fila_a, fila_b in zip(primera, segunda)
    ]


if __name__ == "__main__":
    matriz_a = [[1, 2], [3, 4]]
    matriz_b = [[5, 6], [7, 8]]
    suma = operar_matrices(matriz_a, matriz_b, lambda a, b: a + b)
    producto = operar_matrices(matriz_a, matriz_b, lambda a, b: a * b)

    print("Suma:", suma)
    print("Producto elemento a elemento:", producto)
    assert suma == [[6, 8], [10, 12]]
    assert producto == [[5, 12], [21, 32]]

    try:
        operar_matrices([[1, 2]], [[1]], lambda a, b: a + b)
    except ValueError as error:
        print("Dimensiones incompatibles:", error)
