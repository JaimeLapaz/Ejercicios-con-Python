"""Enunciado:
249. Búsqueda de Camino: verificar si existe un camino entre dos
vértices de un grafo.

Solución:
Recorrer el grafo mediante búsqueda en anchura (BFS), registrando
vértices visitados para evitar ciclos.
"""
from __future__ import annotations
from collections import deque
from typing import Hashable, Mapping, Iterable


def existe_camino(
    grafo: Mapping[Hashable, Iterable[Hashable]],
    origen: Hashable,
    destino: Hashable,
) -> bool:
    """Indica si el destino es alcanzable desde el origen.

    Los vértices ausentes no son válidos. Un vértice sin lista de
    adyacencia explícita puede aparecer como vecino (sumidero).
    """
    vertices = set(grafo)
    for vecinos in grafo.values():
        vertices.update(vecinos)
    if origen not in vertices or destino not in vertices:
        return False
    pendientes = deque([origen])
    visitados = {origen}
    while pendientes:
        actual = pendientes.popleft()
        if actual == destino:
            return True
        for vecino in grafo.get(actual, ()):
            if vecino not in visitados:
                visitados.add(vecino)
                pendientes.append(vecino)
    return False


if __name__ == "__main__":
    red = {"A": {"B"}, "B": {"A", "C"}, "C": {"B"}, "D": set()}
    assert existe_camino(red, "A", "C")
    assert not existe_camino(red, "A", "D")
    assert existe_camino(red, "D", "D")
    assert not existe_camino(red, "A", "Z")
    assert existe_camino({"A": ["B"]}, "A", "B")
    print("¿Hay camino de A a C?", existe_camino(red, "A", "C"))
