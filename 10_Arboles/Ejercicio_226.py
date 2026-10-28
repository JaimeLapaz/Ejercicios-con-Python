"""
Enunciado:

226. Árbol de Intervalo: Crea una clase ArbolIntervalo que implemente un árbol
    de intervalo para buscar y actualizar rangos en un conjunto de valores.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass, field

Intervalo = tuple[int, int]


@dataclass(eq=False)
class NodoIntervalo:
    """Nodo AVL con extremos mínimo y máximo de todo su subárbol."""

    intervalo: Intervalo
    izquierdo: NodoIntervalo | None = None
    derecho: NodoIntervalo | None = None
    altura: int = 1
    minimo_inicio: int = field(init=False)
    maximo_fin: int = field(init=False)

    def __post_init__(self) -> None:
        self.minimo_inicio, self.maximo_fin = self.intervalo


class ArbolIntervalo:
    """Índice AVL de intervalos cerrados [inicio, fin], sin duplicados.

    Inserción, eliminación y actualización: O(log n). Las consultas de
    solapamiento podan subárboles usando sus extremos agregados; devuelven
    los resultados ordenados por (inicio, fin).
    """

    def __init__(self) -> None:
        self.raiz: NodoIntervalo | None = None
        self._cantidad = 0

    @staticmethod
    def _validar(inicio: int, fin: int) -> Intervalo:
        if inicio > fin:
            raise ValueError("El inicio del intervalo no puede superar el fin")
        return inicio, fin

    @staticmethod
    def _altura(nodo: NodoIntervalo | None) -> int:
        return 0 if nodo is None else nodo.altura

    @classmethod
    def _recalcular(cls, nodo: NodoIntervalo) -> None:
        nodo.altura = 1 + max(cls._altura(nodo.izquierdo), cls._altura(nodo.derecho))
        nodo.minimo_inicio, nodo.maximo_fin = nodo.intervalo
        for hijo in (nodo.izquierdo, nodo.derecho):
            if hijo is not None:
                nodo.minimo_inicio = min(nodo.minimo_inicio, hijo.minimo_inicio)
                nodo.maximo_fin = max(nodo.maximo_fin, hijo.maximo_fin)

    @classmethod
    def _rotar_izquierda(cls, nodo: NodoIntervalo) -> NodoIntervalo:
        nuevo = nodo.derecho
        assert nuevo is not None
        nodo.derecho = nuevo.izquierdo
        nuevo.izquierdo = nodo
        cls._recalcular(nodo)
        cls._recalcular(nuevo)
        return nuevo

    @classmethod
    def _rotar_derecha(cls, nodo: NodoIntervalo) -> NodoIntervalo:
        nuevo = nodo.izquierdo
        assert nuevo is not None
        nodo.izquierdo = nuevo.derecho
        nuevo.derecho = nodo
        cls._recalcular(nodo)
        cls._recalcular(nuevo)
        return nuevo

    @classmethod
    def _equilibrar(cls, nodo: NodoIntervalo) -> NodoIntervalo:
        cls._recalcular(nodo)
        balance = cls._altura(nodo.izquierdo) - cls._altura(nodo.derecho)
        if balance > 1:
            assert nodo.izquierdo is not None
            if cls._altura(nodo.izquierdo.izquierdo) < cls._altura(nodo.izquierdo.derecho):
                nodo.izquierdo = cls._rotar_izquierda(nodo.izquierdo)
            return cls._rotar_derecha(nodo)
        if balance < -1:
            assert nodo.derecho is not None
            if cls._altura(nodo.derecho.derecho) < cls._altura(nodo.derecho.izquierdo):
                nodo.derecho = cls._rotar_derecha(nodo.derecho)
            return cls._rotar_izquierda(nodo)
        return nodo

    @classmethod
    def _insertar(
        cls, nodo: NodoIntervalo | None, intervalo: Intervalo
    ) -> tuple[NodoIntervalo, bool]:
        if nodo is None:
            return NodoIntervalo(intervalo), True
        if intervalo == nodo.intervalo:
            return nodo, False
        if intervalo < nodo.intervalo:
            nodo.izquierdo, insertado = cls._insertar(nodo.izquierdo, intervalo)
        else:
            nodo.derecho, insertado = cls._insertar(nodo.derecho, intervalo)
        return cls._equilibrar(nodo), insertado

    @classmethod
    def _eliminar(
        cls, nodo: NodoIntervalo | None, intervalo: Intervalo
    ) -> tuple[NodoIntervalo | None, bool]:
        if nodo is None:
            return None, False
        if intervalo < nodo.intervalo:
            nodo.izquierdo, eliminado = cls._eliminar(nodo.izquierdo, intervalo)
        elif intervalo > nodo.intervalo:
            nodo.derecho, eliminado = cls._eliminar(nodo.derecho, intervalo)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho, True
            if nodo.derecho is None:
                return nodo.izquierdo, True
            sucesor = nodo.derecho
            while sucesor.izquierdo is not None:
                sucesor = sucesor.izquierdo
            nodo.intervalo = sucesor.intervalo
            nodo.derecho, eliminado = cls._eliminar(nodo.derecho, sucesor.intervalo)
            assert eliminado
        return cls._equilibrar(nodo), eliminado

    def contiene(self, inicio: int, fin: int) -> bool:
        """Comprueba la existencia exacta de un intervalo en O(log n)."""
        objetivo = self._validar(inicio, fin)
        nodo = self.raiz
        while nodo is not None:
            if objetivo == nodo.intervalo:
                return True
            nodo = nodo.izquierdo if objetivo < nodo.intervalo else nodo.derecho
        return False

    def insertar(self, inicio: int, fin: int) -> bool:
        """Inserta un intervalo cerrado; devuelve False si ya existe."""
        self.raiz, insertado = self._insertar(self.raiz, self._validar(inicio, fin))
        self._cantidad += int(insertado)
        return insertado

    def eliminar(self, inicio: int, fin: int) -> bool:
        """Elimina un intervalo exacto, si está presente."""
        self.raiz, eliminado = self._eliminar(self.raiz, self._validar(inicio, fin))
        self._cantidad -= int(eliminado)
        return eliminado

    def actualizar(
        self, inicio_anterior: int, fin_anterior: int,
        inicio_nuevo: int, fin_nuevo: int,
    ) -> bool:
        """Sustituye un rango sin perder datos si el destino ya existe.

        Devuelve False si el origen no existe o el destino está ocupado.
        """
        anterior = self._validar(inicio_anterior, fin_anterior)
        nuevo = self._validar(inicio_nuevo, fin_nuevo)
        if not self.contiene(*anterior):
            return False
        if anterior == nuevo:
            return True
        if self.contiene(*nuevo):
            return False
        assert self.eliminar(*anterior)
        assert self.insertar(*nuevo)
        return True

    def buscar_superpuestos(self, inicio: int, fin: int) -> list[Intervalo]:
        """Busca rangos que se intersecan con [inicio, fin] (incluidos extremos)."""
        self._validar(inicio, fin)
        resultado: list[Intervalo] = []

        def visitar(nodo: NodoIntervalo | None) -> None:
            if nodo is None or nodo.maximo_fin < inicio or nodo.minimo_inicio > fin:
                return
            visitar(nodo.izquierdo)
            a, b = nodo.intervalo
            if a <= fin and inicio <= b:
                resultado.append(nodo.intervalo)
            visitar(nodo.derecho)

        visitar(self.raiz)
        return resultado

    def en_orden(self) -> list[Intervalo]:
        """Devuelve los intervalos ordenados por sus extremos."""
        resultado: list[Intervalo] = []
        pila: list[NodoIntervalo] = []
        actual = self.raiz
        while pila or actual is not None:
            while actual is not None:
                pila.append(actual)
                actual = actual.izquierdo
            actual = pila.pop()
            resultado.append(actual.intervalo)
            actual = actual.derecho
        return resultado

    def __len__(self) -> int:
        return self._cantidad


if __name__ == "__main__":
    arbol = ArbolIntervalo()
    assert arbol.buscar_superpuestos(1, 3) == []
    for inicio, fin in ((15, 20), (10, 30), (17, 19), (5, 20), (12, 15), (30, 40)):
        assert arbol.insertar(inicio, fin)
    assert not arbol.insertar(15, 20)
    assert len(arbol) == 6
    assert arbol.buscar_superpuestos(14, 16) == [
        (5, 20), (10, 30), (12, 15), (15, 20)
    ]
    assert arbol.buscar_superpuestos(40, 40) == [(30, 40)]
    assert arbol.buscar_superpuestos(41, 50) == []
    assert arbol.contiene(17, 19) and not arbol.contiene(17, 20)
    assert arbol.actualizar(17, 19, 18, 21)
    assert not arbol.contiene(17, 19) and arbol.contiene(18, 21)
    assert not arbol.actualizar(18, 21, 10, 30)  # Destino ocupado.
    assert not arbol.actualizar(99, 100, 101, 102)
    assert arbol.actualizar(18, 21, 18, 21)
    assert arbol.eliminar(10, 30) and not arbol.eliminar(10, 30)
    assert len(arbol) == 5
    try:
        arbol.insertar(8, 7)
    except ValueError:
        pass
    else:
        raise AssertionError("Debe rechazarse un intervalo invertido")
    print("Ejercicio 226: pruebas superadas")
