"""Ejercicio 267 — Conectividad de Componentes.

Enunciado:
    Implementa un algoritmo para encontrar y contar las componentes
    conexas en un grafo no dirigido.

Solución:
    Recorrer el grafo con DFS iterativo desde cada vértice aún no
    visitado. Cada recorrido identifica una componente, incluyendo
    vértices aislados. Complejidad O(V + E).
"""
from collections.abc import Hashable, Iterable
from typing import TypeVar

Vertice = TypeVar("Vertice", bound=Hashable)


def componentes_conexas(
    grafo: dict[Vertice, Iterable[Vertice]],
) -> list[set[Vertice]]:
    """Obtener las componentes de un grafo no dirigido.

    Cada vecino debe figurar como vértice y las aristas deben ser
    simétricas. No se modifica la entrada.
    """
    vecinos = {vertice: set(adyacentes) for vertice, adyacentes in grafo.items()}
    for origen, adyacentes in vecinos.items():
        for destino in adyacentes:
            if destino not in vecinos or origen not in vecinos[destino]:
                raise ValueError("El grafo debe ser no dirigido y completo")

    visitados: set[Vertice] = set()
    resultado: list[set[Vertice]] = []
    for inicio in vecinos:
        if inicio in visitados:
            continue
        componente: set[Vertice] = set()
        pila = [inicio]
        visitados.add(inicio)
        while pila:
            actual = pila.pop()
            componente.add(actual)
            for destino in vecinos[actual]:
                if destino not in visitados:
                    visitados.add(destino)
                    pila.append(destino)
        resultado.append(componente)
    return resultado


def contar_componentes(grafo: dict[Vertice, Iterable[Vertice]]) -> int:
    """Contar las componentes conexas, incluidos los vértices aislados."""
    return len(componentes_conexas(grafo))


if __name__ == "__main__":
    grafo = {
        "A": ["B"],
        "B": ["A", "C"],
        "C": ["B"],
        "D": ["E"],
        "E": ["D"],
        "F": [],
    }
    componentes = componentes_conexas(grafo)
    assert {frozenset(c) for c in componentes} == {
        frozenset(("A", "B", "C")),
        frozenset(("D", "E")),
        frozenset(("F",)),
    }
    assert contar_componentes(grafo) == 3
    assert componentes_conexas({}) == []
    assert contar_componentes({"A": ["A"], "B": []}) == 2
    assert contar_componentes({"A": ["B"], "B": ["A"]}) == 1
    try:
        componentes_conexas({"A": ["B"], "B": []})
    except ValueError:
        pass
    else:
        raise AssertionError("Debe rechazarse un grafo asimétrico")
    print("Ejercicio 267: pruebas superadas")
