"""
Enunciado:

138. Filtrado de Elementos Duplicados: Diseña una función de orden
superior que tome una lista y una función de filtro que identifique
elementos duplicados, y devuelva una lista con elementos únicos.

Solución:
"""

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def filtrar_unicos(
    elementos: list[T], es_duplicado: Callable[[T, T], bool]
) -> list[T]:
    """Conserva la primera aparición según el criterio de duplicidad."""
    unicos: list[T] = []
    for elemento in elementos:
        if not any(es_duplicado(elemento, anterior) for anterior in unicos):
            unicos.append(elemento)
    return unicos


if __name__ == "__main__":
    palabras = ["Python", "java", "PYTHON", "Java", "Go"]
    resultado = filtrar_unicos(
        palabras, lambda nueva, anterior: nueva.casefold() == anterior.casefold()
    )

    print("Original:", palabras)
    print("Sin duplicados (ignorando mayúsculas):", resultado)
    assert resultado == ["Python", "java", "Go"]

    numeros = filtrar_unicos([1, 2, 1, 3, 2], lambda a, b: a == b)
    assert numeros == [1, 2, 3]
