"""
Enunciado:

112. División segura: Escribe una función que realice una división entre
dos números, pero primero valide que el divisor no sea cero.

Solución:
"""


def dividir(dividendo, divisor) -> float:
    """Valida dos números y realiza una división segura."""
    if (
        isinstance(dividendo, bool)
        or not isinstance(dividendo, (int, float))
        or isinstance(divisor, bool)
        or not isinstance(divisor, (int, float))
    ):
        raise TypeError("El dividendo y el divisor deben ser números.")

    if divisor == 0:
        raise ValueError("El divisor no puede ser cero.")

    return dividendo / divisor


if __name__ == "__main__":
    print(f"10 / 2 = {dividir(10, 2)}")

    try:
        dividir(10, 0)
    except ValueError as error:
        print(f"Error: {error}")
