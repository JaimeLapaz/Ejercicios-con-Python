"""
Enunciado:

157. Torres de Hanoi: Escribe una función recursiva para resolver
el problema de las Torres de Hanoi con n discos.

Solución:
"""

Movimiento = tuple[str, str]


def resolver_hanoi(
    discos: int,
    origen: str = "A",
    destino: str = "C",
    auxiliar: str = "B",
) -> list[Movimiento]:
    """Devuelve los movimientos para trasladar los discos al destino."""
    if discos < 0:
        raise ValueError("El número de discos no puede ser negativo.")
    if discos == 0:
        return []

    movimientos = resolver_hanoi(discos - 1, origen, auxiliar, destino)
    movimientos.append((origen, destino))
    movimientos.extend(
        resolver_hanoi(discos - 1, auxiliar, destino, origen)
    )
    return movimientos


if __name__ == "__main__":
    movimientos = resolver_hanoi(3)
    for numero, (origen, destino) in enumerate(movimientos, start=1):
        print(f"{numero}: {origen} -> {destino}")

    assert len(movimientos) == 7
    assert movimientos[0] == ("A", "C")
    assert movimientos[-1] == ("A", "C")
    assert resolver_hanoi(0) == []

    try:
        resolver_hanoi(-1)
    except ValueError as error:
        print("Entrada no válida:", error)
