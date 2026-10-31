"""
Enunciado:

230. Cálculo de Combinaciones: Desarrolla una función recursiva para calcular
    el número de combinaciones posibles de n elementos tomados de k en k.

Solución:
"""

from __future__ import annotations

from math import comb


def calcular_combinaciones(n: int, k: int) -> int:
    """Calcula C(n, k) recursivamente sin construir todas las combinaciones.

    Utiliza la simetría C(n, k) = C(n, n-k) y la identidad
    C(n, k) = n * C(n-1, k-1) // k, con caso base C(n, 0) = 1.
    Tiempo y profundidad de recursión: O(min(k, n-k)); no usa factoriales.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n debe ser un entero")
    if not isinstance(k, int) or isinstance(k, bool):
        raise TypeError("k debe ser un entero")
    if n < 0 or not 0 <= k <= n:
        raise ValueError("Se requiere n >= 0 y 0 <= k <= n")

    def combinar(total: int, elegidos: int) -> int:
        if elegidos == 0:
            return 1
        return total * combinar(total - 1, elegidos - 1) // elegidos

    return combinar(n, min(k, n - k))


if __name__ == "__main__":
    assert calcular_combinaciones(0, 0) == 1
    assert calcular_combinaciones(5, 0) == 1
    assert calcular_combinaciones(5, 5) == 1
    assert calcular_combinaciones(5, 2) == 10
    assert calcular_combinaciones(10, 3) == 120
    assert calcular_combinaciones(100, 97) == 161700
    for total in range(50):
        for elegidos in range(total + 1):
            assert calcular_combinaciones(total, elegidos) == comb(total, elegidos)
    for argumentos in ((-1, 0), (3, -1), (3, 4)):
        try:
            calcular_combinaciones(*argumentos)
        except ValueError:
            pass
        else:
            raise AssertionError("Se esperaba ValueError")
    for argumentos in ((3.5, 1), (3, True)):
        try:
            calcular_combinaciones(*argumentos)
        except TypeError:
            pass
        else:
            raise AssertionError("Se esperaba TypeError")
    print("Ejercicio 230: pruebas superadas")
