"""
Enunciado:

123. Número de Fibonacci: Desarrolla una función que calcule el número de Fibonacci
en una posición dada después de validar que la posición sea un número entero no negativo.

Solución:
"""

def fibonacci(posicion: int) -> int:
    """Devuelve el número de Fibonacci situado en la posición indicada."""
    if not isinstance(posicion, int) or isinstance(posicion, bool):
        raise TypeError("La posición debe ser un número entero.")
    if posicion < 0:
        raise ValueError("La posición debe ser un número entero no negativo.")

    anterior, actual = 0, 1
    for _ in range(posicion):
        anterior, actual = actual, anterior + actual
    return anterior


if __name__ == "__main__":
    for posicion in (0, 1, 2, 7, 10):
        print(f"Fibonacci({posicion}) = {fibonacci(posicion)}")
