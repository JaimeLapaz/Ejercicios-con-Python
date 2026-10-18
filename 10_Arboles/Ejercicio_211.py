"""
Enunciado:

211. Recorrido en Anchura: Desarrolla una función para realizar un
recorrido en anchura (BFS) en un árbol.

Solución:
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass
class Nodo:
    """Nodo de un árbol binario."""

    valor: int
    izquierdo: Nodo | None = None
    derecho: Nodo | None = None


def recorrido_bfs(raiz: Nodo | None) -> list[int]:
    """Devuelve los valores por niveles, de izquierda a derecha.

    Usa una cola FIFO; complejidad temporal O(n).
    """
    if raiz is None:
        return []

    pendientes = deque([raiz])
    resultado: list[int] = []
    while pendientes:
        actual = pendientes.popleft()
        resultado.append(actual.valor)
        if actual.izquierdo is not None:
            pendientes.append(actual.izquierdo)
        if actual.derecho is not None:
            pendientes.append(actual.derecho)
    return resultado


if __name__ == "__main__":
    assert recorrido_bfs(None) == []
    assert recorrido_bfs(Nodo(5)) == [5]
    arbol = Nodo(1, Nodo(2, Nodo(4), Nodo(5)), Nodo(3, None, Nodo(6)))
    assert recorrido_bfs(arbol) == [1, 2, 3, 4, 5, 6]
    arbol.izquierdo = None
    assert recorrido_bfs(arbol) == [1, 3, 6]
    print("Ejercicio 211: pruebas superadas")
