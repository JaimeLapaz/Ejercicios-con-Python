"""
Enunciado:

216. Árbol Binario Espejo: Desarrolla una función que cree un árbol
    binario espejo a partir de un árbol dado.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Nodo(Generic[T]):
    """Nodo de un árbol binario."""

    valor: T
    izquierdo: Nodo[T] | None = None
    derecho: Nodo[T] | None = None


def arbol_espejo(raiz: Nodo[T] | None) -> Nodo[T] | None:
    """Devuelve una copia especular del árbol en O(n) tiempo y espacio.

    Intercambia los subárboles izquierdo y derecho de cada nodo sin
    modificar los nodos originales. Acepta árboles vacíos.
    """
    if raiz is None:
        return None

    copia = Nodo(raiz.valor)
    pendientes: list[tuple[Nodo[T], Nodo[T]]] = [(raiz, copia)]
    while pendientes:
        original, reflejado = pendientes.pop()
        if original.derecho is not None:
            reflejado.izquierdo = Nodo(original.derecho.valor)
            pendientes.append((original.derecho, reflejado.izquierdo))
        if original.izquierdo is not None:
            reflejado.derecho = Nodo(original.izquierdo.valor)
            pendientes.append((original.izquierdo, reflejado.derecho))
    return copia


def recorrido_preorden(raiz: Nodo[T] | None) -> list[T]:
    """Devuelve los valores en preorden; útil para comprobar el resultado."""
    if raiz is None:
        return []
    valores: list[T] = []
    pendientes = [raiz]
    while pendientes:
        nodo = pendientes.pop()
        valores.append(nodo.valor)
        if nodo.derecho is not None:
            pendientes.append(nodo.derecho)
        if nodo.izquierdo is not None:
            pendientes.append(nodo.izquierdo)
    return valores


if __name__ == "__main__":
    arbol = Nodo(1, Nodo(2, Nodo(4)), Nodo(3, Nodo(5), Nodo(6)))
    espejo = arbol_espejo(arbol)
    assert recorrido_preorden(espejo) == [1, 3, 6, 5, 2, 4]
    assert recorrido_preorden(arbol) == [1, 2, 4, 3, 5, 6]
    assert espejo is not arbol
    assert espejo is not None and espejo.izquierdo is not arbol.derecho
    assert arbol_espejo(None) is None
    assert arbol_espejo(arbol_espejo(arbol)) == arbol
    print("Ejercicio 216: pruebas superadas")
