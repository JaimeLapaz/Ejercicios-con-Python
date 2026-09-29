"""
Enunciado:

137. Ordenar por Valor de Atributo: Implementa una función de orden
superior que tome una lista de objetos y un atributo como argumentos,
y ordene la lista según el valor de ese atributo.

Solución:
"""

from dataclasses import dataclass
from operator import attrgetter
from typing import TypeVar

T = TypeVar("T")


def ordenar_por_atributo(
    objetos: list[T], atributo: str, descendente: bool = False
) -> list[T]:
    """Ordena objetos por el atributo indicado sin alterar la lista original."""
    if not atributo:
        raise ValueError("Debes indicar el nombre de un atributo.")

    return sorted(objetos, key=attrgetter(atributo), reverse=descendente)


@dataclass
class Producto:
    nombre: str
    precio: float


if __name__ == "__main__":
    productos = [
        Producto("Teclado", 45.0),
        Producto("Ratón", 20.0),
        Producto("Monitor", 180.0),
    ]
    por_precio = ordenar_por_atributo(productos, "precio")
    por_nombre = ordenar_por_atributo(productos, "nombre")

    print("Por precio:", por_precio)
    print("Por nombre:", por_nombre)
    assert [producto.precio for producto in por_precio] == [20.0, 45.0, 180.0]
    assert [producto.nombre for producto in por_nombre] == [
        "Monitor", "Ratón", "Teclado"
    ]
