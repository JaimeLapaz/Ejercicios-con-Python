"""
Enunciado:

237. Recorrido en Laberinto 3D: Crea una función recursiva que encuentre una
    ruta a través de un laberinto tridimensional.

Solución:
"""

from __future__ import annotations

from collections.abc import Sequence

Coordenada = tuple[int, int, int]  # (nivel, fila, columna)
Laberinto = Sequence[Sequence[Sequence[int]]]


def encontrar_ruta_3d(
    laberinto: Laberinto, inicio: Coordenada, destino: Coordenada
) -> list[Coordenada] | None:
    """Busca una ruta mediante DFS recursivo entre celdas libres (0).

    Se permiten seis movimientos ortogonales. Las celdas 1 son paredes.
    Devuelve una ruta con ambos extremos o None. No modifica el laberinto.
    Tiempo O(niveles * filas * columnas), sin garantía de ruta mínima.
    """
    if not laberinto or not laberinto[0] or not laberinto[0][0]:
        raise ValueError("El laberinto debe tener dimensiones positivas")
    niveles, filas, columnas = len(laberinto), len(laberinto[0]), len(laberinto[0][0])
    if any(
        len(plano) != filas or any(len(fila) != columnas for fila in plano)
        for plano in laberinto
    ):
        raise ValueError("El laberinto debe ser rectangular en las tres dimensiones")
    if any(celda not in (0, 1) for plano in laberinto for fila in plano for celda in fila):
        raise ValueError("Solo se admiten celdas 0 (libre) y 1 (pared)")

    def valida(posicion: Coordenada) -> bool:
        return (
            isinstance(posicion, tuple)
            and len(posicion) == 3
            and all(isinstance(v, int) and not isinstance(v, bool) for v in posicion)
            and 0 <= posicion[0] < niveles
            and 0 <= posicion[1] < filas
            and 0 <= posicion[2] < columnas
        )

    if not valida(inicio) or not valida(destino):
        raise ValueError("Inicio y destino deben ser coordenadas válidas")
    if laberinto[inicio[0]][inicio[1]][inicio[2]] != 0:
        return None
    if laberinto[destino[0]][destino[1]][destino[2]] != 0:
        return None

    visitadas: set[Coordenada] = set()
    movimientos = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0),
                   (0, 0, 1), (0, 0, -1))

    def explorar(actual: Coordenada) -> list[Coordenada] | None:
        if actual == destino:
            return [actual]
        visitadas.add(actual)
        for dn, df, dc in movimientos:
            siguiente = (actual[0] + dn, actual[1] + df, actual[2] + dc)
            if (
                valida(siguiente)
                and siguiente not in visitadas
                and laberinto[siguiente[0]][siguiente[1]][siguiente[2]] == 0
            ):
                ruta = explorar(siguiente)
                if ruta is not None:
                    return [actual] + ruta
        return None

    return explorar(inicio)


if __name__ == "__main__":
    from collections import deque
    import random

    ejemplo = [[[0, 1], [0, 1]], [[0, 0], [1, 0]]]
    ruta = encontrar_ruta_3d(ejemplo, (0, 0, 0), (1, 1, 1))
    assert ruta is not None and ruta[0] == (0, 0, 0) and ruta[-1] == (1, 1, 1)
    assert all(sum(abs(a - b) for a, b in zip(p, q)) == 1 for p, q in zip(ruta, ruta[1:]))
    assert encontrar_ruta_3d([[[0]]], (0, 0, 0), (0, 0, 0)) == [(0, 0, 0)]
    assert encontrar_ruta_3d([[[0, 1, 0]]], (0, 0, 0), (0, 0, 2)) is None
    for invalido in ([], [[[]]], [[[0], [0, 1]]], [[[2]]]):
        try:
            encontrar_ruta_3d(invalido, (0, 0, 0), (0, 0, 0))
        except ValueError:
            pass
        else:
            raise AssertionError("Se esperaba ValueError")

    rng = random.Random(237)
    for _ in range(300):
        n, f, c = (rng.randint(1, 4) for _ in range(3))
        mapa = [[[int(rng.randrange(3) == 0) for _ in range(c)]
                 for _ in range(f)] for _ in range(n)]
        origen, meta = (0, 0, 0), (n - 1, f - 1, c - 1)
        ruta = encontrar_ruta_3d(mapa, origen, meta)
        cola = deque([origen])
        vistos = {origen}
        while cola:
            z, y, x = cola.popleft()
            for dz, dy, dx in ((1, 0, 0), (-1, 0, 0), (0, 1, 0),
                               (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                vecino = (z + dz, y + dy, x + dx)
                a, b, d = vecino
                if (0 <= a < n and 0 <= b < f and 0 <= d < c
                        and mapa[a][b][d] == 0 and vecino not in vistos):
                    vistos.add(vecino)
                    cola.append(vecino)
        existe = mapa[0][0][0] == 0 and meta in vistos and mapa[meta[0]][meta[1]][meta[2]] == 0
        assert (ruta is not None) == existe
        if ruta:
            assert ruta[0] == origen and ruta[-1] == meta
            assert len(ruta) == len(set(ruta))
            assert all(mapa[z][y][x] == 0 for z, y, x in ruta)
            assert all(sum(abs(a - b) for a, b in zip(p, q)) == 1 for p, q in zip(ruta, ruta[1:]))
    print("Ejercicio 237: pruebas superadas")
