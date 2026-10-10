"""
Enunciado:

189. Inversión de Lista: Desarrolla un método en la clase
    ListaEnlazada que invierta la lista enlazada.

Solución:
"""

from __future__ import annotations

from typing import TypeVar

from Ejercicio_188 import ListaEnlazada as ListaEnlazadaBase

T = TypeVar("T")


class ListaEnlazada(ListaEnlazadaBase[T]):
    """Amplía la lista simple con inversión de enlaces in situ."""

    def invertir(self) -> None:
        """Invierte los enlaces en O(n) sin crear nodos adicionales."""
        anterior = None
        actual = self._cabeza
        self._cola = actual
        while actual is not None:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self._cabeza = anterior


if __name__ == "__main__":
    vacia = ListaEnlazada[int]()
    vacia.invertir()
    assert list(vacia) == [] and len(vacia) == 0

    lista = ListaEnlazada[int]()
    for numero in (1, 2, 3, 4):
        lista.agregar(numero)
    lista.invertir()
    print("Invertida:", list(lista))
    assert list(lista) == [4, 3, 2, 1]
    lista.agregar(5)
    assert list(lista) == [4, 3, 2, 1, 5]
    lista.invertir()
    assert list(lista) == [5, 1, 2, 3, 4]
    assert lista.eliminar(4)
    assert list(lista) == [5, 1, 2, 3]

    unica = ListaEnlazada[str]()
    unica.agregar("único")
    unica.invertir()
    assert list(unica) == ["único"]
