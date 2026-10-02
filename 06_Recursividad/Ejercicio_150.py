"""
Enunciado:

150. Potencia: Crea una función recursiva que calcule la potencia de
un número dado.

Solución:
"""

Numero = int | float


def potencia(base: Numero, exponente: int) -> Numero:
    """Calcula base elevada a un exponente entero mediante recursión."""
    if exponente == 0:
        return 1
    if exponente < 0:
        if base == 0:
            raise ZeroDivisionError("Cero no admite exponentes negativos.")
        return 1 / potencia(base, -exponente)
    return base * potencia(base, exponente - 1)


if __name__ == "__main__":
    print("2^10 =", potencia(2, 10))
    print("2^-3 =", potencia(2, -3))
    assert potencia(2, 10) == 1024
    assert potencia(5, 0) == 1
    assert potencia(2, -3) == 0.125

    try:
        potencia(0, -1)
    except ZeroDivisionError as error:
        print("Operación no válida:", error)
