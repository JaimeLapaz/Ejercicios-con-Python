"""
Enunciado:

143. Operaciones con Fracciones: Crea una función de orden superior
que tome dos fracciones y una función de operación binaria, y
aplique la operación a las fracciones.

Solución:
"""

from collections.abc import Callable
from fractions import Fraction


def operar_fracciones(
    primera: Fraction,
    segunda: Fraction,
    operacion: Callable[[Fraction, Fraction], Fraction],
) -> Fraction:
    """Aplica a las fracciones la operación binaria recibida."""
    return operacion(primera, segunda)


if __name__ == "__main__":
    primera = Fraction(1, 2)
    segunda = Fraction(3, 4)

    suma = operar_fracciones(primera, segunda, lambda a, b: a + b)
    producto = operar_fracciones(primera, segunda, lambda a, b: a * b)
    diferencia = operar_fracciones(primera, segunda, lambda a, b: a - b)

    print("Suma:", suma)
    print("Producto:", producto)
    print("Diferencia:", diferencia)
    assert suma == Fraction(5, 4)
    assert producto == Fraction(3, 8)
    assert diferencia == Fraction(-1, 4)

    try:
        operar_fracciones(primera, Fraction(0), lambda a, b: a / b)
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
