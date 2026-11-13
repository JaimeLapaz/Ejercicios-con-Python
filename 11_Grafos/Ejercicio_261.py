"""Ejercicio 261 — Coloración de Grafos.

Enunciado:
    Implementa un algoritmo de coloración de grafos para asignar colores a
    los vértices de manera que ningún par de vértices adyacentes tenga el
    mismo color.

Solución:
    Aplicar DSATUR: escoger el vértice no coloreado con mayor saturación
    (número de colores distintos entre sus vecinos) y asignarle el menor
    color disponible. Es una heurística, no garantiza el mínimo cromático.
"""
from typing import Hashable, TypeVar

Vertice = TypeVar("Vertice", bound=Hashable)
Grafo = dict[Vertice, set[Vertice]]


def colorear_grafo(grafo: Grafo[Vertice]) -> dict[Vertice, int]:
    """Colorear un grafo no dirigido; colores numerados desde 0."""
    # Incorporar vértices que solo figuran como vecinos, sin alterar la entrada.
    adyacencia: Grafo[Vertice] = {u: set(vecinos) for u, vecinos in grafo.items()}
    for u, vecinos in grafo.items():
        if u in vecinos:
            raise ValueError("Un bucle impide una coloración propia")
        for v in vecinos:
            adyacencia.setdefault(v, set()).add(u)
    colores: dict[Vertice, int] = {}
    # El orden de inserción resuelve empates de forma reproducible.
    orden = {vertice: indice for indice, vertice in enumerate(adyacencia)}
    while len(colores) < len(adyacencia):
        pendientes = (v for v in adyacencia if v not in colores)
        vertice = max(
            pendientes,
            key=lambda v: (
                len({colores[w] for w in adyacencia[v] if w in colores}),
                len(adyacencia[v]),
                -orden[v],
            ),
        )
        ocupados = {colores[w] for w in adyacencia[vertice] if w in colores}
        color = 0
        while color in ocupados:
            color += 1
        colores[vertice] = color
    return colores


def coloracion_valida(
    grafo: Grafo[Vertice], colores: dict[Vertice, int]
) -> bool:
    """Comprobar que todos los extremos están coloreados de modo distinto."""
    vertices = set(grafo)
    vertices.update(v for vecinos in grafo.values() for v in vecinos)
    return set(colores) == vertices and all(
        u != v and colores[u] != colores[v]
        for u, vecinos in grafo.items() for v in vecinos
    )


if __name__ == "__main__":
    triangulo = {"A": {"B", "C"}, "B": {"A", "C"}, "C": {"A", "B"}}
    colores = colorear_grafo(triangulo)
    assert coloracion_valida(triangulo, colores)
    assert len(set(colores.values())) == 3

    bipartito = {1: {2, 4}, 2: {3}, 3: {4}, 4: set(), 5: set()}
    colores = colorear_grafo(bipartito)
    assert coloracion_valida(bipartito, colores)
    assert len(set(colores.values())) == 2
    assert colorear_grafo({}) == {}
    try:
        colorear_grafo({"A": {"A"}})
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba rechazar un bucle")
    print("Ejercicio 261: pruebas superadas.")
