"""
Enunciado:

213. Árbol AVL: Diseña una clase ArbolAVL que implemente un árbol AVL
    y permita realizar inserciones y eliminaciones manteniendo el equilibrio.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Nodo:
    """Nodo de un AVL; la altura de una hoja es 1."""

    valor: int
    izquierdo: Nodo | None = None
    derecho: Nodo | None = None
    altura: int = 1


class ArbolAVL:
    """Árbol binario de búsqueda autoequilibrado, sin valores duplicados.

    La inserción, eliminación y búsqueda cuestan O(log n).
    """

    def __init__(self) -> None:
        self.raiz: Nodo | None = None

    @staticmethod
    def _altura(nodo: Nodo | None) -> int:
        return nodo.altura if nodo is not None else 0

    @classmethod
    def _actualizar_altura(cls, nodo: Nodo) -> None:
        nodo.altura = 1 + max(cls._altura(nodo.izquierdo), cls._altura(nodo.derecho))

    @classmethod
    def _balance(cls, nodo: Nodo) -> int:
        return cls._altura(nodo.izquierdo) - cls._altura(nodo.derecho)

    @classmethod
    def _rotar_derecha(cls, raiz: Nodo) -> Nodo:
        nueva_raiz = raiz.izquierdo
        assert nueva_raiz is not None
        raiz.izquierdo = nueva_raiz.derecho
        nueva_raiz.derecho = raiz
        cls._actualizar_altura(raiz)
        cls._actualizar_altura(nueva_raiz)
        return nueva_raiz

    @classmethod
    def _rotar_izquierda(cls, raiz: Nodo) -> Nodo:
        nueva_raiz = raiz.derecho
        assert nueva_raiz is not None
        raiz.derecho = nueva_raiz.izquierdo
        nueva_raiz.izquierdo = raiz
        cls._actualizar_altura(raiz)
        cls._actualizar_altura(nueva_raiz)
        return nueva_raiz

    @classmethod
    def _equilibrar(cls, nodo: Nodo) -> Nodo:
        cls._actualizar_altura(nodo)
        balance = cls._balance(nodo)
        if balance > 1:
            assert nodo.izquierdo is not None
            if cls._balance(nodo.izquierdo) < 0:
                nodo.izquierdo = cls._rotar_izquierda(nodo.izquierdo)
            return cls._rotar_derecha(nodo)
        if balance < -1:
            assert nodo.derecho is not None
            if cls._balance(nodo.derecho) > 0:
                nodo.derecho = cls._rotar_derecha(nodo.derecho)
            return cls._rotar_izquierda(nodo)
        return nodo

    @classmethod
    def _insertar(cls, nodo: Nodo | None, valor: int) -> tuple[Nodo, bool]:
        if nodo is None:
            return Nodo(valor), True
        if valor == nodo.valor:
            return nodo, False
        if valor < nodo.valor:
            nodo.izquierdo, insertado = cls._insertar(nodo.izquierdo, valor)
        else:
            nodo.derecho, insertado = cls._insertar(nodo.derecho, valor)
        return cls._equilibrar(nodo), insertado

    def insertar(self, valor: int) -> bool:
        """Inserta un valor; devuelve False si ya estaba presente."""
        self.raiz, insertado = self._insertar(self.raiz, valor)
        return insertado

    @classmethod
    def _eliminar(cls, nodo: Nodo | None, valor: int) -> tuple[Nodo | None, bool]:
        if nodo is None:
            return None, False
        if valor < nodo.valor:
            nodo.izquierdo, eliminado = cls._eliminar(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho, eliminado = cls._eliminar(nodo.derecho, valor)
        else:
            eliminado = True
            if nodo.izquierdo is None:
                return nodo.derecho, True
            if nodo.derecho is None:
                return nodo.izquierdo, True
            sucesor = nodo.derecho
            while sucesor.izquierdo is not None:
                sucesor = sucesor.izquierdo
            nodo.valor = sucesor.valor
            nodo.derecho, _ = cls._eliminar(nodo.derecho, sucesor.valor)
        return cls._equilibrar(nodo), eliminado

    def eliminar(self, valor: int) -> bool:
        """Elimina un valor; devuelve False si no existe."""
        self.raiz, eliminado = self._eliminar(self.raiz, valor)
        return eliminado

    def buscar(self, valor: int) -> bool:
        """Comprueba si el valor pertenece al árbol."""
        actual = self.raiz
        while actual is not None:
            if valor == actual.valor:
                return True
            actual = actual.izquierdo if valor < actual.valor else actual.derecho
        return False

    def recorrido_en_orden(self) -> list[int]:
        """Devuelve los valores de menor a mayor."""
        resultado: list[int] = []

        def recorrer(nodo: Nodo | None) -> None:
            if nodo is not None:
                recorrer(nodo.izquierdo)
                resultado.append(nodo.valor)
                recorrer(nodo.derecho)

        recorrer(self.raiz)
        return resultado


if __name__ == "__main__":
    for valores in ((30, 20, 10), (10, 20, 30), (30, 10, 20), (10, 30, 20)):
        arbol = ArbolAVL()
        for valor in valores:
            assert arbol.insertar(valor)
        assert arbol.raiz is not None and arbol.raiz.valor == 20
        assert arbol.recorrido_en_orden() == [10, 20, 30]
        assert not arbol.insertar(20)

    arbol = ArbolAVL()
    for valor in (40, 20, 60, 10, 30, 50, 70, 25, 35):
        arbol.insertar(valor)
    assert arbol.eliminar(20)  # Nodo con dos hijos.
    assert arbol.eliminar(10)  # Hoja.
    assert not arbol.eliminar(999)
    assert not arbol.buscar(20) and arbol.buscar(25)
    assert arbol.recorrido_en_orden() == [25, 30, 35, 40, 50, 60, 70]
    print("Ejercicio 213: pruebas superadas")
