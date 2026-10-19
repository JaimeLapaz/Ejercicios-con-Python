"""
Enunciado:

214. Recorrido Postorden: Escribe una función para realizar un recorrido
    postorden en un árbol.

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


def recorrido_postorden(raiz: Nodo | None) -> list[int]:
    """Recorre izquierda, derecha y raíz, en ese orden (O(n))."""
    resultado: list[int] = []

    def visitar(nodo: Nodo | None) -> None:
        if nodo is None:
            return
        visitar(nodo.izquierdo)
        visitar(nodo.derecho)
        resultado.append(nodo.valor)

    visitar(raiz)
    return resultado


if __name__ == "__main__":
    arbol = Nodo(1, Nodo(2, Nodo(4), Nodo(5)), Nodo(3, Nodo(6), Nodo(7)))
    assert recorrido_postorden(arbol) == [4, 5, 2, 6, 7, 3, 1]
    assert recorrido_postorden(Nodo(9)) == [9]
    assert recorrido_postorden(None) == []
    print("Ejercicio 214: pruebas superadas")
