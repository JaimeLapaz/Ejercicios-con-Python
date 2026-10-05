"""
Enunciado:

165. Cola Doble con Prioridad: Crea una cola doble con prioridad
utilizando una lista y funciones para insertar elementos con
diferentes prioridades.

Solución:
"""

from typing import TypeVar

T = TypeVar("T")
ElementoPrioridad = tuple[int, T]


def insertar(
    cola: list[ElementoPrioridad[T]], elemento: T, prioridad: int
) -> None:
    """Inserta manteniendo primero los elementos de mayor prioridad."""
    posicion = next(
        (
            indice
            for indice, (actual, _) in enumerate(cola)
            if prioridad > actual
        ),
        len(cola),
    )
    cola.insert(posicion, (prioridad, elemento))


def extraer_inicio(cola: list[ElementoPrioridad[T]]) -> T:
    """Extrae el elemento de mayor prioridad."""
    if not cola:
        raise IndexError("La cola está vacía.")
    return cola.pop(0)[1]


def extraer_final(cola: list[ElementoPrioridad[T]]) -> T:
    """Extrae el elemento situado al final de la cola doble."""
    if not cola:
        raise IndexError("La cola está vacía.")
    return cola.pop()[1]


if __name__ == "__main__":
    cola: list[ElementoPrioridad[str]] = []
    insertar(cola, "normal", 1)
    insertar(cola, "urgente", 3)
    insertar(cola, "preferente", 2)

    print("Cola:", cola)
    assert [elemento for _, elemento in cola] == [
        "urgente", "preferente", "normal"
    ]
    assert extraer_inicio(cola) == "urgente"
    assert extraer_final(cola) == "normal"
