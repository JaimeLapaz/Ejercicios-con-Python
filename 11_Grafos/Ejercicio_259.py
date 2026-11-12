"""Ejercicio 259 — Floyd-Warshall.

Enunciado:
    Encontrar las rutas más cortas entre todos los pares de vértices
    de un grafo ponderado.

Solución:
    Programación dinámica: para cada vértice intermedio k, comprobar
    si pasar por k mejora la distancia entre i y j. Reconstruimos rutas
    mediante una tabla del siguiente vértice y detectamos ciclos negativos.
"""
from math import inf, isfinite
from typing import Hashable, TypeVar

Vertice = TypeVar("Vertice", bound=Hashable)
Grafo = dict[Vertice, dict[Vertice, float]]


def floyd_warshall(grafo: Grafo[Vertice]) -> tuple[
    dict[Vertice, dict[Vertice, float]],
    dict[Vertice, dict[Vertice, Vertice | None]],
]:
    """Calcular distancias y siguientes pasos; O(V³) tiempo, O(V²) memoria."""
    # dict.fromkeys conserva el orden de inserción, incluso para destinos
    # que no aparecen como claves del grafo.
    vertices = list(dict.fromkeys(
        [*grafo, *(v for vecinos in grafo.values() for v in vecinos)]
    ))
    distancias = {u: {v: (0.0 if u == v else inf) for v in vertices}
                  for u in vertices}
    siguientes: dict[Vertice, dict[Vertice, Vertice | None]] = {
        u: {v: (u if u == v else None) for v in vertices}
        for u in vertices
    }
    for u, vecinos in grafo.items():
        for v, peso in vecinos.items():
            if not isfinite(peso):
                raise ValueError("Los pesos deben ser finitos")
            if peso < distancias[u][v]:
                distancias[u][v] = peso
                siguientes[u][v] = v

    for k in vertices:
        for i in vertices:
            if distancias[i][k] == inf:
                continue
            for j in vertices:
                if distancias[k][j] == inf:
                    continue
                alternativa = distancias[i][k] + distancias[k][j]
                if alternativa < distancias[i][j]:
                    distancias[i][j] = alternativa
                    siguientes[i][j] = siguientes[i][k]

    if any(distancias[v][v] < 0 for v in vertices):
        raise ValueError("El grafo contiene un ciclo de peso negativo")
    return distancias, siguientes


def reconstruir_camino(
    siguientes: dict[Vertice, dict[Vertice, Vertice | None]],
    origen: Vertice,
    destino: Vertice,
) -> list[Vertice]:
    """Obtener un camino mínimo, o [] si no existe."""
    if origen not in siguientes or destino not in siguientes[origen]:
        return []
    if siguientes[origen][destino] is None:
        return []
    ruta = [origen]
    actual = origen
    while actual != destino:
        paso = siguientes[actual][destino]
        if paso is None:
            return []
        actual = paso
        ruta.append(actual)
    return ruta


if __name__ == "__main__":
    grafo = {
        "A": {"B": 3, "C": 10},
        "B": {"C": -2},
        "C": {"D": 4},
        "D": {},
        "X": {},
    }
    distancias, siguientes = floyd_warshall(grafo)
    assert distancias["A"]["C"] == 1
    assert distancias["A"]["D"] == 5
    assert distancias["D"]["A"] == inf
    assert distancias["X"]["X"] == 0
    assert reconstruir_camino(siguientes, "A", "D") == ["A", "B", "C", "D"]
    assert reconstruir_camino(siguientes, "D", "A") == []
    assert reconstruir_camino(siguientes, "X", "X") == ["X"]
    try:
        floyd_warshall({"A": {"B": 1}, "B": {"A": -2}})
        assert False, "Se esperaba detectar un ciclo negativo"
    except ValueError:
        pass
    print("Ejercicio 259: pruebas superadas.")
