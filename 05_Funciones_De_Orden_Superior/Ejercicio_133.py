"""
Enunciado:

133. Composición de Funciones: Implementa una función de orden superior
que tome dos funciones como argumentos y devuelva una nueva función
que sea la composición de las dos funciones.

Solución:
"""

from collections.abc import Callable
from typing import TypeVar

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")


def componer(
    exterior: Callable[[B], C], interior: Callable[[A], B]
) -> Callable[[A], C]:
    """Devuelve una función que aplica primero interior y después exterior."""
    def compuesta(valor: A) -> C:
        return exterior(interior(valor))

    return compuesta


if __name__ == "__main__":
    duplicar = lambda numero: numero * 2
    sumar_tres = lambda numero: numero + 3

    duplicar_despues_de_sumar = componer(duplicar, sumar_tres)
    sumar_despues_de_duplicar = componer(sumar_tres, duplicar)

    print("(5 + 3) * 2 =", duplicar_despues_de_sumar(5))
    print("(5 * 2) + 3 =", sumar_despues_de_duplicar(5))
    assert duplicar_despues_de_sumar(5) == 16
    assert sumar_despues_de_duplicar(5) == 13
