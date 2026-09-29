"""
Enunciado:

136. Reducción de Lista: Desarrolla una función de orden superior que
tome una lista de números y una función de reducción (como máximo o
mínimo) como argumentos, y devuelva el resultado de aplicarla a la lista.

Solución:
"""

from collections.abc import Callable
from functools import reduce

Numero = int | float


def reducir_numeros(
    numeros: list[Numero], reductor: Callable[[Numero, Numero], Numero]
) -> Numero:
    """Reduce una lista no vacía usando la función binaria recibida."""
    if not numeros:
        raise ValueError("No se puede reducir una lista vacía sin valor inicial.")

    return reduce(reductor, numeros)


if __name__ == "__main__":
    numeros = [8, 3, 12, 5, 1]
    mayor = reducir_numeros(numeros, max)
    menor = reducir_numeros(numeros, min)

    print("Mayor:", mayor)
    print("Menor:", menor)
    assert mayor == 12
    assert menor == 1

    try:
        reducir_numeros([], max)
    except ValueError as error:
        print("Lista vacía:", error)
