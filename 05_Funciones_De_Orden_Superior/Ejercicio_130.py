"""
Enunciado:

130. Suma de Números en Lista: Diseña una función de orden superior que
tome una lista de números y una función acumuladora como argumentos,
y devuelva la suma acumulada de los números en la lista.

Solución:
"""

from collections.abc import Callable
from functools import reduce

Numero = int | float


def sumar_con_acumuladora(
    numeros: list[Numero], acumuladora: Callable[[Numero, Numero], Numero]
) -> Numero:
    """Acumula los valores desde cero con la función de suma indicada."""
    return reduce(acumuladora, numeros, 0)


if __name__ == "__main__":
    valores = [3, 5, 7, 2]
    resultado = sumar_con_acumuladora(valores, lambda total, numero: total + numero)

    print("Números:", valores)
    print("Suma acumulada:", resultado)
    assert resultado == 17
    assert sumar_con_acumuladora([], lambda total, numero: total + numero) == 0
