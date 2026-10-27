"""
Enunciado:

225. Árbol Splay: Desarrolla una clase ArbolSplay que implemente un árbol
    Splay y permita realizar operaciones de acceso y reorganización.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(eq=False)
class NodoSplay:
    """Nodo de un árbol de búsqueda con referencia a su progenitor."""

    valor: int
    izquierdo: NodoSplay | None = None
    derecho: NodoSplay | None = None
    padre: NodoSplay | None = None


class ArbolSplay:
    """Árbol de búsqueda autoajustable, sin valores duplicados.

    Tras una inserción o búsqueda, el nodo accedido asciende a la raíz.
    Una búsqueda fallida acerca a la raíz el último nodo visitado.
    Las operaciones cuestan O(log n) amortizado y O(n) en el peor caso.
    """

    def __init__(self) -> None:
        self.raiz: NodoSplay | None = None
        self._cantidad = 0

    def _rotar_izquierda(self, nodo: NodoSplay) -> None:
        """Rota el subárbol de nodo hacia la izquierda."""
        hijo = nodo.derecho
        assert hijo is not None
        nodo.derecho = hijo.izquierdo
        if hijo.izquierdo is not None:
            hijo.izquierdo.padre = nodo
        hijo.padre = nodo.padre
        if nodo.padre is None:
            self.raiz = hijo
        elif nodo is nodo.padre.izquierdo:
            nodo.padre.izquierdo = hijo
        else:
            nodo.padre.derecho = hijo
        hijo.izquierdo = nodo
        nodo.padre = hijo

    def _rotar_derecha(self, nodo: NodoSplay) -> None:
        """Rota el subárbol de nodo hacia la derecha."""
        hijo = nodo.izquierdo
        assert hijo is not None
        nodo.izquierdo = hijo.derecho
        if hijo.derecho is not None:
            hijo.derecho.padre = nodo
        hijo.padre = nodo.padre
        if nodo.padre is None:
            self.raiz = hijo
        elif nodo is nodo.padre.izquierdo:
            nodo.padre.izquierdo = hijo
        else:
            nodo.padre.derecho = hijo
        hijo.derecho = nodo
        nodo.padre = hijo

    def _splay(self, nodo: NodoSplay) -> None:
        """Sube nodo a la raíz con pasos zig, zig-zig y zig-zag."""
        while nodo.padre is not None:
            padre = nodo.padre
            abuelo = padre.padre
            if abuelo is None:  # Zig.
                if nodo is padre.izquierdo:
                    self._rotar_derecha(padre)
                else:
                    self._rotar_izquierda(padre)
            elif nodo is padre.izquierdo and padre is abuelo.izquierdo:
                self._rotar_derecha(abuelo)  # Zig-zig izquierdo.
                self._rotar_derecha(padre)
            elif nodo is padre.derecho and padre is abuelo.derecho:
                self._rotar_izquierda(abuelo)  # Zig-zig derecho.
                self._rotar_izquierda(padre)
            elif nodo is padre.derecho:  # Zig-zag izquierdo-derecho.
                self._rotar_izquierda(padre)
                self._rotar_derecha(abuelo)
            else:  # Zig-zag derecho-izquierdo.
                self._rotar_derecha(padre)
                self._rotar_izquierda(abuelo)

    def buscar(self, valor: int) -> NodoSplay | None:
        """Devuelve el nodo buscado y lo lleva a la raíz si existe."""
        actual = self.raiz
        ultimo: NodoSplay | None = None
        while actual is not None:
            ultimo = actual
            if valor == actual.valor:
                self._splay(actual)
                return actual
            actual = actual.izquierdo if valor < actual.valor else actual.derecho
        if ultimo is not None:
            self._splay(ultimo)
        return None

    def insertar(self, valor: int) -> bool:
        """Inserta un valor nuevo, llevándolo a la raíz; evita duplicados."""
        if self.raiz is None:
            self.raiz = NodoSplay(valor)
            self._cantidad = 1
            return True
        actual = self.raiz
        while True:
            if valor == actual.valor:
                self._splay(actual)
                return False
            if valor < actual.valor:
                if actual.izquierdo is None:
                    nuevo = NodoSplay(valor, padre=actual)
                    actual.izquierdo = nuevo
                    break
                actual = actual.izquierdo
            else:
                if actual.derecho is None:
                    nuevo = NodoSplay(valor, padre=actual)
                    actual.derecho = nuevo
                    break
                actual = actual.derecho
        self._splay(nuevo)
        self._cantidad += 1
        return True

    def eliminar(self, valor: int) -> bool:
        """Elimina un valor y reúne los subárboles restantes."""
        encontrado = self.buscar(valor)
        if encontrado is None:
            return False
        assert self.raiz is encontrado
        izquierdo, derecho = encontrado.izquierdo, encontrado.derecho
        if izquierdo is not None:
            izquierdo.padre = None
        if derecho is not None:
            derecho.padre = None
        encontrado.izquierdo = encontrado.derecho = None
        encontrado.padre = None
        if izquierdo is None:
            self.raiz = derecho
        else:
            self.raiz = izquierdo
            maximo = izquierdo
            while maximo.derecho is not None:
                maximo = maximo.derecho
            self._splay(maximo)
            assert self.raiz is maximo and maximo.derecho is None
            maximo.derecho = derecho
            if derecho is not None:
                derecho.padre = maximo
        self._cantidad -= 1
        return True

    def en_orden(self) -> list[int]:
        """Devuelve los valores ordenados sin modificar el árbol."""
        resultado: list[int] = []
        pila: list[NodoSplay] = []
        actual = self.raiz
        while pila or actual is not None:
            while actual is not None:
                pila.append(actual)
                actual = actual.izquierdo
            actual = pila.pop()
            resultado.append(actual.valor)
            actual = actual.derecho
        return resultado

    def __len__(self) -> int:
        return self._cantidad


if __name__ == "__main__":
    arbol = ArbolSplay()
    assert arbol.buscar(7) is None
    assert not arbol.eliminar(7)
    for numero in (10, 20, 30, 40, 50, 25):
        assert arbol.insertar(numero)
        assert arbol.raiz is not None and arbol.raiz.valor == numero
    assert arbol.en_orden() == [10, 20, 25, 30, 40, 50]
    assert not arbol.insertar(20)
    assert arbol.raiz is not None and arbol.raiz.valor == 20
    nodo = arbol.buscar(40)
    assert nodo is arbol.raiz and nodo.valor == 40
    assert arbol.buscar(999) is None
    assert arbol.raiz is not None and arbol.raiz.valor == 50
    assert arbol.eliminar(30)
    assert arbol.eliminar(50)
    assert not arbol.eliminar(50)
    assert arbol.en_orden() == [10, 20, 25, 40]
    for numero in (10, 20, 25, 40):
        assert arbol.eliminar(numero)
    assert len(arbol) == 0 and arbol.raiz is None
    print("Ejercicio 225: pruebas superadas")
