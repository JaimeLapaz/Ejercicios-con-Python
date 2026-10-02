"""
Enunciado:

149. Factorial: Implementa una función recursiva para calcular el
factorial de un número.

Solución:
"""


def factorial(n: int) -> int:
    """Calcula n! de forma recursiva."""
    if n < 0:
        raise ValueError("El factorial no está definido para negativos.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print("5! =", factorial(5))
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

    try:
        factorial(-2)
    except ValueError as error:
        print("Entrada no válida:", error)
