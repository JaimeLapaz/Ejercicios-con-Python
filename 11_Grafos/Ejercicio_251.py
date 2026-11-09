"""Enunciado:
251. Recorrido en Profundidad: implementar DFS en un grafo.

Solución:
Utilizar una pila explícita y un conjunto de visitados. El orden
de los vecinos sigue el orden de iteración de la colección recibida.
"""
from __future__ import annotations
from typing import Hashable, Mapping, Iterable


def recorrido_dfs(
    grafo: Mapping[Hashable, Iterable[Hashable]], inicio: Hashable
) -> list[Hashable]:
    """Devuelve los vértices alcanzables en orden de profundidad."""
    vertices = set(grafo)
    for vecinos in grafo.values():
        vertices.update(vecinos)
    if inicio not in vertices:
        raise KeyError(f"Vértice inexistente: {inicio!r}")
    visitados: set[Hashable] = set()
    recorrido: list[Hashable] = []
    pila = [inicio]
    while pila:
        actual = pila.pop()
        if actual in visitados:
            continue
        visitados.add(actual)
        recorrido.append(actual)
        pila.extend(reversed(tuple(grafo.get(actual, ()))))
    return recorrido


if __name__ == "__main__":
    red = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": [], "E": []}
    assert recorrido_dfs(red, "A") == ["A", "B", "D", "C"]
    assert recorrido_dfs(red, "E") == ["E"]
    assert recorrido_dfs({"A": ["B"]}, "A") == ["A", "B"]
    print("DFS desde A:", recorrido_dfs(red, "A"))
