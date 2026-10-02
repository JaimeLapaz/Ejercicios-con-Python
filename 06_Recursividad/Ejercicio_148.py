"""
Enunciado:

148. Suma de Números: Escribe una función recursiva que calcule la suma
de los primeros n números naturales.

Solución:
"""


def sumar_naturales(n: int) -> int:
    """Devuelve la suma de los números naturales desde 1 hasta n."""
    if n < 0:
        raise ValueError("n debe ser un entero no negativo.")
    if n == 0:
        return 0
    return n + sumar_naturales(n - 1)


if __name__ == "__main__":
    print("Suma hasta 5:", sumar_naturales(5))
    assert sumar_naturales(0) == 0
    assert sumar_naturales(1) == 1
    assert sumar_naturales(5) == 15

    try:
        sumar_naturales(-1)
    except ValueError as error:
        print("Entrada no válida:", error)
