"""Ejercicio 262 — Algoritmo de Kruskal.

Enunciado:
    Desarrolla el algoritmo de Kruskal para encontrar el árbol de expansión
    mínima en un grafo ponderado con conjuntos disjuntos.

Solución:
    Ordenar las aristas por peso y añadir cada una si conecta componentes
    diferentes. La estructura de conjuntos disjuntos (union-find) utiliza
    compresión de caminos y unión por tamaño. Si el grafo no es conexo,
    devolver el bosque de expansión mínima.
"""
from math import isfinite
from typing import Hashable, TypeVar

Vertice = TypeVar("Vertice", bound=Hashable)
Arista = tuple[Vertice, Vertice, float]


class ConjuntosDisjuntos:
    """Mantener componentes mediante compresión de caminos y unión por tamaño."""

    def __init__(self, vertices: set[Vertice]) -> None:
        self.padre = {v: v for v in vertices}
        self.tamano = {v: 1 for v in vertices}

    def encontrar(self, vertice: Vertice) -> Vertice:
        """Encontrar la raíz de la componente."""
        if self.padre[vertice] != vertice:
            self.padre[vertice] = self.encontrar(self.padre[vertice])
        return self.padre[vertice]

    def unir(self, primero: Vertice, segundo: Vertice) -> bool:
        """Unir componentes; devolver False si ya estaban conectadas."""
        raiz_a, raiz_b = self.encontrar(primero), self.encontrar(segundo)
        if raiz_a == raiz_b:
            return False
        if self.tamano[raiz_a] < self.tamano[raiz_b]:
            raiz_a, raiz_b = raiz_b, raiz_a
        self.padre[raiz_b] = raiz_a
        self.tamano[raiz_a] += self.tamano[raiz_b]
        return True


def kruskal(
    vertices: set[Vertice], aristas: list[Arista[Vertice]]
) -> tuple[float, list[Arista[Vertice]]]:
    """Calcular bosque mínimo en O(E log E) tiempo."""
    for origen, destino, peso in aristas:
        if origen not in vertices or destino not in vertices:
            raise ValueError("Los extremos deben pertenecer al grafo")
        if not isfinite(peso):
            raise ValueError("Los pesos deben ser finitos")

    componentes = ConjuntosDisjuntos(vertices)
    seleccionadas: list[Arista[Vertice]] = []
    total = 0.0
    # sorted es estable: los empates respetan el orden de entrada.
    for origen, destino, peso in sorted(aristas, key=lambda arista: arista[2]):
        if componentes.unir(origen, destino):
            seleccionadas.append((origen, destino, peso))
            total += peso
    return total, seleccionadas


if __name__ == "__main__":
    vertices = {"A", "B", "C", "D"}
    aristas = [
        ("A", "B", 1), ("B", "C", 2), ("A", "C", 4),
        ("C", "D", 3), ("A", "D", 10),
    ]
    peso, arbol = kruskal(vertices, aristas)
    assert peso == 6
    assert len(arbol) == len(vertices) - 1
    assert kruskal({"A", "B", "C"}, [("A", "B", -2)])[0] == -2
    assert kruskal(set(), []) == (0.0, [])
    try:
        kruskal({"A"}, [("A", "B", 1)])
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba rechazar un vértice desconocido")
    print("Ejercicio 262: pruebas superadas.")
