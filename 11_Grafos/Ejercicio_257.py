"""Enunciado:
257. Grafo Bipartito: determinar si un grafo es bipartito.

Solución:
Colorear mediante BFS cada componente conexa con dos colores
alternos. Una arista que une vértices del mismo color demuestra
que el grafo no es bipartito.
"""
from __future__ import annotations

from collections import deque
from typing import Hashable, Iterable, Mapping

Vertice = Hashable
Grafo = Mapping[Vertice, Iterable[Vertice]]


def es_bipartito(grafo: Grafo) -> bool:
    """Comprueba si un grafo no dirigido admite dos colores.

    La lista de adyacencia debe describir aristas no dirigidas:
    cada arista u-v debe aparecer en ambos sentidos.
    """
    adyacencia = {vertice: set(vecinos) for vertice, vecinos in grafo.items()}
    for vertice, vecinos in list(adyacencia.items()):
        for vecino in vecinos:
            adyacencia.setdefault(vecino, set())
            if vertice not in adyacencia[vecino]:
                raise ValueError("Las aristas deben aparecer en ambos sentidos")

    colores: dict[Vertice, int] = {}
    for inicio in adyacencia:
        if inicio in colores:
            continue
        colores[inicio] = 0
        cola = deque([inicio])
        while cola:
            actual = cola.popleft()
            for vecino in adyacencia[actual]:
                if vecino not in colores:
                    colores[vecino] = 1 - colores[actual]
                    cola.append(vecino)
                elif colores[vecino] == colores[actual]:
                    return False
    return True


if __name__ == "__main__":
    cuadrado = {
        1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]
    }
    triangulo = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    assert es_bipartito(cuadrado)
    assert not es_bipartito(triangulo)
    assert es_bipartito({1: [], 2: [3], 3: [2]})
    assert es_bipartito({})
    assert not es_bipartito({1: [1]})
    try:
        es_bipartito({1: [2], 2: []})
    except ValueError:
        pass
    else:
        raise AssertionError("Se debe validar la simetría")
    print("¿Es bipartito el cuadrado?", es_bipartito(cuadrado))
