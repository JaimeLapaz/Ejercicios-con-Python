"""
Enunciado:

228. Recorrido de Árbol Binario: Implementa una función recursiva que
    realice un recorrido en orden de un árbol binario.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Nodo(Generic[T]):
    """Nodo de un árbol binario, sin requisito de ordenación."""

    valor: T
    izquierdo: Nodo[T] | None = None
    derecho: Nodo[T] | None = None


def recorrido_inorden(raiz: Nodo[T] | None) -> list[T]:
    """Recorre recursivamente izquierda, raíz y derecha.

    Visita cada nodo una vez: O(n) tiempo y O(h) pila de llamadas,
    además de O(n) memoria para el resultado (h es la altura).
    """
    resultado: list[T] = []

    def visitar(nodo: Nodo[T] | None) -> None:
        if nodo is None:
            return
        visitar(nodo.izquierdo)
        resultado.append(nodo.valor)
        visitar(nodo.derecho)

    visitar(raiz)
    return resultado


if __name__ == "__main__":
    arbol = Nodo(
        8,
        Nodo(3, Nodo(1), Nodo(6, Nodo(4), Nodo(7))),
        Nodo(10, None, Nodo(14, Nodo(13))),
    )
    assert recorrido_inorden(arbol) == [1, 3, 4, 6, 7, 8, 10, 13, 14]
    assert recorrido_inorden(None) == []
    assert recorrido_inorden(Nodo("único")) == ["único"]
    assert recorrido_inorden(Nodo(1, Nodo(9), Nodo(-2))) == [9, 1, -2]
    assert recorrido_inorden(Nodo(5, Nodo(5), Nodo(5))) == [5, 5, 5]
    assert recorrido_inorden(arbol) == [1, 3, 4, 6, 7, 8, 10, 13, 14]
    print("Ejercicio 228: pruebas superadas")
