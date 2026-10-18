"""
Enunciado:

212. Árbol Binario de Búsqueda (BST): Crea una clase ArbolBST que
implemente un árbol binario de búsqueda y permita realizar inserciones
y búsquedas.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Nodo:
    """Nodo de un árbol binario de búsqueda."""

    valor: int
    izquierdo: Nodo | None = None
    derecho: Nodo | None = None


class ArbolBST:
    """BST de enteros: menores a la izquierda, mayores a la derecha.

    Los valores duplicados se ignoran. En el peor caso, buscar e insertar
    cuestan O(n), y en un árbol equilibrado O(log n).
    """

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    def insertar(self, valor: int) -> bool:
        """Inserta el valor y devuelve False si ya existía."""
        if self.raiz is None:
            self.raiz = Nodo(valor)
            return True

        actual = self.raiz
        while True:
            if valor == actual.valor:
                return False
            if valor < actual.valor:
                if actual.izquierdo is None:
                    actual.izquierdo = Nodo(valor)
                    return True
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    actual.derecho = Nodo(valor)
                    return True
                actual = actual.derecho

    def buscar(self, valor: int) -> Nodo | None:
        """Devuelve el nodo que contiene el valor, o None."""
        actual = self.raiz
        while actual is not None:
            if valor == actual.valor:
                return actual
            actual = actual.izquierdo if valor < actual.valor else actual.derecho
        return None

    def recorrido_en_orden(self) -> list[int]:
        """Obtiene los valores ordenados ascendentemente."""
        resultado: list[int] = []
        pendientes: list[Nodo] = []
        actual = self.raiz
        while pendientes or actual is not None:
            while actual is not None:
                pendientes.append(actual)
                actual = actual.izquierdo
            actual = pendientes.pop()
            resultado.append(actual.valor)
            actual = actual.derecho
        return resultado


if __name__ == "__main__":
    arbol = ArbolBST()
    assert arbol.buscar(5) is None
    assert arbol.recorrido_en_orden() == []
    for valor in (8, 3, 10, 1, 6, 14, 4, 7, 13):
        assert arbol.insertar(valor)
    assert not arbol.insertar(6)
    assert arbol.buscar(7) is not None and arbol.buscar(7).valor == 7
    assert arbol.buscar(9) is None
    assert arbol.recorrido_en_orden() == [1, 3, 4, 6, 7, 8, 10, 13, 14]
    print("Ejercicio 212: pruebas superadas")
