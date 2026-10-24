"""
Enunciado:

222. Árbol 2-3: Crea una clase Arbol23 que implemente un árbol 2-3 y
    permita realizar inserciones y eliminaciones manteniendo la propiedad.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator


@dataclass
class Nodo23:
    """Nodo de 2 o 3 hijos (1 o 2 claves), salvo durante el reajuste."""

    claves: list[int] = field(default_factory=list)
    hijos: list[Nodo23] = field(default_factory=list)

    @property
    def es_hoja(self) -> bool:
        return not self.hijos


class Arbol23:
    """Conjunto ordenado de enteros mediante un árbol 2-3 equilibrado.

    Todos los caminos desde la raíz hasta las hojas tienen igual longitud.
    Buscar, insertar y eliminar requieren O(log n) en el peor caso.
    No admite claves duplicadas.
    """

    def __init__(self) -> None:
        self.raiz: Nodo23 | None = None
        self._tamano = 0

    def __len__(self) -> int:
        return self._tamano

    def buscar(self, clave: int) -> bool:
        """Comprueba si una clave está almacenada."""
        nodo = self.raiz
        while nodo is not None:
            indice = 0
            while indice < len(nodo.claves) and nodo.claves[indice] < clave:
                indice += 1
            if indice < len(nodo.claves) and nodo.claves[indice] == clave:
                return True
            nodo = nodo.hijos[indice] if nodo.hijos else None
        return False

    def __contains__(self, clave: int) -> bool:
        return self.buscar(clave)

    @classmethod
    def _insertar(cls, nodo: Nodo23, clave: int) -> tuple[bool, tuple[int, Nodo23] | None]:
        """Devuelve (insertada, promoción); el nodo original es el hijo izquierdo."""
        indice = 0
        while indice < len(nodo.claves) and nodo.claves[indice] < clave:
            indice += 1
        if indice < len(nodo.claves) and nodo.claves[indice] == clave:
            return False, None

        if nodo.es_hoja:
            nodo.claves.insert(indice, clave)
        else:
            insertada, promocion = cls._insertar(nodo.hijos[indice], clave)
            if not insertada:
                return False, None
            if promocion is not None:
                mediana, derecho = promocion
                nodo.claves.insert(indice, mediana)
                nodo.hijos.insert(indice + 1, derecho)

        if len(nodo.claves) <= 2:
            return True, None

        # Un nodo temporal de tres claves se divide en dos nodos de una.
        mediana = nodo.claves[1]
        derecho = Nodo23(nodo.claves[2:], nodo.hijos[2:] if nodo.hijos else [])
        nodo.claves = nodo.claves[:1]
        if nodo.hijos:
            nodo.hijos = nodo.hijos[:2]
        return True, (mediana, derecho)

    def insertar(self, clave: int) -> bool:
        """Inserta una clave y devuelve False si ya existía."""
        if self.raiz is None:
            self.raiz = Nodo23([clave])
            self._tamano = 1
            return True
        insertada, promocion = self._insertar(self.raiz, clave)
        if not insertada:
            return False
        if promocion is not None:
            mediana, derecho = promocion
            self.raiz = Nodo23([mediana], [self.raiz, derecho])
        self._tamano += 1
        return True

    @staticmethod
    def _maximo(nodo: Nodo23) -> int:
        while nodo.hijos:
            nodo = nodo.hijos[-1]
        return nodo.claves[-1]

    @staticmethod
    def _reparar(nodo: Nodo23, indice: int) -> None:
        """Corrige un hijo con cero claves, prestando o fusionando hermanos."""
        hijo = nodo.hijos[indice]
        if hijo.claves:
            return

        if indice > 0:
            izquierdo = nodo.hijos[indice - 1]
            if len(izquierdo.claves) == 2:
                hijo.claves.insert(0, nodo.claves[indice - 1])
                nodo.claves[indice - 1] = izquierdo.claves.pop()
                if izquierdo.hijos:
                    hijo.hijos.insert(0, izquierdo.hijos.pop())
                return

        if indice + 1 < len(nodo.hijos):
            derecho = nodo.hijos[indice + 1]
            if len(derecho.claves) == 2:
                hijo.claves.append(nodo.claves[indice])
                nodo.claves[indice] = derecho.claves.pop(0)
                if derecho.hijos:
                    hijo.hijos.append(derecho.hijos.pop(0))
                return

        if indice > 0:
            izquierdo = nodo.hijos[indice - 1]
            izquierdo.claves.append(nodo.claves.pop(indice - 1))
            izquierdo.claves.extend(hijo.claves)
            izquierdo.hijos.extend(hijo.hijos)
            nodo.hijos.pop(indice)
        else:
            derecho = nodo.hijos[indice + 1]
            hijo.claves.append(nodo.claves.pop(indice))
            hijo.claves.extend(derecho.claves)
            hijo.hijos.extend(derecho.hijos)
            nodo.hijos.pop(indice + 1)

    @classmethod
    def _eliminar(cls, nodo: Nodo23, clave: int) -> bool:
        indice = 0
        while indice < len(nodo.claves) and nodo.claves[indice] < clave:
            indice += 1
        encontrada = indice < len(nodo.claves) and nodo.claves[indice] == clave

        if nodo.es_hoja:
            if encontrada:
                nodo.claves.pop(indice)
            return encontrada

        if encontrada:
            # Sustituye por el predecesor y elimina ese valor de su subárbol.
            predecesor = cls._maximo(nodo.hijos[indice])
            nodo.claves[indice] = predecesor
            cls._eliminar(nodo.hijos[indice], predecesor)
        else:
            if not cls._eliminar(nodo.hijos[indice], clave):
                return False
        cls._reparar(nodo, indice)
        return True

    def eliminar(self, clave: int) -> bool:
        """Elimina la clave y devuelve False si no existía."""
        if self.raiz is None or not self._eliminar(self.raiz, clave):
            return False
        self._tamano -= 1
        if not self.raiz.claves:
            self.raiz = self.raiz.hijos[0] if self.raiz.hijos else None
        return True

    def __iter__(self) -> Iterator[int]:
        """Recorre las claves en orden ascendente."""
        def visitar(nodo: Nodo23) -> Iterator[int]:
            for indice, clave in enumerate(nodo.claves):
                if nodo.hijos:
                    yield from visitar(nodo.hijos[indice])
                yield clave
            if nodo.hijos:
                yield from visitar(nodo.hijos[-1])

        if self.raiz is not None:
            yield from visitar(self.raiz)

    def validar(self) -> bool:
        """Verifica ocupación, orden, número de hijos y profundidad de hojas."""
        if self.raiz is None:
            return self._tamano == 0
        profundidades: set[int] = set()

        def comprobar(nodo: Nodo23, minimo: int | None,
                      maximo: int | None, profundidad: int) -> int:
            if not 1 <= len(nodo.claves) <= 2:
                raise ValueError("Número de claves inválido")
            if any((minimo is not None and clave <= minimo)
                   or (maximo is not None and clave >= maximo)
                   for clave in nodo.claves):
                raise ValueError("Clave fuera de rango")
            if len(nodo.claves) == 2 and nodo.claves[0] >= nodo.claves[1]:
                raise ValueError("Claves desordenadas")
            if not nodo.hijos:
                profundidades.add(profundidad)
                return len(nodo.claves)
            if len(nodo.hijos) != len(nodo.claves) + 1:
                raise ValueError("Cantidad de hijos inválida")
            limites = [minimo, *nodo.claves, maximo]
            return len(nodo.claves) + sum(
                comprobar(hijo, limites[i], limites[i + 1], profundidad + 1)
                for i, hijo in enumerate(nodo.hijos)
            )

        try:
            total = comprobar(self.raiz, None, None, 0)
        except ValueError:
            return False
        return len(profundidades) == 1 and total == self._tamano


if __name__ == "__main__":
    arbol = Arbol23()
    assert arbol.validar() and list(arbol) == []
    for numero in (10, 20, 5, 15, 30, 25, 35, 1, 8, 12, 18):
        assert arbol.insertar(numero)
        assert arbol.validar()
    assert not arbol.insertar(20)
    assert list(arbol) == [1, 5, 8, 10, 12, 15, 18, 20, 25, 30, 35]
    assert arbol.buscar(25) and not arbol.buscar(100)
    assert len(arbol) == 11
    assert not arbol.eliminar(100)
    for numero in (15, 1, 35, 10, 5, 8, 12, 18, 20, 25, 30):
        assert arbol.eliminar(numero)
        assert arbol.validar()
        assert not arbol.buscar(numero)
    assert len(arbol) == 0 and arbol.raiz is None
    assert not arbol.eliminar(10)
    print("Ejercicio 222: pruebas superadas")
