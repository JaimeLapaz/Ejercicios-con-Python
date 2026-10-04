"""
Enunciado:

160. Cola Doble: Diseña una cola doble utilizando una lista y
funciones para insertar y eliminar elementos tanto al principio
como al final de la cola.

Solución:
"""

from typing import TypeVar

T = TypeVar("T")


def insertar_inicio(cola: list[T], elemento: T) -> None:
    """Inserta un elemento al principio de la cola doble."""
    cola.insert(0, elemento)


def insertar_final(cola: list[T], elemento: T) -> None:
    """Inserta un elemento al final de la cola doble."""
    cola.append(elemento)


def eliminar_inicio(cola: list[T]) -> T:
    """Elimina y devuelve el elemento del principio."""
    if not cola:
        raise IndexError("La cola doble está vacía.")
    return cola.pop(0)


def eliminar_final(cola: list[T]) -> T:
    """Elimina y devuelve el elemento del final."""
    if not cola:
        raise IndexError("La cola doble está vacía.")
    return cola.pop()


if __name__ == "__main__":
    cola: list[int] = [2, 3]
    insertar_inicio(cola, 1)
    insertar_final(cola, 4)

    print("Cola doble:", cola)
    assert cola == [1, 2, 3, 4]
    assert eliminar_inicio(cola) == 1
    assert eliminar_final(cola) == 4
    assert cola == [2, 3]
