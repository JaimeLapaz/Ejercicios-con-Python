"""
Enunciado:

208. Árbol Binario Simple: Crea una clase Nodo para representar nodos en
un árbol binario y una clase ArbolBinario que permita agregar nodos y
realizar un recorrido en orden.

Solución:
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass
class Nodo:
    """Nodo con un valor y, como máximo, dos hijos."""

    valor: int
    izquierdo: Nodo | None = None
    derecho: Nodo | None = None


class ArbolBinario:
    """Árbol binario que inserta por niveles, de izquierda a derecha."""

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def agregar_nodo(self, valor: int) -> None:
        """Ocupa el primer hueco disponible en orden de anchura."""
        nuevo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo
            return

        pendientes = deque([self.raiz])
        while pendientes:
            actual = pendientes.popleft()
            if actual.izquierdo is None:
                actual.izquierdo = nuevo
                return
            pendientes.append(actual.izquierdo)
            if actual.derecho is None:
                actual.derecho = nuevo
                return
            pendientes.append(actual.derecho)

    def recorrido_en_orden(self) -> list[int]:
        """Devuelve izquierda, raíz, derecha, sin alterar el árbol."""
        resultado: list[int] = []

        def visitar(nodo: Nodo | None) -> None:
            if nodo is None:
                return
            visitar(nodo.izquierdo)
            resultado.append(nodo.valor)
            visitar(nodo.derecho)

        visitar(self.raiz)
        return resultado


if __name__ == "__main__":
    arbol = ArbolBinario()
    assert arbol.recorrido_en_orden() == []
    for numero in range(1, 8):
        arbol.agregar_nodo(numero)
    assert arbol.recorrido_en_orden() == [4, 2, 5, 1, 6, 3, 7]
    assert arbol.raiz is not None and arbol.raiz.valor == 1
    assert arbol.raiz.derecho is not None and arbol.raiz.derecho.valor == 3
    arbol.agregar_nodo(8)
    assert arbol.recorrido_en_orden() == [8, 4, 2, 5, 1, 6, 3, 7]
    print("Ejercicio 208: pruebas superadas")
