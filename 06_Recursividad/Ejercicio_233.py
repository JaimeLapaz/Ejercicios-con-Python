"""
Enunciado:

233. División Entera: Implementa una función recursiva para realizar
    una división entera de dos números enteros.

Solución:
"""

from __future__ import annotations


def dividir_con_resto(dividendo: int, divisor: int) -> tuple[int, int]:
    """Calcula cociente y resto sin usar /, // ni %.

    Usa división binaria recursiva: al volver de dividir el dividendo
    entre dos, reconstruye el cociente y el resto incorporando su bit
    menos significativo. Aplica el redondeo hacia menos infinito, igual
    que los operadores // y % de Python, incluso con signos distintos.

    Tiempo y profundidad de recursión: O(log(abs(dividendo) + 1)).
    """
    if not isinstance(dividendo, int) or isinstance(dividendo, bool):
        raise TypeError("El dividendo debe ser un entero")
    if not isinstance(divisor, int) or isinstance(divisor, bool):
        raise TypeError("El divisor debe ser un entero")
    if divisor == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")

    magnitud_divisor = abs(divisor)

    def dividir_positivos(numero: int) -> tuple[int, int]:
        if numero == 0:
            return 0, 0
        cociente, resto = dividir_positivos(numero >> 1)
        cociente <<= 1
        resto = (resto << 1) | (numero & 1)
        if resto >= magnitud_divisor:
            return cociente + 1, resto - magnitud_divisor
        return cociente, resto

    cociente, resto = dividir_positivos(abs(dividendo))
    if (dividendo < 0) != (divisor < 0):
        cociente = -cociente - (resto != 0)
    return cociente, dividendo - divisor * cociente


def division_entera(dividendo: int, divisor: int) -> int:
    """Devuelve el cociente entero, con el mismo criterio que a // b."""
    return dividir_con_resto(dividendo, divisor)[0]


if __name__ == "__main__":
    assert dividir_con_resto(17, 5) == (3, 2)
    assert dividir_con_resto(-17, 5) == (-4, 3)
    assert dividir_con_resto(17, -5) == (-4, -3)
    assert dividir_con_resto(-17, -5) == (3, -2)
    assert dividir_con_resto(0, -7) == (0, 0)
    assert division_entera(12, 3) == 4
    for a in range(-100, 101):
        for b in range(-20, 21):
            if b != 0:
                assert dividir_con_resto(a, b) == (a // b, a % b)
                assert division_entera(a, b) == a // b
    grande = 2**256 + 12345
    for a, b in ((grande, 7), (-grande, 7), (grande, -13), (-grande, -13)):
        assert dividir_con_resto(a, b) == (a // b, a % b)
    try:
        division_entera(1, 0)
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("Se esperaba ZeroDivisionError")
    for argumentos in ((True, 2), (3, False), (3.5, 2), (5, "2")):
        try:
            dividir_con_resto(*argumentos)
        except TypeError:
            pass
        else:
            raise AssertionError("Se esperaba TypeError")
    print("Ejercicio 233: pruebas superadas")
