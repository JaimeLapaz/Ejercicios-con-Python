"""Ejercicio 265 — Flujo de Redes.

Enunciado:
    Desarrolla un algoritmo para calcular el flujo máximo en una red
    de flujo con múltiples fuentes y sumideros.

Solución:
    Conectar una superfuente a todas las fuentes y cada sumidero a
    un supersumidero. Ejecutar Edmonds-Karp (Ford-Fulkerson con BFS)
    sobre una red residual. Las capacidades auxiliares se limitan a
    la suma de capacidades originales. Complejidad O(V * E**2).
"""
from collections import deque
from math import isfinite
from typing import Hashable, TypeVar

Vertice = TypeVar("Vertice", bound=Hashable)
Red = dict[Vertice, dict[Vertice, float]]


def flujo_maximo_multiple(
    red: Red[Vertice],
    fuentes: set[Vertice],
    sumideros: set[Vertice],
) -> tuple[float, dict[tuple[Vertice, Vertice], float]]:
    """Calcular flujo máximo y flujo neto por arista original.

    No se admiten aristas antiparalelas: así el flujo reportado por
    arista es inequívoco. Se admiten capacidades cero.
    """
    if not fuentes or not sumideros:
        raise ValueError("Se necesita al menos una fuente y un sumidero")
    if fuentes & sumideros:
        raise ValueError("Fuentes y sumideros deben ser disjuntos")
    if not fuentes <= red.keys() or not sumideros <= red.keys():
        raise ValueError("Las fuentes y sumideros deben existir en la red")

    capacidades: dict[tuple[Vertice, Vertice], float] = {}
    total = 0.0
    for origen, vecinos in red.items():
        for destino, capacidad in vecinos.items():
            if destino not in red:
                raise ValueError("Todos los destinos deben existir en la red")
            if (not isinstance(capacidad, (int, float))
                    or not isfinite(capacidad) or capacidad < 0):
                raise ValueError("Las capacidades deben ser finitas y no negativas")
            if origen == destino:
                raise ValueError("No se admiten bucles")
            if origen in red[destino]:
                raise ValueError("No se admiten aristas antiparalelas")
            capacidades[(origen, destino)] = float(capacidad)
            total += capacidad

    # Los centinelas únicos evitan colisiones con nombres de vértices.
    superfuente, supersumidero = object(), object()
    residual: dict[object, dict[object, float]] = {
        v: {} for v in red
    }
    residual[superfuente] = {}
    residual[supersumidero] = {}

    def agregar(origen: object, destino: object, capacidad: float) -> None:
        residual[origen][destino] = capacidad
        residual[destino].setdefault(origen, 0.0)

    for (origen, destino), capacidad in capacidades.items():
        agregar(origen, destino, capacidad)
    for fuente in fuentes:
        agregar(superfuente, fuente, total)
    for sumidero in sumideros:
        agregar(sumidero, supersumidero, total)

    maximo = 0.0
    while True:
        padres: dict[object, object | None] = {superfuente: None}
        cola = deque([superfuente])
        while cola and supersumidero not in padres:
            actual = cola.popleft()
            for vecino, capacidad in residual[actual].items():
                if capacidad > 0 and vecino not in padres:
                    padres[vecino] = actual
                    cola.append(vecino)
                    if vecino is supersumidero:
                        break
        if supersumidero not in padres:
            break

        aumento = float("inf")
        actual = supersumidero
        while actual is not superfuente:
            anterior = padres[actual]
            assert anterior is not None
            aumento = min(aumento, residual[anterior][actual])
            actual = anterior

        actual = supersumidero
        while actual is not superfuente:
            anterior = padres[actual]
            assert anterior is not None
            residual[anterior][actual] -= aumento
            residual[actual][anterior] += aumento
            actual = anterior
        maximo += aumento

    flujos = {
        arista: capacidad - residual[arista[0]][arista[1]]
        for arista, capacidad in capacidades.items()
    }
    return maximo, flujos


if __name__ == "__main__":
    red = {
        "S1": {"A": 5},
        "S2": {"A": 4, "B": 3},
        "A": {"T1": 4, "B": 3},
        "B": {"T2": 6},
        "T1": {},
        "T2": {},
    }
    maximo, flujos = flujo_maximo_multiple(red, {"S1", "S2"}, {"T1", "T2"})
    assert maximo == 10
    assert sum(flujos[("S1", v)] for v in red["S1"]) + sum(
        flujos[("S2", v)] for v in red["S2"]
    ) == maximo
    assert flujo_maximo_multiple({"S": {}, "T": {}}, {"S"}, {"T"})[0] == 0
    assert flujo_maximo_multiple({"S": {"T": 2}, "T": {}}, {"S"}, {"T"})[0] == 2
    for invalida in (
        {"S": {"T": -1}, "T": {}},
        {"S": {"T": 1}, "T": {"S": 2}},
    ):
        try:
            flujo_maximo_multiple(invalida, {"S"}, {"T"})
        except ValueError:
            pass
        else:
            raise AssertionError("Se esperaba rechazar la red inválida")
    print("Ejercicio 265: pruebas superadas.")
