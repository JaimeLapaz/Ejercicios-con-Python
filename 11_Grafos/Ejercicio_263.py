"""Ejercicio 263 — Algoritmo de Prim.

Enunciado:
    Crea el algoritmo de Prim para encontrar el árbol de expansión mínima
    en un grafo ponderado no dirigido.

Solución:
    Utilizar un montículo de aristas candidatas para expandir el árbol
    desde un vértice inicial. Repetir desde los vértices aún no visitados
    para obtener un bosque mínimo cuando el grafo sea desconectado.
"""
from heapq import heappop, heappush
from itertools import count
from math import isfinite
from typing import Hashable, TypeVar

Vertice = TypeVar("Vertice", bound=Hashable)
Grafo = dict[Vertice, dict[Vertice, float]]
Arista = tuple[Vertice, Vertice, float]


def prim(grafo: Grafo[Vertice]) -> tuple[float, list[Arista[Vertice]]]:
    """Obtener bosque de expansión mínima; O((V + E) log E) tiempo.

    Se exige que cada arista tenga su inversa con idéntico peso.
    """
    for origen, vecinos in grafo.items():
        for destino, peso in vecinos.items():
            if destino not in grafo:
                raise ValueError("Todos los vértices deben figurar como claves")
            if not isfinite(peso):
                raise ValueError("Los pesos deben ser finitos")
            if origen not in grafo[destino] or grafo[destino][origen] != peso:
                raise ValueError("El grafo debe ser no dirigido y simétrico")

    visitados: set[Vertice] = set()
    resultado: list[Arista[Vertice]] = []
    total = 0.0
    desempate = count()

    for inicio in grafo:
        if inicio in visitados:
            continue
        visitados.add(inicio)
        # El contador evita comparar vértices de tipos no ordenables.
        pendientes: list[tuple[float, int, Vertice, Vertice]] = []
        for vecino, peso in grafo[inicio].items():
            if vecino not in visitados:
                heappush(pendientes, (peso, next(desempate), inicio, vecino))

        while pendientes:
            peso, _, origen, destino = heappop(pendientes)
            if destino in visitados:
                continue
            visitados.add(destino)
            resultado.append((origen, destino, peso))
            total += peso
            for vecino, nuevo_peso in grafo[destino].items():
                if vecino not in visitados:
                    heappush(
                        pendientes, (nuevo_peso, next(desempate), destino, vecino)
                    )
    return total, resultado


if __name__ == "__main__":
    grafo = {
        "A": {"B": 1, "C": 4},
        "B": {"A": 1, "C": 2},
        "C": {"A": 4, "B": 2, "D": 3},
        "D": {"C": 3},
    }
    peso, arbol = prim(grafo)
    assert peso == 6
    assert len(arbol) == 3
    assert prim({"A": {"B": -2}, "B": {"A": -2}, "C": {}})[0] == -2
    assert prim({}) == (0.0, [])
    try:
        prim({"A": {"B": 1}, "B": {"A": 2}})
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba rechazar pesos asimétricos")
    print("Ejercicio 263: pruebas superadas.")
