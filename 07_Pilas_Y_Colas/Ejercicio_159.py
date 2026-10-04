"""
Enunciado:

159. Cola: Crea una cola utilizando una lista y funciones para
encolar y desencolar elementos.

Solución:
"""

from typing import TypeVar

T = TypeVar("T")


def encolar(cola: list[T], elemento: T) -> None:
    """Añade un elemento al final de la cola."""
    cola.append(elemento)


def desencolar(cola: list[T]) -> T:
    """Retira y devuelve el primer elemento de la cola."""
    if not cola:
        raise IndexError("No se puede desencolar una cola vacía.")
    return cola.pop(0)


if __name__ == "__main__":
    cola: list[str] = []
    encolar(cola, "Ana")
    encolar(cola, "Luis")
    encolar(cola, "Marta")

    print("Cola:", cola)
    print("Atendido:", desencolar(cola))
    assert cola == ["Luis", "Marta"]
    assert desencolar(cola) == "Luis"
    assert cola == ["Marta"]
