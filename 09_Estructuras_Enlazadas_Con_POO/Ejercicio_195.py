"""
Enunciado:

195. Cola Doble con Listas Enlazadas: Implementa una clase ColaDoble
    utilizando una lista enlazada que permita insertar y eliminar
    elementos tanto al principio como al final de la cola.

Solución:
"""

from __future__ import annotations

from typing import Generic, Iterator, TypeVar

from Ejercicio_191 import NodoDoble

T = TypeVar("T")


class ColaDoble(Generic[T]):
    """Cola doble enlazada con operaciones en ambos extremos en O(1)."""

    def __init__(self) -> None:
        self._frente: NodoDoble[T] | None = None
        self._final: NodoDoble[T] | None = None
        self._longitud = 0

    def insertar_inicio(self, valor: T) -> None:
        """Inserta un elemento por el frente."""
        nuevo = NodoDoble(valor, siguiente=self._frente)
        if self._frente is None:
            self._final = nuevo
        else:
            self._frente.anterior = nuevo
        self._frente = nuevo
        self._longitud += 1

    def insertar_final(self, valor: T) -> None:
        """Inserta un elemento por el final."""
        nuevo = NodoDoble(valor, anterior=self._final)
        if self._final is None:
            self._frente = nuevo
        else:
            self._final.siguiente = nuevo
        self._final = nuevo
        self._longitud += 1

    def eliminar_inicio(self) -> T:
        """Extrae el elemento del frente; lanza IndexError si está vacía."""
        if self._frente is None:
            raise IndexError("No se puede eliminar de una cola doble vacía")
        nodo = self._frente
        self._frente = nodo.siguiente
        if self._frente is None:
            self._final = None
        else:
            self._frente.anterior = None
        nodo.siguiente = None
        self._longitud -= 1
        return nodo.valor

    def eliminar_final(self) -> T:
        """Extrae el último elemento; lanza IndexError si está vacía."""
        if self._final is None:
            raise IndexError("No se puede eliminar de una cola doble vacía")
        nodo = self._final
        self._final = nodo.anterior
        if self._final is None:
            self._frente = None
        else:
            self._final.siguiente = None
        nodo.anterior = None
        self._longitud -= 1
        return nodo.valor

    def ver_inicio(self) -> T:
        if self._frente is None:
            raise IndexError("La cola doble está vacía")
        return self._frente.valor

    def ver_final(self) -> T:
        if self._final is None:
            raise IndexError("La cola doble está vacía")
        return self._final.valor

    def esta_vacia(self) -> bool:
        return self._frente is None

    def __len__(self) -> int:
        return self._longitud

    def __iter__(self) -> Iterator[T]:
        """Recorre desde el frente hacia el final."""
        actual = self._frente
        while actual is not None:
            yield actual.valor
            actual = actual.siguiente

    def iterar_reversa(self) -> Iterator[T]:
        """Recorre desde el final hacia el frente."""
        actual = self._final
        while actual is not None:
            yield actual.valor
            actual = actual.anterior


if __name__ == "__main__":
    cola = ColaDoble[int]()
    assert cola.esta_vacia() and len(cola) == 0
    for operacion in (
        cola.eliminar_inicio, cola.eliminar_final,
        cola.ver_inicio, cola.ver_final,
    ):
        try:
            operacion()
        except IndexError:
            pass
        else:
            raise AssertionError("Una cola doble vacía debe lanzar IndexError")

    cola.insertar_inicio(2)
    cola.insertar_inicio(1)
    cola.insertar_final(3)
    cola.insertar_final(4)
    assert list(cola) == [1, 2, 3, 4]
    assert list(cola.iterar_reversa()) == [4, 3, 2, 1]
    assert cola.ver_inicio() == 1 and cola.ver_final() == 4
    assert cola.eliminar_inicio() == 1
    assert cola.eliminar_final() == 4
    assert list(cola) == [2, 3] and len(cola) == 2
    assert cola.eliminar_final() == 3
    assert cola.eliminar_inicio() == 2
    assert cola.esta_vacia()
    cola.insertar_final(9)
    assert cola.eliminar_inicio() == 9
    cola.insertar_inicio(8)
    assert cola.eliminar_final() == 8
    print("Cola doble vacía:", cola.esta_vacia())
