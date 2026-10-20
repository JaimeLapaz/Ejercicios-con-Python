"""
Enunciado:

217. Búsqueda en Árbol Binario: Crea una función que busque un valor
    en un árbol binario y devuelva el nodo correspondiente.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Nodo(Generic[T]):
    """Nodo de un árbol binario, no necesariamente de búsqueda (BST)."""

    valor: T
    izquierdo: Nodo[T] | None = None
    derecho: Nodo[T] | None = None


def buscar_nodo(raiz: Nodo[T] | None, valor: T) -> Nodo[T] | None:
    """Busca en preorden y devuelve el primer nodo coincidente o None.

    Al no suponer que el árbol está ordenado, visita hasta O(n) nodos.
    Utiliza una pila explícita para evitar límites de recursión.
    """
    if raiz is None:
        return None
    pendientes = [raiz]
    while pendientes:
        nodo = pendientes.pop()
        if nodo.valor == valor:
            return nodo
        if nodo.derecho is not None:
            pendientes.append(nodo.derecho)
        if nodo.izquierdo is not None:
            pendientes.append(nodo.izquierdo)
    return None


if __name__ == "__main__":
    primero = Nodo(7)
    segundo = Nodo(7)
    arbol = Nodo(10, Nodo(3, primero), Nodo(5, segundo))
    assert buscar_nodo(arbol, 7) is primero
    assert buscar_nodo(arbol, 5) is arbol.derecho
    assert buscar_nodo(arbol, 10) is arbol
    assert buscar_nodo(arbol, 99) is None
    assert buscar_nodo(None, 10) is None
    assert buscar_nodo(Nodo("texto"), "texto") == Nodo("texto")
    print("Ejercicio 217: pruebas superadas")
