"""
Enunciado:

215. Suma de Nodos: Implementa una función que calcule la suma de
    todos los nodos en un árbol.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Nodo:
    """Nodo de un árbol binario de valores enteros."""

    valor: int
    izquierdo: Nodo | None = None
    derecho: Nodo | None = None


def suma_nodos(raiz: Nodo | None) -> int:
    """Suma los valores de todos los nodos en O(n), sin alterar el árbol."""
    if raiz is None:
        return 0
    total = 0
    pendientes = [raiz]
    while pendientes:
        nodo = pendientes.pop()
        total += nodo.valor
        if nodo.izquierdo is not None:
            pendientes.append(nodo.izquierdo)
        if nodo.derecho is not None:
            pendientes.append(nodo.derecho)
    return total


if __name__ == "__main__":
    arbol = Nodo(5, Nodo(-2, Nodo(3)), Nodo(10, Nodo(0), Nodo(4)))
    assert suma_nodos(arbol) == 20
    assert suma_nodos(Nodo(-7)) == -7
    assert suma_nodos(None) == 0
    print("Ejercicio 215: pruebas superadas")
