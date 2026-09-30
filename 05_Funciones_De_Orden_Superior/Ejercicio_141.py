"""
Enunciado:

141. Filtrado de Fechas: Implementa una función de orden superior que
tome una lista de fechas y una función de filtro basada en una
condición de fecha, y devuelva las fechas que cumplan la condición.

Solución:
"""

from collections.abc import Callable
from datetime import date


def filtrar_fechas(
    fechas: list[date], condicion: Callable[[date], bool]
) -> list[date]:
    """Selecciona las fechas que cumplen la condición sin alterar la lista."""
    return [fecha for fecha in fechas if condicion(fecha)]


if __name__ == "__main__":
    fechas = [
        date(2025, 12, 31),
        date(2026, 1, 15),
        date(2026, 7, 1),
        date(2027, 2, 10),
    ]
    desde_2026 = filtrar_fechas(
        fechas, lambda fecha: fecha >= date(2026, 1, 1)
    )
    solo_2026 = filtrar_fechas(fechas, lambda fecha: fecha.year == 2026)

    print("Desde 2026:", desde_2026)
    print("Solo 2026:", solo_2026)
    assert desde_2026 == fechas[1:]
    assert solo_2026 == fechas[1:3]
