"""
Enunciado:

145. Ordenar por Frecuencia: Implementa una función de orden superior
que tome una lista de elementos y una función de frecuencia, y ordene
la lista en función de la frecuencia de cada elemento.

Solución:
"""

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def ordenar_por_frecuencia(
    elementos: list[T], frecuencia: Callable[[T], int | float]
) -> list[T]:
    """Devuelve los elementos ordenados de mayor a menor frecuencia."""
    return sorted(elementos, key=frecuencia, reverse=True)


if __name__ == "__main__":
    palabras = ["python", "sol", "programacion", "código"]
    por_longitud = ordenar_por_frecuencia(palabras, len)

    frecuencias = {"python": 8, "sol": 12, "programacion": 3, "código": 6}
    por_apariciones = ordenar_por_frecuencia(
        palabras, lambda palabra: frecuencias[palabra]
    )

    print("Por longitud:", por_longitud)
    print("Por apariciones:", por_apariciones)
    assert por_longitud == ["programacion", "python", "código", "sol"]
    assert por_apariciones == ["sol", "python", "código", "programacion"]
    assert ordenar_por_frecuencia([], lambda _: 0) == []
