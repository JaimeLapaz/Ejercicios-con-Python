"""
Enunciado:

129. Filtrado de Números Pares: Implementa una función de orden superior
que tome una lista de números y una función de filtro como argumentos,
y devuelva una lista con solo los números pares que pasen el filtro.

Solución:
"""

from collections.abc import Callable


def filtrar_pares(
    numeros: list[int], criterio: Callable[[int], bool]
) -> list[int]:
    """Conserva los enteros pares que también cumplen el criterio recibido."""
    return [numero for numero in numeros if numero % 2 == 0 and criterio(numero)]


if __name__ == "__main__":
    valores = [-4, -2, 0, 1, 2, 4, 7, 10]
    pares_positivos = filtrar_pares(valores, lambda numero: numero > 0)
    pares_mayores_que_cinco = filtrar_pares(valores, lambda numero: numero > 5)

    print("Pares positivos:", pares_positivos)
    print("Pares mayores que cinco:", pares_mayores_que_cinco)
    assert pares_positivos == [2, 4, 10]
    assert pares_mayores_que_cinco == [10]
