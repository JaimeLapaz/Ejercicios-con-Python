"""
Enunciado:

158. Pila: Implementa una pila utilizando una lista y crea funciones
para apilar y desapilar elementos.

Solución:
"""

from typing import TypeVar

T = TypeVar("T")


def apilar(pila: list[T], elemento: T) -> None:
    """Añade un elemento en la parte superior de la pila."""
    pila.append(elemento)


def desapilar(pila: list[T]) -> T:
    """Retira y devuelve el elemento superior de la pila."""
    if not pila:
        raise IndexError("No se puede desapilar una pila vacía.")
    return pila.pop()


if __name__ == "__main__":
    pila: list[int] = []
    apilar(pila, 10)
    apilar(pila, 20)
    apilar(pila, 30)

    print("Pila:", pila)
    print("Elemento desapilado:", desapilar(pila))
    assert pila == [10, 20]
    assert desapilar(pila) == 20
    assert pila == [10]
