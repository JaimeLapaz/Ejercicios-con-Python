"""
Enunciado:

191. Listas Enlazadas Dobles: Crea una clase ListaEnlazadaDoble para
    gestionar una lista enlazada doble que permita agregar y eliminar
    elementos en ambos sentidos.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterator, TypeVar

T = TypeVar("T")


@dataclass
class NodoDoble(Generic[T]):
    """Nodo con enlaces al anterior y al siguiente."""

    valor: T
    anterior: NodoDoble[T] | None = None
    siguiente: NodoDoble[T] | None = None


class ListaEnlazadaDoble(Generic[T]):
    """Lista doble con operaciones en los extremos en O(1)."""

    def __init__(self) -> None:
        self._cabeza: NodoDoble[T] | None = None
        self._cola: NodoDoble[T] | None = None
        self._longitud = 0

    def agregar_inicio(self, valor: T) -> None:
        """Inserta un valor al principio de la lista."""
        nuevo = NodoDoble(valor, siguiente=self._cabeza)
        if self._cabeza is None:
            self._cola = nuevo
        else:
            self._cabeza.anterior = nuevo
        self._cabeza = nuevo
        self._longitud += 1

    def agregar_final(self, valor: T) -> None:
        """Inserta un valor al final de la lista."""
        nuevo = NodoDoble(valor, anterior=self._cola)
        if self._cola is None:
            self._cabeza = nuevo
        else:
            self._cola.siguiente = nuevo
        self._cola = nuevo
        self._longitud += 1

    def _desvincular(self, nodo: NodoDoble[T]) -> T:
        """Desenlaza un nodo existente sin recorrer la lista."""
        if nodo.anterior is None:
            self._cabeza = nodo.siguiente
        else:
            nodo.anterior.siguiente = nodo.siguiente
        if nodo.siguiente is None:
            self._cola = nodo.anterior
        else:
            nodo.siguiente.anterior = nodo.anterior
        self._longitud -= 1
        nodo.anterior = None
        nodo.siguiente = None
        return nodo.valor

    def eliminar_inicio(self) -> T:
        """Extrae el primer valor; lanza IndexError si está vacía."""
        if self._cabeza is None:
            raise IndexError("No se puede eliminar de una lista vacía")
        return self._desvincular(self._cabeza)

    def eliminar_final(self) -> T:
        """Extrae el último valor; lanza IndexError si está vacía."""
        if self._cola is None:
            raise IndexError("No se puede eliminar de una lista vacía")
        return self._desvincular(self._cola)

    def eliminar(self, valor: T, desde_final: bool = False) -> bool:
        """Elimina la primera coincidencia en el sentido indicado, en O(n)."""
        actual = self._cola if desde_final else self._cabeza
        while actual is not None:
            if actual.valor == valor:
                self._desvincular(actual)
                return True
            actual = actual.anterior if desde_final else actual.siguiente
        return False

    def __iter__(self) -> Iterator[T]:
        actual = self._cabeza
        while actual is not None:
            yield actual.valor
            actual = actual.siguiente

    def iterar_reversa(self) -> Iterator[T]:
        """Recorre los valores desde el final hasta el principio."""
        actual = self._cola
        while actual is not None:
            yield actual.valor
            actual = actual.anterior

    def __len__(self) -> int:
        return self._longitud


if __name__ == "__main__":
    lista = ListaEnlazadaDoble[int]()
    assert list(lista) == [] and list(lista.iterar_reversa()) == []
    try:
        lista.eliminar_inicio()
    except IndexError:
        pass
    else:
        raise AssertionError("Una lista vacía debe lanzar IndexError")

    lista.agregar_inicio(2)
    lista.agregar_inicio(1)
    lista.agregar_final(3)
    lista.agregar_final(2)
    assert list(lista) == [1, 2, 3, 2]
    assert list(lista.iterar_reversa()) == [2, 3, 2, 1]
    assert lista.eliminar(2, desde_final=True)
    assert lista.eliminar(2)
    assert list(lista) == [1, 3] and len(lista) == 2
    assert lista.eliminar_inicio() == 1
    assert lista.eliminar_final() == 3
    assert not lista.eliminar(99) and len(lista) == 0
    lista.agregar_final(7)
    assert list(lista.iterar_reversa()) == [7]
    assert lista.eliminar_final() == 7
    print("Lista tras las operaciones:", list(lista))
