"""Ejercicio 258 — Dijkstra y Bellman-Ford.

Enunciado:
    Implementar ambos algoritmos para rutas más cortas en grafos ponderados,
    con pesos no negativos para Dijkstra y negativos para Bellman-Ford.

Solución:
    Representamos el grafo dirigido mediante listas de adyacencia. Dijkstra
    usa un montículo mínimo; Bellman-Ford relaja aristas |V|-1 veces y
    detecta ciclos negativos alcanzables desde el origen.
"""
from heapq import heappop, heappush
from math import inf, isfinite
from typing import Hashable, TypeVar

Vertice = TypeVar("Vertice", bound=Hashable)
Grafo = dict[Vertice, dict[Vertice, float]]


def _preparar(grafo: Grafo[Vertice], origen: Vertice) -> tuple[set[Vertice], list[tuple[Vertice, Vertice, float]]]:
    """Incluir destinos sin entrada propia y validar pesos."""
    vertices = set(grafo)
    aristas = []
    for u, vecinos in grafo.items():
        for v, peso in vecinos.items():
            if not isfinite(peso):
                raise ValueError("Los pesos deben ser finitos")
            vertices.add(v)
            aristas.append((u, v, peso))
    if origen not in vertices:
        raise ValueError("El origen no pertenece al grafo")
    return vertices, aristas


def dijkstra(grafo: Grafo[Vertice], origen: Vertice) -> tuple[dict[Vertice, float], dict[Vertice, Vertice | None]]:
    """Distancias mínimas y predecesores; rechaza cualquier peso negativo."""
    vertices, aristas = _preparar(grafo, origen)
    if any(peso < 0 for _, _, peso in aristas):
        raise ValueError("Dijkstra no admite pesos negativos")
    distancias = {v: inf for v in vertices}
    anteriores: dict[Vertice, Vertice | None] = {v: None for v in vertices}
    distancias[origen] = 0
    # Contador para evitar comparar vértices de tipos heterogéneos en empates.
    cola = [(0.0, 0, origen)]
    secuencia = 0
    while cola:
        distancia, _, actual = heappop(cola)
        if distancia > distancias[actual]:
            continue
        for vecino, peso in grafo.get(actual, {}).items():
            nueva = distancia + peso
            if nueva < distancias[vecino]:
                distancias[vecino] = nueva
                anteriores[vecino] = actual
                secuencia += 1
                heappush(cola, (nueva, secuencia, vecino))
    return distancias, anteriores


def bellman_ford(grafo: Grafo[Vertice], origen: Vertice) -> tuple[dict[Vertice, float], dict[Vertice, Vertice | None]]:
    """Permite pesos negativos; rechaza ciclos negativos alcanzables."""
    vertices, aristas = _preparar(grafo, origen)
    distancias = {v: inf for v in vertices}
    anteriores: dict[Vertice, Vertice | None] = {v: None for v in vertices}
    distancias[origen] = 0
    for _ in range(len(vertices) - 1):
        cambios = False
        for u, v, peso in aristas:
            if distancias[u] != inf and distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
                anteriores[v] = u
                cambios = True
        if not cambios:
            break
    for u, v, peso in aristas:
        if distancias[u] != inf and distancias[u] + peso < distancias[v]:
            raise ValueError("Existe un ciclo negativo alcanzable")
    return distancias, anteriores


def reconstruir_camino(anteriores: dict[Vertice, Vertice | None],
                       origen: Vertice, destino: Vertice) -> list[Vertice]:
    """Devolver la ruta al destino, o [] si no es alcanzable."""
    if origen not in anteriores or destino not in anteriores:
        return []
    ruta = []
    actual: Vertice | None = destino
    visitados: set[Vertice] = set()
    while actual is not None and actual not in visitados:
        ruta.append(actual)
        if actual == origen:
            return ruta[::-1]
        visitados.add(actual)
        actual = anteriores[actual]
    return []


if __name__ == "__main__":
    positivo = {"A": {"B": 4, "C": 1}, "C": {"B": 2}, "B": {"D": 1}, "D": {}, "X": {}}
    dist, prev = dijkstra(positivo, "A")
    assert dist["D"] == 4 and dist["X"] == inf
    assert reconstruir_camino(prev, "A", "D") == ["A", "C", "B", "D"]
    assert reconstruir_camino(prev, "A", "X") == []
    assert bellman_ford(positivo, "A")[0] == dist
    negativo = {"S": {"A": 4, "B": 5}, "A": {"B": -2}, "B": {"T": 3}, "T": {}}
    assert bellman_ford(negativo, "S")[0]["T"] == 5
    try:
        dijkstra(negativo, "S")
        assert False, "Se esperaba ValueError"
    except ValueError:
        pass
    try:
        bellman_ford({"A": {"B": 1}, "B": {"A": -2}}, "A")
        assert False, "Se esperaba detectar ciclo negativo"
    except ValueError:
        pass
    print("Ejercicio 258: pruebas superadas.")
