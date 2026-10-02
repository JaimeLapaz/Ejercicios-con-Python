"""
Enunciado:

152. Cuenta Regresiva: Escribe una función recursiva que muestre una
cuenta regresiva desde un número n hasta 1.

Solución:
"""


def cuenta_regresiva(n: int) -> None:
    """Muestra los enteros desde n hasta 1 usando recursión."""
    if n < 0:
        raise ValueError("n debe ser un entero no negativo.")
    if n == 0:
        return
    print(n)
    cuenta_regresiva(n - 1)


if __name__ == "__main__":
    print("Cuenta regresiva desde 5:")
    cuenta_regresiva(5)
    print("Cuenta regresiva desde 0 (sin salida):")
    cuenta_regresiva(0)

    try:
        cuenta_regresiva(-1)
    except ValueError as error:
        print("Entrada no válida:", error)
