"""
Enunciado:

209. Altura de un Árbol: Escribe una función que calcule la altura de
un árbol binario.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Nodo:
    """Nodo de un árbol binario."""

    valor: int
    izquierdo: Nodo | None = None
    derecho: Nodo | None = None


def altura_arbol(raiz: Nodo | None) -> int:
    """Calcula la altura en número de nodos (árbol vacío: 0).

    Un árbol de un solo nodo tiene altura 1; el cálculo es O(n).
    """
    if raiz is None:
        return 0
    return 1 + max(altura_arbol(raiz.izquierdo), altura_arbol(raiz.derecho))


if __name__ == "__main__":
    assert altura_arbol(None) == 0
    hoja = Nodo(10)
    assert altura_arbol(hoja) == 1
    equilibrado = Nodo(1, Nodo(2, Nodo(4), Nodo(5)), Nodo(3))
    assert altura_arbol(equilibrado) == 3
    descompensado = Nodo(1, Nodo(2, Nodo(3, Nodo(4))))
    assert altura_arbol(descompensado) == 4
    print("Ejercicio 209: pruebas superadas")
