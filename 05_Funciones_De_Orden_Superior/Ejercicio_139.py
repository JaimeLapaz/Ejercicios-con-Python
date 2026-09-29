"""
Enunciado:

139. Agrupar Elementos por Clave: Crea una función de orden superior
que tome una lista de objetos y una función de agrupación basada en
una clave como argumentos, y devuelva un diccionario que agrupe
los objetos según la clave.

Solución:
"""

from collections.abc import Callable, Hashable
from typing import TypeVar

T = TypeVar("T")
K = TypeVar("K", bound=Hashable)


def agrupar_por_clave(
    objetos: list[T], clave: Callable[[T], K]
) -> dict[K, list[T]]:
    """Agrupa los objetos sin alterar el orden de aparición de cada grupo."""
    grupos: dict[K, list[T]] = {}
    for objeto in objetos:
        grupos.setdefault(clave(objeto), []).append(objeto)
    return grupos


if __name__ == "__main__":
    personas = [
        {"nombre": "Ana", "ciudad": "Madrid"},
        {"nombre": "Luis", "ciudad": "Granada"},
        {"nombre": "Eva", "ciudad": "Madrid"},
        {"nombre": "Leo", "ciudad": "Granada"},
    ]
    por_ciudad = agrupar_por_clave(personas, lambda persona: persona["ciudad"])

    for ciudad, habitantes in por_ciudad.items():
        print(ciudad, ":", [persona["nombre"] for persona in habitantes])

    assert [persona["nombre"] for persona in por_ciudad["Madrid"]] == ["Ana", "Eva"]
    assert [persona["nombre"] for persona in por_ciudad["Granada"]] == ["Luis", "Leo"]
