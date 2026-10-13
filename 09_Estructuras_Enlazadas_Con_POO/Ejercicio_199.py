"""
Enunciado:

199. Búsqueda en Anchura (BFS): Desarrolla una clase Grafo que utilice
    una cola para realizar un recorrido en anchura (BFS) en un grafo.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Hashable, TypeVar

T = TypeVar("T", bound=Hashable)


@dataclass
class NodoCola(Generic[T]):
    """Nodo de una cola simplemente enlazada."""

    valor: T
    siguiente: NodoCola[T] | None = None


class Cola(Generic[T]):
    """Cola FIFO enlazada, con operaciones O(1)."""

    def __init__(self) -> None:
        self._frente: NodoCola[T] | None = None
        self._final: NodoCola[T] | None = None

    def encolar(self, valor: T) -> None:
        nuevo = NodoCola(valor)
        if self._final is None:
            self._frente = nuevo
        else:
            self._final.siguiente = nuevo
        self._final = nuevo

    def desencolar(self) -> T:
        if self._frente is None:
            raise IndexError("La cola está vacía")
        valor = self._frente.valor
        self._frente = self._frente.siguiente
        if self._frente is None:
            self._final = None
        return valor

    def esta_vacia(self) -> bool:
        return self._frente is None


class Grafo(Generic[T]):
    """Grafo no dirigido con vecinos en orden de inserción."""

    def __init__(self) -> None:
        self._adyacencias: dict[T, list[T]] = {}

    def agregar_vertice(self, vertice: T) -> None:
        """Agrega un vértice, si todavía no existe."""
        self._adyacencias.setdefault(vertice, [])

    def agregar_arista(self, origen: T, destino: T) -> None:
        """Conecta dos vértices sin duplicar aristas."""
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        if destino not in self._adyacencias[origen]:
            self._adyacencias[origen].append(destino)
        if origen not in self._adyacencias[destino]:
            self._adyacencias[destino].append(origen)

    def bfs(self, inicio: T) -> list[T]:
        """Recorre los vértices alcanzables por niveles usando una cola."""
        if inicio not in self._adyacencias:
            raise ValueError("El vértice inicial no existe")
        visitados = {inicio}
        cola: Cola[T] = Cola()
        cola.encolar(inicio)
        recorrido = []
        while not cola.esta_vacia():
            actual = cola.desencolar()
            recorrido.append(actual)
            for vecino in self._adyacencias[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.encolar(vecino)
        return recorrido


if __name__ == "__main__":
    grafo = Grafo[str]()
    for origen, destino in (
        ("A", "B"), ("A", "C"), ("B", "D"),
        ("C", "E"), ("D", "E"), ("E", "A"),
    ):
        grafo.agregar_arista(origen, destino)
    grafo.agregar_arista("A", "B")  # No duplica la conexión.
    grafo.agregar_vertice("Z")  # Vértice aislado.
    assert grafo.bfs("A") == ["A", "B", "C", "E", "D"]
    assert grafo.bfs("B") == ["B", "A", "D", "C", "E"]
    assert grafo.bfs("Z") == ["Z"]
    try:
        grafo.bfs("Inexistente")
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba ValueError")
    print("Recorrido BFS desde A:", grafo.bfs("A"))
