"""
Enunciado:

210. Recorrido en Profundidad: Implementa una función para realizar un
recorrido en profundidad (DFS) en un árbol.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Nodo:
    """Nodo de un árbol binario."""

    valor: int
    izquierdo: Nodo | None = None
    derecho: Nodo | None = None


def recorrido_dfs(raiz: Nodo | None) -> list[int]:
    """Recorre en profundidad en preorden: raíz, izquierda, derecha.

    Usa una pila explícita para evitar depender de la recursión.
    """
    if raiz is None:
        return []

    pendientes = [raiz]
    visitados: list[int] = []
    while pendientes:
        actual = pendientes.pop()
        visitados.append(actual.valor)
        if actual.derecho is not None:
            pendientes.append(actual.derecho)
        if actual.izquierdo is not None:
            pendientes.append(actual.izquierdo)
    return visitados


if __name__ == "__main__":
    assert recorrido_dfs(None) == []
    assert recorrido_dfs(Nodo(7)) == [7]
    arbol = Nodo(1, Nodo(2, Nodo(4), Nodo(5)), Nodo(3, None, Nodo(6)))
    assert recorrido_dfs(arbol) == [1, 2, 4, 5, 3, 6]
    assert arbol.izquierdo is not None and arbol.izquierdo.valor == 2
    print("Ejercicio 210: pruebas superadas")
