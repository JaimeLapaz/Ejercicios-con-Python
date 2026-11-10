"""Enunciado:
254. Árbol de Expansión Mínima: encontrar el árbol de expansión mínima
de un grafo ponderado.

Solución:
Aplicar Prim con una cola de prioridad. Para grafos desconectados
devolver un bosque de expansión mínima; cada arista se elige una vez.
"""
from __future__ import annotations

import heapq
from itertools import count
from typing import Hashable, Iterable, Mapping

Vertice = Hashable
Grafo = Mapping[Vertice, Iterable[tuple[Vertice, float]]]


def bosque_expansion_minima(
    grafo: Grafo,
) -> tuple[float, list[tuple[Vertice, Vertice, float]]]:
    """Devuelve (peso total, aristas) de un bosque mínimo no dirigido.

    Las aristas deben figurar en ambos sentidos con el mismo peso.
    """
    adyacencia: dict[Vertice, list[tuple[Vertice, float]]] = {
        vertice: list(vecinos) for vertice, vecinos in grafo.items()
    }
    pesos: dict[tuple[Vertice, Vertice], float] = {}
    for origen, vecinos in adyacencia.items():
        for destino, peso in vecinos:
            if destino not in adyacencia:
                raise ValueError("Falta un vértice de destino en el grafo")
            if origen == destino:
                continue
            if (destino, origen) in pesos and pesos[destino, origen] != peso:
                raise ValueError("Pesos inconsistentes en arista no dirigida")
            pesos[origen, destino] = peso
    for origen, destino in pesos:
        if (destino, origen) not in pesos:
            raise ValueError("Las aristas deben aparecer en ambos sentidos")

    visitados: set[Vertice] = set()
    aristas: list[tuple[Vertice, Vertice, float]] = []
    total = 0.0
    secuencia = count()
    for inicio in adyacencia:
        if inicio in visitados:
            continue
        visitados.add(inicio)
        cola: list[tuple[float, int, Vertice, Vertice]] = []
        for destino, peso in adyacencia[inicio]:
            heapq.heappush(cola, (peso, next(secuencia), inicio, destino))
        while cola:
            peso, _, origen, destino = heapq.heappop(cola)
            if destino in visitados:
                continue
            visitados.add(destino)
            total += peso
            aristas.append((origen, destino, peso))
            for siguiente, peso_siguiente in adyacencia[destino]:
                if siguiente not in visitados:
                    heapq.heappush(
                        cola, (peso_siguiente, next(secuencia), destino, siguiente)
                    )
    return total, aristas


if __name__ == "__main__":
    red = {
        "A": [("B", 4), ("C", 1)],
        "B": [("A", 4), ("C", 2)],
        "C": [("A", 1), ("B", 2)],
        "D": [],
    }
    peso, aristas = bosque_expansion_minima(red)
    assert peso == 3 and len(aristas) == 2
    assert bosque_expansion_minima({"A": [], "B": []}) == (0.0, [])
    print("Bosque mínimo:", aristas, "peso:", peso)
