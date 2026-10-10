"""
Enunciado:

190. Eliminación de Duplicados: Diseña un método en la clase
    ListaEnlazada que elimine los elementos duplicados de la lista.

Solución:
"""

from __future__ import annotations

from typing import TypeVar

from Ejercicio_189 import ListaEnlazada as ListaEnlazadaBase

T = TypeVar("T")


class ListaEnlazada(ListaEnlazadaBase[T]):
    """Amplía la lista enlazada con eliminación de duplicados."""

    def eliminar_duplicados(self) -> int:
        """Conserva la primera aparición de cada valor, incluso no hashable.

        Compara valores con igualdad; coste O(n²) y memoria O(n).
        Devuelve la cantidad de nodos eliminados.
        """
        vistos: list[T] = []
        anterior = None
        actual = self._cabeza
        eliminados = 0
        while actual is not None:
            if any(actual.valor == valor for valor in vistos):
                assert anterior is not None
                anterior.siguiente = actual.siguiente
                if self._cola is actual:
                    self._cola = anterior
                self._longitud -= 1
                eliminados += 1
            else:
                vistos.append(actual.valor)
                anterior = actual
            actual = actual.siguiente
        return eliminados


if __name__ == "__main__":
    lista = ListaEnlazada[int]()
    for numero in (1, 2, 1, 3, 2, 3, 3):
        lista.agregar(numero)
    assert lista.eliminar_duplicados() == 4
    print("Sin duplicados:", list(lista))
    assert list(lista) == [1, 2, 3] and len(lista) == 3
    assert lista.eliminar_duplicados() == 0
    lista.agregar(4)
    assert list(lista) == [1, 2, 3, 4]

    no_hashables = ListaEnlazada[list[int]]()
    for elemento in ([1], [2], [1], [2], [3]):
        no_hashables.agregar(elemento)
    assert no_hashables.eliminar_duplicados() == 2
    assert list(no_hashables) == [[1], [2], [3]]

    vacia = ListaEnlazada[str]()
    assert vacia.eliminar_duplicados() == 0
    repetidos = ListaEnlazada[int]()
    for _ in range(3):
        repetidos.agregar(7)
    assert repetidos.eliminar_duplicados() == 2
    assert repetidos.eliminar(7) and len(repetidos) == 0
