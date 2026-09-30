"""
Enunciado:

142. Conteo de Elementos: Diseña una función de orden superior que
tome una lista de objetos y una función de conteo basada en una
propiedad, y devuelva un diccionario con la cantidad de elementos
para cada valor de esa propiedad.

Solución:
"""

from collections.abc import Callable, Hashable
from typing import TypeVar

T = TypeVar("T")
K = TypeVar("K", bound=Hashable)


def contar_por_propiedad(
    objetos: list[T], propiedad: Callable[[T], K]
) -> dict[K, int]:
    """Cuenta cuántos objetos corresponden a cada clave calculada."""
    conteos: dict[K, int] = {}
    for objeto in objetos:
        clave = propiedad(objeto)
        conteos[clave] = conteos.get(clave, 0) + 1
    return conteos


if __name__ == "__main__":
    productos = [
        {"nombre": "Manzana", "categoria": "fruta"},
        {"nombre": "Zanahoria", "categoria": "verdura"},
        {"nombre": "Pera", "categoria": "fruta"},
        {"nombre": "Lechuga", "categoria": "verdura"},
        {"nombre": "Plátano", "categoria": "fruta"},
    ]
    por_categoria = contar_por_propiedad(
        productos, lambda producto: producto["categoria"]
    )
    por_inicial = contar_por_propiedad(
        productos, lambda producto: producto["nombre"][0]
    )

    print("Por categoría:", por_categoria)
    print("Por inicial:", por_inicial)
    assert por_categoria == {"fruta": 3, "verdura": 2}
    assert por_inicial == {"M": 1, "Z": 1, "P": 2, "L": 1}
    assert contar_por_propiedad([], lambda elemento: elemento) == {}
