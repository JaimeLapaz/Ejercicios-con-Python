"""
Enunciado:

234. Recorrido de Grafo: Diseña una función recursiva que realice un
    recorrido en profundidad (DFS) de un grafo.

Solución:
"""

from __future__ import annotations

from collections.abc import Collection, Hashable, Mapping
from typing import TypeVar

Vertice = TypeVar("Vertice", bound=Hashable)


def recorrido_dfs(
    grafo: Mapping[Vertice, Collection[Vertice]], inicio: Vertice
) -> list[Vertice]:
    """Recorre en profundidad desde ``inicio`` y devuelve el orden de visita.

    El grafo se representa con listas de adyacencia: cada vértice tiene
    una colección de vecinos. Puede ser dirigido o no dirigido. Los
    vecinos que no figuran como claves se tratan como vértices sin salidas.
    Se respeta el orden de vecinos y no se modifica el grafo.

    Tiempo O(V + E), espacio O(V) entre visitados y pila de recursión.
    En grafos muy profundos puede alcanzarse el límite de recursión.
    """
    if inicio not in grafo:
        raise ValueError("El vértice inicial debe figurar en el grafo")

    visitados: set[Vertice] = set()
    orden: list[Vertice] = []

    def visitar(vertice: Vertice) -> None:
        if vertice in visitados:
            return
        visitados.add(vertice)  # Marcar antes de explorar evita ciclos.
        orden.append(vertice)
        for vecino in grafo.get(vertice, ()):
            visitar(vecino)

    visitar(inicio)
    return orden


def camino_dfs(
    grafo: Mapping[Vertice, Collection[Vertice]],
    inicio: Vertice,
    destino: Vertice,
) -> list[Vertice] | None:
    """Encuentra recursivamente un camino de inicio a destino, si existe.

    Devuelve None si el destino no es alcanzable. Los vértices se marcan
    al visitarlos y se retiran del camino al retroceder (backtracking).
    """
    if inicio not in grafo:
        raise ValueError("El vértice inicial debe figurar en el grafo")

    visitados: set[Vertice] = set()
    camino: list[Vertice] = []

    def buscar(vertice: Vertice) -> bool:
        if vertice in visitados:
            return False
        visitados.add(vertice)
        camino.append(vertice)
        if vertice == destino:
            return True
        for vecino in grafo.get(vertice, ()):
            if buscar(vecino):
                return True
        camino.pop()
        return False

    return camino if buscar(inicio) else None


if __name__ == "__main__":
    ejemplo = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": ["A"],  # Ciclo: D -> A.
        "E": ["C"],
        "F": [],
        "G": [],  # Componente desconectada.
    }
    copia = {vertice: vecinos.copy() for vertice, vecinos in ejemplo.items()}
    assert recorrido_dfs(ejemplo, "A") == ["A", "B", "D", "E", "C", "F"]
    assert recorrido_dfs(ejemplo, "G") == ["G"]
    assert camino_dfs(ejemplo, "A", "F") == ["A", "B", "E", "C", "F"]
    assert camino_dfs(ejemplo, "A", "G") is None
    assert camino_dfs(ejemplo, "A", "A") == ["A"]
    assert recorrido_dfs({1: [2]}, 1) == [1, 2]  # Vértice sumidero implícito.
    assert camino_dfs({1: [2]}, 1, 2) == [1, 2]
    assert ejemplo == copia

    for funcion, argumentos in (
        (recorrido_dfs, ({}, "A")),
        (camino_dfs, (ejemplo, "Z", "A")),
    ):
        try:
            funcion(*argumentos)
        except ValueError:
            pass
        else:
            raise AssertionError("Se esperaba ValueError")

    print("Ejercicio 234: pruebas superadas")
