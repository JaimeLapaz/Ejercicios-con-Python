"""
Enunciado:

156. Máximo Común Divisor: Desarrolla una función recursiva para
calcular el máximo común divisor (MCD) de dos números.

Solución:
"""


def maximo_comun_divisor(a: int, b: int) -> int:
    """Calcula el MCD mediante el algoritmo recursivo de Euclides."""
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return maximo_comun_divisor(b, a % b)


if __name__ == "__main__":
    casos = [
        (48, 18, 6),
        (54, 24, 6),
        (17, 13, 1),
        (-42, 56, 14),
        (0, 9, 9),
    ]

    for a, b, esperado in casos:
        resultado = maximo_comun_divisor(a, b)
        print(f"MCD({a}, {b}) = {resultado}")
        assert resultado == esperado

    assert maximo_comun_divisor(0, 0) == 0
