"""Enunciado:
248. Representación de Grafo: implementar una clase Grafo no dirigido
que permita agregar vértices y aristas.

Solución:
Usar un diccionario de conjuntos de vecinos. Las aristas se almacenan
en ambos sentidos y los vértices aislados también se representan.
"""
from __future__ import annotations
from typing import Hashable


class Grafo:
    """Grafo simple no dirigido, sin aristas duplicadas."""

    def __init__(self) -> None:
        self.adyacencia: dict[Hashable, set[Hashable]] = {}

    def agregar_vertice(self, vertice: Hashable) -> None:
        """Agrega un vértice si todavía no existe."""
        self.adyacencia.setdefault(vertice, set())

    def agregar_arista(self, origen: Hashable, destino: Hashable) -> None:
        """Conecta dos vértices, creándolos cuando sea necesario."""
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        self.adyacencia[origen].add(destino)
        self.adyacencia[destino].add(origen)

    def vecinos(self, vertice: Hashable) -> set[Hashable]:
        """Devuelve una copia de los vecinos de un vértice."""
        if vertice not in self.adyacencia:
            raise KeyError(f"Vértice inexistente: {vertice!r}")
        return self.adyacencia[vertice].copy()


if __name__ == "__main__":
    grafo = Grafo()
    grafo.agregar_vertice("aislado")
    grafo.agregar_arista("A", "B")
    grafo.agregar_arista("A", "C")
    grafo.agregar_arista("A", "B")
    assert grafo.vecinos("A") == {"B", "C"}
    assert grafo.vecinos("B") == {"A"}
    assert grafo.vecinos("aislado") == set()
    print("Grafo:", grafo.adyacencia)
