"""Ejercicio 266 — Ciclo Euleriano.

Enunciado:
    Diseña una función que determine si un grafo contiene un ciclo euleriano
    (un ciclo que visita cada arista exactamente una vez).

Solución:
    En un grafo no dirigido, los vértices con aristas deben formar una sola
    componente conexa y todos sus grados deben ser pares. Se comprueban
    ambas condiciones y se construye el ciclo con Hierholzer en O(V + E).
    La lista de adyacencia admite aristas paralelas y bucles (cada bucle
    aparece dos veces en la lista de su vértice).
"""
from collections import Counter
from collections.abc import Hashable, Iterable
from typing import TypeVar

Vertice = TypeVar("Vertice", bound=Hashable)


def ciclo_euleriano(
    grafo: dict[Vertice, Iterable[Vertice]],
) -> list[Vertice] | None:
    """Devolver un ciclo euleriano o None si no existe.

    Un grafo sin aristas tiene el ciclo vacío. Se rechazan listas de
    adyacencia asimétricas o bucles representados una sola vez.
    No se modifica el grafo de entrada.
    """
    adyacencia = {vertice: list(vecinos) for vertice, vecinos in grafo.items()}
    cuentas = {vertice: Counter(vecinos) for vertice, vecinos in adyacencia.items()}

    for origen, vecinos in cuentas.items():
        for destino, cantidad in vecinos.items():
            if destino not in cuentas:
                raise ValueError("Todos los vértices vecinos deben existir")
            if cuentas[destino][origen] != cantidad:
                raise ValueError("Cada arista debe figurar en ambos extremos")
        if vecinos[origen] % 2:
            raise ValueError("Cada bucle debe aparecer dos veces")

    activos = {vertice for vertice, vecinos in adyacencia.items() if vecinos}
    if not activos:
        return []
    if any(len(adyacencia[vertice]) % 2 for vertice in activos):
        return None

    inicio = next(iter(activos))
    visitados = {inicio}
    pendientes = [inicio]
    while pendientes:
        actual = pendientes.pop()
        for vecino in adyacencia[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                pendientes.append(vecino)
    if visitados != activos:
        return None

    # Asignar un identificador a cada arista no dirigida, incluso
    # cuando hay aristas paralelas o bucles.
    aristas: dict[Vertice, list[tuple[Vertice, int]]] = {
        vertice: [] for vertice in grafo
    }
    restantes = {vertice: Counter(vecinos) for vertice, vecinos in adyacencia.items()}
    identificador = 0
    for origen in grafo:
        for destino in adyacencia[origen]:
            if restantes[origen][destino] == 0:
                continue
            if origen == destino:
                restantes[origen][destino] -= 2
            else:
                restantes[origen][destino] -= 1
                restantes[destino][origen] -= 1
            aristas[origen].append((destino, identificador))
            aristas[destino].append((origen, identificador))
            identificador += 1

    pila = [inicio]
    recorrido: list[Vertice] = []
    usadas: set[int] = set()
    while pila:
        actual = pila[-1]
        while aristas[actual] and aristas[actual][-1][1] in usadas:
            aristas[actual].pop()
        if not aristas[actual]:
            recorrido.append(pila.pop())
        else:
            vecino, indice = aristas[actual].pop()
            usadas.add(indice)
            pila.append(vecino)

    recorrido.reverse()
    assert len(usadas) == identificador
    assert len(recorrido) == identificador + 1
    return recorrido


if __name__ == "__main__":
    triangulo = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}
    ciclo = ciclo_euleriano(triangulo)
    assert ciclo is not None and ciclo[0] == ciclo[-1]
    assert len(ciclo) == 4
    assert {frozenset((a, b)) for a, b in zip(ciclo, ciclo[1:])} == {
        frozenset(("A", "B")),
        frozenset(("B", "C")),
        frozenset(("A", "C")),
    }
    assert ciclo_euleriano({"A": ["B"], "B": ["A"]}) is None
    assert ciclo_euleriano({"A": ["A", "A"]}) == ["A", "A"]
    assert len(ciclo_euleriano({"A": ["B", "B"], "B": ["A", "A"]})) == 3
    assert ciclo_euleriano({"A": [], "B": []}) == []
    assert ciclo_euleriano({"A": ["A", "A"], "B": ["B", "B"]}) is None
    try:
        ciclo_euleriano({"A": ["B"], "B": []})
    except ValueError:
        pass
    else:
        raise AssertionError("Debe rechazarse un grafo asimétrico")
    print("Ejercicio 266: pruebas superadas")
