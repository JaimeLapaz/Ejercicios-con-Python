"""
Enunciado:

236. Ordenamiento por Fusión: Escribe una función recursiva para realizar el
    ordenamiento por fusión en una lista.

Solución:
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import TypeVar

T = TypeVar("T")
K = TypeVar("K")


def ordenamiento_por_fusion(
    elementos: Iterable[T], *, clave: Callable[[T], K] | None = None,
    inverso: bool = False,
) -> list[T]:
    """Devuelve una lista ordenada mediante merge sort recursivo y estable.

    La entrada no cambia; las claves se calculan una sola vez.
    Tiempo O(n log n), memoria adicional O(n).
    """
    datos = list(elementos)
    obtener_clave = clave if clave is not None else lambda valor: valor
    decorados = [(obtener_clave(valor), valor) for valor in datos]

    def ordenar(pares: list[tuple[K, T]]) -> list[tuple[K, T]]:
        if len(pares) <= 1:
            return pares
        medio = len(pares) // 2
        izquierda = ordenar(pares[:medio])
        derecha = ordenar(pares[medio:])
        resultado: list[tuple[K, T]] = []
        i = j = 0
        while i < len(izquierda) and j < len(derecha):
            a, b = izquierda[i][0], derecha[j][0]
            # En caso de empate se conserva el orden original.
            elegir_izquierda = (a >= b) if inverso else (a <= b)
            if elegir_izquierda:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        return resultado

    return [valor for _, valor in ordenar(decorados)]


if __name__ == "__main__":
    import random

    assert ordenamiento_por_fusion([]) == []
    assert ordenamiento_por_fusion([7]) == [7]
    assert ordenamiento_por_fusion([5, 2, 4, 2, -1]) == [-1, 2, 2, 4, 5]
    registros = [("a", 2), ("b", 1), ("c", 2), ("d", 1)]
    assert ordenamiento_por_fusion(registros, clave=lambda r: r[1]) == [
        ("b", 1), ("d", 1), ("a", 2), ("c", 2)
    ]
    assert ordenamiento_por_fusion(registros, clave=lambda r: r[1], inverso=True) == [
        ("a", 2), ("c", 2), ("b", 1), ("d", 1)
    ]
    rng = random.Random(236)
    for _ in range(500):
        original = [rng.randint(-50, 50) for _ in range(rng.randrange(100))]
        copia = original[:]
        for inverso in (False, True):
            assert ordenamiento_por_fusion(original, inverso=inverso) == sorted(
                original, reverse=inverso
            )
        assert original == copia
    print("Ejercicio 236: pruebas superadas")
