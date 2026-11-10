"""Enunciado:
255. Ruta más Corta: encontrar la ruta más corta entre dos vértices
de un grafo ponderado.

Solución:
Utilizar Dijkstra con montículo de mínimos para pesos no negativos
y reconstruir el camino siguiendo los predecesores.
"""
from __future__ import annotations

import heapq
from itertools import count
from math import isfinite
from typing import Hashable, Iterable, Mapping

Vertice = Hashable
Grafo = Mapping[Vertice, Iterable[tuple[Vertice, float]]]


def ruta_mas_corta(
    grafo: Grafo, inicio: Vertice, destino: Vertice
) -> tuple[float, list[Vertice]] | None:
    """Devuelve (distancia, ruta) o None si no existe un camino."""
    adyacencia: dict[Vertice, list[tuple[Vertice, float]]] = {
        vertice: list(vecinos) for vertice, vecinos in grafo.items()
    }
    vertices = set(adyacencia)
    for vecinos in adyacencia.values():
        for vecino, peso in vecinos:
            if not isfinite(peso) or peso < 0:
                raise ValueError("Dijkstra requiere pesos finitos no negativos")
            vertices.add(vecino)
    if inicio not in vertices or destino not in vertices:
        raise KeyError("El vértice de inicio o destino no existe")
    if inicio == destino:
        return 0.0, [inicio]

    distancias: dict[Vertice, float] = {inicio: 0.0}
    anteriores: dict[Vertice, Vertice] = {}
    secuencia = count()
    cola: list[tuple[float, int, Vertice]] = [(0.0, next(secuencia), inicio)]
    while cola:
        distancia, _, actual = heapq.heappop(cola)
        if distancia > distancias[actual]:
            continue
        if actual == destino:
            ruta = [destino]
            while ruta[-1] != inicio:
                ruta.append(anteriores[ruta[-1]])
            ruta.reverse()
            return distancia, ruta
        for vecino, peso in adyacencia.get(actual, ()):
            nueva = distancia + peso
            if nueva < distancias.get(vecino, float("inf")):
                distancias[vecino] = nueva
                anteriores[vecino] = actual
                heapq.heappush(cola, (nueva, next(secuencia), vecino))
    return None


if __name__ == "__main__":
    red = {
        "A": [("B", 5), ("C", 1)],
        "B": [("D", 1)],
        "C": [("B", 2)],
        "D": [],
        "E": [],
    }
    assert ruta_mas_corta(red, "A", "D") == (4.0, ["A", "C", "B", "D"])
    assert ruta_mas_corta(red, "A", "E") is None
    assert ruta_mas_corta(red, "A", "A") == (0.0, ["A"])
    print("Ruta más corta:", ruta_mas_corta(red, "A", "D"))
