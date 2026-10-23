"""
Enunciado:

221. Recorrido en Zigzag: Escribe una función para realizar un recorrido
    en zigzag en un árbol (alternando entre izquierda y derecha en cada nivel).

Solución:
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Nodo(Generic[T]):
    """Nodo de un árbol binario, sin restricciones de orden."""

    valor: T
    izquierdo: Nodo[T] | None = None
    derecho: Nodo[T] | None = None


def recorrido_zigzag(raiz: Nodo[T] | None) -> list[list[T]]:
    """Recorre el árbol por niveles, invirtiendo la dirección en cada nivel.

    El primer nivel se lee de izquierda a derecha. La complejidad temporal
    es O(n) y la memoria adicional es O(n) en el peor caso.
    """
    if raiz is None:
        return []

    cola = deque([raiz])
    izquierda_a_derecha = True
    niveles: list[list[T]] = []
    while cola:
        nivel: deque[T] = deque()
        for _ in range(len(cola)):
            nodo = cola.popleft()
            if izquierda_a_derecha:
                nivel.append(nodo.valor)
            else:
                nivel.appendleft(nodo.valor)
            if nodo.izquierdo is not None:
                cola.append(nodo.izquierdo)
            if nodo.derecho is not None:
                cola.append(nodo.derecho)
        niveles.append(list(nivel))
        izquierda_a_derecha = not izquierda_a_derecha
    return niveles


if __name__ == "__main__":
    arbol = Nodo(
        1,
        Nodo(2, Nodo(4), Nodo(5)),
        Nodo(3, Nodo(6), Nodo(7)),
    )
    assert recorrido_zigzag(arbol) == [[1], [3, 2], [4, 5, 6, 7]]
    assert recorrido_zigzag(arbol) == [[1], [3, 2], [4, 5, 6, 7]]
    assert recorrido_zigzag(None) == []
    assert recorrido_zigzag(Nodo("único")) == [["único"]]
    irregular = Nodo(10, Nodo(20, derecho=Nodo(40)), Nodo(30))
    assert recorrido_zigzag(irregular) == [[10], [30, 20], [40]]
    cadena = Nodo(0, Nodo(1, Nodo(2, Nodo(3))))
    assert recorrido_zigzag(cadena) == [[0], [1], [2], [3]]
    print("Ejercicio 221: pruebas superadas")
