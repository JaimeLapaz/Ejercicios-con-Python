"""Enunciado:
256. Orden Topológico: encontrar un orden topológico válido en un
grafo dirigido acíclico (DAG).

Solución:
Aplicar el algoritmo de Kahn: calcular los grados de entrada,
procesar los vértices sin predecesores y reducir los grados de sus
sucesores. Si quedan vértices sin procesar, existe un ciclo.
"""
from __future__ import annotations

from collections import deque
from typing import Hashable, Iterable, Mapping

Vertice = Hashable
Grafo = Mapping[Vertice, Iterable[Vertice]]


def orden_topologico(grafo: Grafo) -> list[Vertice]:
    """Devuelve un orden válido; lanza ValueError si el grafo tiene ciclos."""
    adyacencia = {vertice: list(vecinos) for vertice, vecinos in grafo.items()}
    grados: dict[Vertice, int] = {vertice: 0 for vertice in adyacencia}

    # Incluir también los vértices que aparecen solo como destino.
    for vecinos in adyacencia.values():
        for vecino in vecinos:
            grados[vecino] = grados.get(vecino, 0) + 1

    pendientes = deque(v for v, grado in grados.items() if grado == 0)
    orden: list[Vertice] = []
    while pendientes:
        actual = pendientes.popleft()
        orden.append(actual)
        for vecino in adyacencia.get(actual, ()):
            grados[vecino] -= 1
            if grados[vecino] == 0:
                pendientes.append(vecino)

    if len(orden) != len(grados):
        raise ValueError("No existe orden topológico: el grafo contiene un ciclo")
    return orden


if __name__ == "__main__":
    tareas = {
        "comprar": ["cocinar"],
        "lavar": ["cocinar"],
        "cocinar": ["servir"],
        "descansar": [],
    }
    orden = orden_topologico(tareas)
    posiciones = {tarea: i for i, tarea in enumerate(orden)}
    assert set(orden) == set(tareas)
    assert all(posiciones[u] < posiciones[v]
               for u, vecinos in tareas.items() for v in vecinos)
    assert orden_topologico({}) == []
    assert orden_topologico({"A": ["B"]}) == ["A", "B"]
    try:
        orden_topologico({"A": ["B"], "B": ["A"]})
    except ValueError:
        pass
    else:
        raise AssertionError("Se debe detectar el ciclo")
    print("Orden topológico:", orden)
