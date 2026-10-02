"""
Enunciado:

151. Fibonacci: Desarrolla una función recursiva para calcular el término
n de la secuencia de Fibonacci.

Solución:
"""


def fibonacci(n: int) -> int:
    """Devuelve el término n de Fibonacci, tomando F(0)=0 y F(1)=1."""
    if n < 0:
        raise ValueError("n debe ser un entero no negativo.")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    primeros = [fibonacci(n) for n in range(10)]
    print("Primeros términos:", primeros)
    assert primeros == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibonacci(10) == 55

    try:
        fibonacci(-1)
    except ValueError as error:
        print("Entrada no válida:", error)
