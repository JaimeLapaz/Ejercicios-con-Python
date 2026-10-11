"""
Enunciado:

192. Pila con Listas Enlazadas: Implementa una clase Pila utilizando
    una lista enlazada que permita realizar operaciones de apilamiento
    y desapilamiento.

Solución:
"""

from __future__ import annotations

from typing import Generic, Iterator, TypeVar

from Ejercicio_188 import Nodo

T = TypeVar("T")


class Pila(Generic[T]):
    """Pila LIFO implementada mediante nodos enlazados."""

    def __init__(self) -> None:
        self._cima: Nodo[T] | None = None
        self._longitud = 0

    def apilar(self, valor: T) -> None:
        """Coloca un elemento en la cima en O(1)."""
        self._cima = Nodo(valor, siguiente=self._cima)
        self._longitud += 1

    def desapilar(self) -> T:
        """Retira y devuelve la cima en O(1); falla si está vacía."""
        if self._cima is None:
            raise IndexError("No se puede desapilar una pila vacía")
        valor = self._cima.valor
        self._cima = self._cima.siguiente
        self._longitud -= 1
        return valor

    def ver_cima(self) -> T:
        """Consulta la cima sin extraerla."""
        if self._cima is None:
            raise IndexError("La pila está vacía")
        return self._cima.valor

    def esta_vacia(self) -> bool:
        return self._cima is None

    def __len__(self) -> int:
        return self._longitud

    def __iter__(self) -> Iterator[T]:
        """Itera desde la cima hacia la base."""
        actual = self._cima
        while actual is not None:
            yield actual.valor
            actual = actual.siguiente


if __name__ == "__main__":
    pila = Pila[str]()
    assert pila.esta_vacia() and len(pila) == 0
    try:
        pila.desapilar()
    except IndexError:
        pass
    else:
        raise AssertionError("Una pila vacía debe lanzar IndexError")

    for palabra in ("primero", "segundo", "tercero"):
        pila.apilar(palabra)
    assert pila.ver_cima() == "tercero"
    assert list(pila) == ["tercero", "segundo", "primero"]
    assert len(pila) == 3
    assert [pila.desapilar() for _ in range(3)] == [
        "tercero", "segundo", "primero"
    ]
    assert pila.esta_vacia()
    pila.apilar("nuevo")
    assert pila.desapilar() == "nuevo"
    print("Pila vacía:", pila.esta_vacia())
