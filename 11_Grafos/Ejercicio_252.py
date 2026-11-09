"""Enunciado:
252. Recorrido en Anchura: implementar BFS en un grafo.

Solución:
Usar una cola FIFO y marcar cada vértice al encolarlo para evitar
repeticiones y recorrer primero los vértices más cercanos.
"""
from __future__ import annotations
from collections import deque
from typing import Hashable, Mapping, Iterable


def recorrido_bfs(
    grafo: Mapping[Hashable, Iterable[Hashable]], inicio: Hashable
) -> list[Hashable]:
    """Devuelve los vértices alcanzables en orden de anchura."""
    vertices = set(grafo)
    for vecinos in grafo.values():
        vertices.update(vecinos)
    if inicio not in vertices:
        raise KeyError(f"Vértice inexistente: {inicio!r}")
    cola = deque([inicio])
    visitados = {inicio}
    recorrido: list[Hashable] = []
    while cola:
        actual = cola.popleft()
        recorrido.append(actual)
        for vecino in grafo.get(actual, ()):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
    return recorrido


if __name__ == "__main__":
    red = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": [], "E": []}
    assert recorrido_bfs(red, "A") == ["A", "B", "C", "D"]
    assert recorrido_bfs(red, "E") == ["E"]
    assert recorrido_bfs({"A": ["B"]}, "A") == ["A", "B"]
    print("BFS desde A:", recorrido_bfs(red, "A"))
