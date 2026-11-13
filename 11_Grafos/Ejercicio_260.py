"""Ejercicio 260 — Flujo Máximo.

Enunciado:
    Diseña un algoritmo para encontrar el flujo máximo en un grafo de
    flujo con capacidad en aristas.

Solución:
    Edmonds-Karp utiliza BFS sobre la red residual para encontrar caminos
    aumentantes. Cada aumento actualiza las capacidades en ambos sentidos,
    incluso cuando es necesario deshacer parte de un flujo anterior.
"""
from collections import deque
from math import isfinite
from typing import Hashable, TypeVar

Vertice = TypeVar("Vertice", bound=Hashable)
Red = dict[Vertice, dict[Vertice, float]]


def flujo_maximo(
    red: Red[Vertice], fuente: Vertice, sumidero: Vertice
) -> tuple[float, dict[Vertice, dict[Vertice, float]]]:
    """Devolver valor máximo y flujo por arista; O(V * E²) tiempo."""
    vertices = set(red)
    for vecinos in red.values():
        vertices.update(vecinos)
        for capacidad in vecinos.values():
            if not isfinite(capacidad) or capacidad < 0:
                raise ValueError("Las capacidades deben ser finitas y no negativas")
    if fuente not in vertices or sumidero not in vertices:
        raise ValueError("Fuente y sumidero deben existir en la red")
    if fuente == sumidero:
        raise ValueError("Fuente y sumidero deben ser distintos")

    # La matriz residual admite aristas antiparalelas.
    residual: dict[Vertice, dict[Vertice, float]] = {v: {} for v in vertices}
    for u, vecinos in red.items():
        for v, capacidad in vecinos.items():
            if u == v:
                continue  # Los bucles no contribuyen al flujo fuente-sumidero.
            residual[u][v] = residual[u].get(v, 0.0) + capacidad
            residual[v].setdefault(u, 0.0)

    total = 0.0
    while True:
        padres: dict[Vertice, Vertice | None] = {fuente: None}
        cola = deque([fuente])
        while cola and sumidero not in padres:
            u = cola.popleft()
            for v, disponible in residual[u].items():
                if disponible > 0 and v not in padres:
                    padres[v] = u
                    cola.append(v)
        if sumidero not in padres:
            break

        cuello = float("inf")
        actual = sumidero
        while actual != fuente:
            anterior = padres[actual]
            assert anterior is not None
            cuello = min(cuello, residual[anterior][actual])
            actual = anterior
        actual = sumidero
        while actual != fuente:
            anterior = padres[actual]
            assert anterior is not None
            residual[anterior][actual] -= cuello
            residual[actual][anterior] = residual[actual].get(anterior, 0.0) + cuello
            actual = anterior
        total += cuello

    # Para aristas antiparalelas, el flujo neto puede ser negativo.
    # Repartirlo entre las aristas originales respetando sus capacidades.
    flujo: dict[Vertice, dict[Vertice, float]] = {
        u: {v: 0.0 for v in vecinos} for u, vecinos in red.items()
    }
    procesados: set[frozenset[Vertice]] = set()
    for u, vecinos in red.items():
        for v in vecinos:
            if u == v:
                continue
            par = frozenset((u, v))
            if par in procesados:
                continue
            procesados.add(par)
            capacidad_uv = red.get(u, {}).get(v, 0.0)
            capacidad_vu = red.get(v, {}).get(u, 0.0)
            neto = capacidad_uv - residual[u].get(v, 0.0)
            if neto >= 0:
                flujo[u][v] = min(neto, capacidad_uv)
            elif v in flujo and u in flujo[v]:
                flujo[v][u] = min(-neto, capacidad_vu)
    return total, flujo


if __name__ == "__main__":
    red = {
        "s": {"a": 16, "b": 13},
        "a": {"b": 10, "c": 12},
        "b": {"a": 4, "d": 14},
        "c": {"b": 9, "t": 20},
        "d": {"c": 7, "t": 4},
        "t": {},
    }
    valor, flujo = flujo_maximo(red, "s", "t")
    assert valor == 23
    assert sum(flujo["s"].values()) == 23
    assert sum(flujo[u].get("t", 0) for u in flujo) == 23
    assert all(0 <= f <= red[u][v] for u, vecinos in flujo.items()
               for v, f in vecinos.items())
    assert flujo_maximo({"s": {}, "t": {}}, "s", "t")[0] == 0
    try:
        flujo_maximo({"s": {"t": -1}, "t": {}}, "s", "t")
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba rechazar capacidad negativa")
    print("Ejercicio 260: pruebas superadas.")
