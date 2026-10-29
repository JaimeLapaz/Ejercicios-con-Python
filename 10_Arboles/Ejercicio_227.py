"""
Enunciado:

227. Árbol B+: Diseña una clase ArbolBPlus que implemente un árbol B+
    y permita realizar inserciones, eliminaciones y búsquedas eficientes
    en un conjunto ordenado de datos.

Solución:
"""

from __future__ import annotations

from bisect import bisect_left, bisect_right
from dataclasses import dataclass, field


@dataclass(eq=False)
class NodoBPlus:
    """Nodo del índice; los datos solo se guardan en las hojas."""

    hoja: bool = True
    claves: list[int] = field(default_factory=list)
    hijos: list[NodoBPlus] = field(default_factory=list)
    siguiente: NodoBPlus | None = None


class ArbolBPlus:
    """Árbol B+ de enteros únicos, con hojas enlazadas en orden.

    ``orden`` es el máximo de hijos de un nodo interno; las hojas guardan
    hasta ``orden - 1`` claves. Las búsquedas, inserciones y eliminaciones
    cuestan O(log n) para un orden fijo; los recorridos por rango son
    O(log n + k), donde k es el número de resultados.
    """

    def __init__(self, orden: int = 4) -> None:
        if orden < 3:
            raise ValueError("El orden debe ser al menos 3")
        self.orden = orden
        self.raiz = NodoBPlus()
        self._cantidad = 0

    @staticmethod
    def _minima(nodo: NodoBPlus) -> int:
        """Primera clave de un subárbol no vacío."""
        while not nodo.hoja:
            nodo = nodo.hijos[0]
        return nodo.claves[0]

    @classmethod
    def _actualizar_separadores(cls, nodo: NodoBPlus) -> None:
        if not nodo.hoja:
            nodo.claves = [cls._minima(hijo) for hijo in nodo.hijos[1:]]

    def _hoja_para(self, clave: int) -> NodoBPlus:
        nodo = self.raiz
        while not nodo.hoja:
            nodo = nodo.hijos[bisect_right(nodo.claves, clave)]
        return nodo

    def buscar(self, clave: int) -> bool:
        """Comprueba si una clave existe sin recorrer otras hojas."""
        hoja = self._hoja_para(clave)
        indice = bisect_left(hoja.claves, clave)
        return indice < len(hoja.claves) and hoja.claves[indice] == clave

    def _insertar(self, nodo: NodoBPlus, clave: int) -> tuple[bool, NodoBPlus | None]:
        if nodo.hoja:
            indice = bisect_left(nodo.claves, clave)
            if indice < len(nodo.claves) and nodo.claves[indice] == clave:
                return False, None
            nodo.claves.insert(indice, clave)
            if len(nodo.claves) < self.orden:
                return True, None
            corte = len(nodo.claves) // 2
            derecha = NodoBPlus(claves=nodo.claves[corte:], siguiente=nodo.siguiente)
            nodo.claves = nodo.claves[:corte]
            nodo.siguiente = derecha
            return True, derecha

        indice = bisect_right(nodo.claves, clave)
        insertado, nuevo = self._insertar(nodo.hijos[indice], clave)
        if not insertado:
            return False, None
        if nuevo is not None:
            nodo.hijos.insert(indice + 1, nuevo)
        self._actualizar_separadores(nodo)
        if len(nodo.hijos) <= self.orden:
            return True, None
        corte = len(nodo.hijos) // 2
        derecha = NodoBPlus(hoja=False, hijos=nodo.hijos[corte:])
        nodo.hijos = nodo.hijos[:corte]
        self._actualizar_separadores(nodo)
        self._actualizar_separadores(derecha)
        return True, derecha

    def insertar(self, clave: int) -> bool:
        """Inserta una clave; devuelve False si ya estaba presente."""
        insertado, derecha = self._insertar(self.raiz, clave)
        if not insertado:
            return False
        if derecha is not None:
            self.raiz = NodoBPlus(hoja=False, hijos=[self.raiz, derecha])
            self._actualizar_separadores(self.raiz)
        self._cantidad += 1
        return True

    def _minimo_ocupacion(self, nodo: NodoBPlus) -> int:
        if nodo.hoja:
            return self.orden // 2  # ceil((orden - 1) / 2)
        return (self.orden + 1) // 2  # ceil(orden / 2) hijos

    def _ocupacion(self, nodo: NodoBPlus) -> int:
        return len(nodo.claves) if nodo.hoja else len(nodo.hijos)

    def _reparar(self, padre: NodoBPlus, indice: int) -> None:
        """Corrige el déficit de un hijo mediante préstamo o fusión."""
        hijo = padre.hijos[indice]
        minimo = self._minimo_ocupacion(hijo)
        if self._ocupacion(hijo) >= minimo:
            return

        if indice > 0:
            izquierdo = padre.hijos[indice - 1]
            if self._ocupacion(izquierdo) > minimo:
                if hijo.hoja:
                    hijo.claves.insert(0, izquierdo.claves.pop())
                else:
                    hijo.hijos.insert(0, izquierdo.hijos.pop())
                    self._actualizar_separadores(izquierdo)
                    self._actualizar_separadores(hijo)
                return

        if indice + 1 < len(padre.hijos):
            derecho = padre.hijos[indice + 1]
            if self._ocupacion(derecho) > minimo:
                if hijo.hoja:
                    hijo.claves.append(derecho.claves.pop(0))
                else:
                    hijo.hijos.append(derecho.hijos.pop(0))
                    self._actualizar_separadores(derecho)
                    self._actualizar_separadores(hijo)
                return

        if indice > 0:
            izquierdo = padre.hijos[indice - 1]
            if hijo.hoja:
                izquierdo.claves.extend(hijo.claves)
                izquierdo.siguiente = hijo.siguiente
            else:
                izquierdo.hijos.extend(hijo.hijos)
                self._actualizar_separadores(izquierdo)
            padre.hijos.pop(indice)
        else:
            derecho = padre.hijos[indice + 1]
            if hijo.hoja:
                hijo.claves.extend(derecho.claves)
                hijo.siguiente = derecho.siguiente
            else:
                hijo.hijos.extend(derecho.hijos)
                self._actualizar_separadores(hijo)
            padre.hijos.pop(indice + 1)

    def _eliminar(self, nodo: NodoBPlus, clave: int) -> bool:
        if nodo.hoja:
            indice = bisect_left(nodo.claves, clave)
            if indice == len(nodo.claves) or nodo.claves[indice] != clave:
                return False
            nodo.claves.pop(indice)
            return True
        indice = bisect_right(nodo.claves, clave)
        if not self._eliminar(nodo.hijos[indice], clave):
            return False
        self._reparar(nodo, indice)
        self._actualizar_separadores(nodo)
        return True

    def eliminar(self, clave: int) -> bool:
        """Elimina una clave y reequilibra el árbol si hace falta."""
        if not self._eliminar(self.raiz, clave):
            return False
        while not self.raiz.hoja and len(self.raiz.hijos) == 1:
            self.raiz = self.raiz.hijos[0]
        self._cantidad -= 1
        return True

    def rango(self, inicio: int, fin: int) -> list[int]:
        """Claves en el intervalo cerrado [inicio, fin], ordenadas."""
        if inicio > fin:
            return []
        hoja = self._hoja_para(inicio)
        resultado: list[int] = []
        while hoja is not None:
            for clave in hoja.claves:
                if clave > fin:
                    return resultado
                if clave >= inicio:
                    resultado.append(clave)
            hoja = hoja.siguiente
        return resultado

    def en_orden(self) -> list[int]:
        """Recorre todas las hojas de izquierda a derecha."""
        nodo = self.raiz
        while not nodo.hoja:
            nodo = nodo.hijos[0]
        resultado: list[int] = []
        while nodo is not None:
            resultado.extend(nodo.claves)
            nodo = nodo.siguiente
        return resultado

    def __len__(self) -> int:
        return self._cantidad


if __name__ == "__main__":
    for orden in (3, 4, 5, 8):
        arbol = ArbolBPlus(orden)
        assert not arbol.buscar(10) and not arbol.eliminar(10)
        for numero in (9, 2, 7, 1, 5, 3, 8, 6, 4, 0):
            assert arbol.insertar(numero)
        assert not arbol.insertar(5)
        assert arbol.en_orden() == list(range(10))
        assert arbol.rango(3, 7) == [3, 4, 5, 6, 7]
        assert arbol.rango(8, 3) == []
        for numero in (0, 9, 5, 2, 6, 1, 7, 3, 8, 4):
            assert arbol.buscar(numero) and arbol.eliminar(numero)
            assert not arbol.buscar(numero)
        assert len(arbol) == 0 and arbol.en_orden() == []
        assert arbol.insertar(42) and arbol.buscar(42)
    try:
        ArbolBPlus(2)
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba ValueError")
    print("Ejercicio 227: pruebas superadas")
