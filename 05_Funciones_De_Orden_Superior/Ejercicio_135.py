"""
Enunciado:

135. Operaciones en Lista: Crea una función de orden superior que tome
una lista de números y una función de operación binaria (como suma o
multiplicación) como argumentos, y aplique la operación a todos los
elementos de la lista.

Solución:
"""

from collections.abc import Callable
from functools import reduce

Numero = int | float


def operar_lista(
    numeros: list[Numero], operacion: Callable[[Numero, Numero], Numero]
) -> Numero:
    """Combina los números de izquierda a derecha mediante la operación."""
    if not numeros:
        raise ValueError("Se necesita al menos un número para operar.")

    return reduce(operacion, numeros)


if __name__ == "__main__":
    numeros = [2, 3, 4]
    suma = operar_lista(numeros, lambda anterior, actual: anterior + actual)
    producto = operar_lista(numeros, lambda anterior, actual: anterior * actual)

    print("Suma:", suma)
    print("Producto:", producto)
    assert suma == 9
    assert producto == 24

    try:
        operar_lista([], lambda a, b: a + b)
    except ValueError as error:
        print("Lista vacía:", error)
