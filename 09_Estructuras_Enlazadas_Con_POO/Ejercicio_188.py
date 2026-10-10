"""
Enunciado:

188. Lista Enlazada Simple: Implementa una clase ListaEnlazada para
    gestionar una lista enlazada simple que permita agregar y eliminar
    elementos.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterator, TypeVar

T = TypeVar("T")


@dataclass
class Nodo(Generic[T]):
    """Almacena un valor y la referencia al siguiente nodo."""

    valor: T
    siguiente: Nodo[T] | None = None


class ListaEnlazada(Generic[T]):
    """Lista simplemente enlazada con inserción al final en O(1)."""

    def __init__(self) -> None:
        self._cabeza: Nodo[T] | None = None
        self._cola: Nodo[T] | None = None
        self._longitud = 0

    def agregar(self, valor: T) -> None:
        """Añade un elemento al final de la lista."""
        nuevo = Nodo(valor)
        if self._cola is None:
            self._cabeza = nuevo
        else:
            self._cola.siguiente = nuevo
        self._cola = nuevo
        self._longitud += 1

    def eliminar(self, valor: T) -> bool:
        """Elimina la primera aparición del valor; devuelve si existía."""
        anterior: Nodo[T] | None = None
        actual = self._cabeza
        while actual is not None:
            if actual.valor == valor:
                if anterior is None:
                    self._cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                if self._cola is actual:
                    self._cola = anterior
                self._longitud -= 1
                return True
            anterior, actual = actual, actual.siguiente
        return False

    def __iter__(self) -> Iterator[T]:
        actual = self._cabeza
        while actual is not None:
            yield actual.valor
            actual = actual.siguiente

    def __len__(self) -> int:
        return self._longitud


if __name__ == "__main__":
    lista = ListaEnlazada[int]()
    assert not lista.eliminar(10)
    for numero in (3, 1, 3):
        lista.agregar(numero)
    print("Lista inicial:", list(lista))
    assert list(lista) == [3, 1, 3] and len(lista) == 3
    assert lista.eliminar(3) and list(lista) == [1, 3]
    assert lista.eliminar(3) and list(lista) == [1]
    assert not lista.eliminar(99)
    assert lista.eliminar(1) and len(lista) == 0
    lista.agregar(7)
    assert list(lista) == [7]
    print("Tras las operaciones:", list(lista))
