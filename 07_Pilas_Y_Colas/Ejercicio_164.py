"""
Enunciado:

164. Cola Circular: Diseña una cola circular utilizando una lista y
funciones para encolar y desencolar elementos.

Solución:
"""

from typing import TypeVar

T = TypeVar("T")


def crear_cola(capacidad: int) -> list[T | None]:
    """Crea el almacenamiento fijo de una cola circular."""
    if capacidad <= 0:
        raise ValueError("La capacidad debe ser mayor que cero.")
    return [None] * capacidad


def encolar(
    cola: list[T | None], elemento: T, final: int, cantidad: int
) -> tuple[int, int]:
    """Inserta un elemento y devuelve el nuevo final y cantidad."""
    if cantidad == len(cola):
        raise OverflowError("La cola circular está llena.")
    cola[final] = elemento
    return (final + 1) % len(cola), cantidad + 1


def desencolar(
    cola: list[T | None], frente: int, cantidad: int
) -> tuple[T, int, int]:
    """Extrae el elemento del frente y actualiza los índices."""
    if cantidad == 0:
        raise IndexError("La cola circular está vacía.")
    elemento = cola[frente]
    cola[frente] = None
    return elemento, (frente + 1) % len(cola), cantidad - 1  # type: ignore[return-value]


if __name__ == "__main__":
    cola = crear_cola(3)
    frente = final = cantidad = 0
    for valor in (10, 20, 30):
        final, cantidad = encolar(cola, valor, final, cantidad)

    primero, frente, cantidad = desencolar(cola, frente, cantidad)
    final, cantidad = encolar(cola, 40, final, cantidad)
    print("Almacenamiento circular:", cola)

    assert primero == 10
    assert cola == [40, 20, 30]
    assert cantidad == 3
