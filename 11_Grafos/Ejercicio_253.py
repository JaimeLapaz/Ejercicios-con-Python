"""Enunciado:
253. Ciclo en Grafo: determinar si un grafo contiene algún ciclo.

Solución:
En un grafo no dirigido, recorrer cada componente mediante DFS y
detectar aristas hacia vértices visitados distintos del padre.
Los bucles propios también constituyen ciclos.
"""
from __future__ import annotations

from typing import Hashable, Iterable, Mapping


def contiene_ciclo(grafo: Mapping[Hashable, Iterable[Hashable]]) -> bool:
    """Detecta ciclos en un grafo no dirigido, incluso desconectado."""
    adyacencia: dict[Hashable, set[Hashable]] = {
        vertice: set(vecinos) for vertice, vecinos in grafo.items()
    }
    for vertice, vecinos in list(adyacencia.items()):
        for vecino in vecinos:
            adyacencia.setdefault(vecino, set()).add(vertice)

    visitados: set[Hashable] = set()
    for inicio in adyacencia:
        if inicio in visitados:
            continue
        visitados.add(inicio)
        pila: list[tuple[Hashable, Hashable | None]] = [(inicio, None)]
        while pila:
            actual, padre = pila.pop()
            for vecino in adyacencia[actual]:
                if vecino == actual:
                    return True
                if vecino not in visitados:
                    visitados.add(vecino)
                    pila.append((vecino, actual))
                elif vecino != padre:
                    return True
    return False


if __name__ == "__main__":
    assert not contiene_ciclo({"A": ["B"], "B": ["C"], "C": []})
    assert contiene_ciclo({"A": ["B", "C"], "B": ["C"], "C": []})
    assert contiene_ciclo({"A": ["A"]})
    assert not contiene_ciclo({"A": [], "B": []})
    print("Ciclo detectado:", contiene_ciclo({"A": ["B"], "B": ["A"]}))
