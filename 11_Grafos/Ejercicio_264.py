"""Ejercicio 264 — Caminos más Cortos en DAG.

Enunciado:
    Implementa un algoritmo eficiente para encontrar caminos más cortos
    en un grafo dirigido acíclico (DAG).

Solución:
    Ordenar topológicamente los vértices con el algoritmo de Kahn y
    relajar las aristas en ese orden. Admite pesos negativos porque
    no existen ciclos. Complejidad O(V + E).
"""
from collections import deque
from math import inf, isfinite
from typing import Hashable, TypeVar

Vertice = TypeVar("Vertice", bound=Hashable)
Grafo = dict[Vertice, dict[Vertice, float]]


def caminos_cortos_dag(
    grafo: Grafo[Vertice], origen: Vertice
) -> tuple[dict[Vertice, float], dict[Vertice, Vertice | None]]:
    """Devolver distancias y predecesores desde origen en un DAG."""
    if origen not in grafo:
        raise ValueError("El origen debe existir en el grafo")

    entrada = {vertice: 0 for vertice in grafo}
    for vertice, vecinos in grafo.items():
        for destino, peso in vecinos.items():
            if destino not in grafo:
                raise ValueError("Todos los destinos deben existir como vértices")
            if not isinstance(peso, (int, float)) or not isfinite(peso):
                raise ValueError("Los pesos deben ser números finitos")
            entrada[destino] += 1

    cola = deque(v for v, grado in entrada.items() if grado == 0)
    orden: list[Vertice] = []
    while cola:
        actual = cola.popleft()
        orden.append(actual)
        for destino in grafo[actual]:
            entrada[destino] -= 1
            if entrada[destino] == 0:
                cola.append(destino)

    if len(orden) != len(grafo):
        raise ValueError("El grafo contiene un ciclo: no es un DAG")

    distancias = {vertice: inf for vertice in grafo}
    anteriores: dict[Vertice, Vertice | None] = {v: None for v in grafo}
    distancias[origen] = 0.0
    for actual in orden:
        if distancias[actual] == inf:
            continue
        for destino, peso in grafo[actual].items():
            candidato = distancias[actual] + peso
            if candidato < distancias[destino]:
                distancias[destino] = candidato
                anteriores[destino] = actual
    return distancias, anteriores


def reconstruir_camino(
    anteriores: dict[Vertice, Vertice | None],
    origen: Vertice,
    destino: Vertice,
) -> list[Vertice]:
    """Reconstruir una ruta alcanzable; devolver [] si no existe."""
    if origen not in anteriores or destino not in anteriores:
        raise ValueError("Origen y destino deben existir")
    camino: list[Vertice] = []
    actual: Vertice | None = destino
    while actual is not None:
        camino.append(actual)
        if actual == origen:
            return camino[::-1]
        actual = anteriores[actual]
    return []


if __name__ == "__main__":
    grafo = {
        "A": {"B": 3, "C": 6},
        "B": {"C": -2, "D": 4},
        "C": {"D": 1},
        "D": {},
        "E": {},
    }
    distancias, anteriores = caminos_cortos_dag(grafo, "A")
    assert distancias["D"] == 2
    assert distancias["E"] == inf
    assert reconstruir_camino(anteriores, "A", "D") == ["A", "B", "C", "D"]
    assert reconstruir_camino(anteriores, "A", "E") == []
    assert caminos_cortos_dag({"A": {}}, "A")[0] == {"A": 0.0}
    for invalido in (
        {"A": {"B": 1}, "B": {"A": 1}},
        {"A": {"B": 1}},
        {"A": {"A": 0}},
    ):
        try:
            caminos_cortos_dag(invalido, "A")
        except ValueError:
            pass
        else:
            raise AssertionError("Se esperaba rechazar el grafo inválido")
    print("Ejercicio 264: pruebas superadas.")
