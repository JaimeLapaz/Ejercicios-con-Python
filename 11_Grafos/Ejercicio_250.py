"""Enunciado:
250. Grado de un Vértice: calcular el grado de un vértice
en un grafo no dirigido.

Solución:
Contar las aristas incidentes a partir de sus vecinos.
Un lazo contribuye dos unidades al grado, según la definición usual.
"""
from __future__ import annotations
from typing import Hashable, Mapping, Iterable


def grado_vertice(
    grafo: Mapping[Hashable, Iterable[Hashable]], vertice: Hashable
) -> int:
    """Devuelve el grado; exige que el vértice esté representado."""
    if vertice not in grafo:
        raise KeyError(f"Vértice inexistente: {vertice!r}")
    vecinos = set(grafo[vertice])
    return len(vecinos) + (1 if vertice in vecinos else 0)


if __name__ == "__main__":
    red = {"A": {"B", "C"}, "B": {"A"}, "C": {"A"}, "D": set()}
    assert grado_vertice(red, "A") == 2
    assert grado_vertice(red, "D") == 0
    assert grado_vertice({"X": {"X"}}, "X") == 2
    try:
        grado_vertice(red, "Z")
    except KeyError:
        pass
    else:
        raise AssertionError("Se esperaba KeyError")
    print("Grado de A:", grado_vertice(red, "A"))
