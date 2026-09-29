"""
Enunciado:

132. Ordenar por Clave: Desarrolla una función de orden superior que tome
una lista de objetos y una función de clave como argumentos, y ordene
la lista en función de la clave proporcionada.

Solución:
"""

from collections.abc import Callable
from typing import Any, TypeVar

T = TypeVar("T")


def ordenar_por_clave(
    objetos: list[T], clave: Callable[[T], Any], descendente: bool = False
) -> list[T]:
    """Devuelve una lista nueva ordenada mediante la función de clave."""
    return sorted(objetos, key=clave, reverse=descendente)


if __name__ == "__main__":
    alumnos = [
        {"nombre": "Lucía", "nota": 7},
        {"nombre": "Ana", "nota": 9},
        {"nombre": "Carlos", "nota": 6},
    ]
    por_nombre = ordenar_por_clave(alumnos, lambda alumno: alumno["nombre"])
    por_nota = ordenar_por_clave(
        alumnos, lambda alumno: alumno["nota"], descendente=True
    )

    print("Por nombre:", por_nombre)
    print("Por nota descendente:", por_nota)
    assert [alumno["nombre"] for alumno in por_nombre] == ["Ana", "Carlos", "Lucía"]
    assert [alumno["nota"] for alumno in por_nota] == [9, 7, 6]
