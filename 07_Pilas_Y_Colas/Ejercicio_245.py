"""
Enunciado:
245. Pila de Navegación de Laberinto: Encuentra una ruta a través de un
laberinto utilizando una pila para seguir las ubicaciones visitadas.

Solución:
Se utiliza búsqueda en profundidad iterativa (DFS). Cada posición pendiente
se almacena en una pila junto con su predecesora; se reconstruye la ruta
cuando se alcanza la salida. No se modifica el laberinto original.
"""
from __future__ import annotations

from collections.abc import Sequence

Posicion = tuple[int, int]
Laberinto = Sequence[Sequence[int]]


def encontrar_ruta(
    laberinto: Laberinto, inicio: Posicion, fin: Posicion
) -> list[Posicion] | None:
    """Devuelve una ruta de celdas libres (0) o None si no existe.

    Solo se permiten movimientos ortogonales; 1 representa una pared.
    """
    if not laberinto or not laberinto[0]:
        raise ValueError("El laberinto no puede estar vacío")
    filas, columnas = len(laberinto), len(laberinto[0])
    if any(len(fila) != columnas for fila in laberinto):
        raise ValueError("El laberinto debe ser rectangular")
    if any(celda not in (0, 1) for fila in laberinto for celda in fila):
        raise ValueError("Solo se admiten celdas 0 y 1")
    for posicion in (inicio, fin):
        if (not isinstance(posicion, tuple) or len(posicion) != 2
            or any(type(coordenada) is not int for coordenada in posicion)):
            raise ValueError("Las posiciones deben ser tuplas de dos enteros")
        f, c = posicion
        if not (0 <= f < filas and 0 <= c < columnas):
            raise ValueError("Posición fuera del laberinto")
    if laberinto[inicio[0]][inicio[1]] or laberinto[fin[0]][fin[1]]:
        return None

    pila: list[Posicion] = [inicio]
    anteriores: dict[Posicion, Posicion | None] = {inicio: None}
    while pila:
        actual = pila.pop()
        if actual == fin:
            ruta: list[Posicion] = []
            paso: Posicion | None = fin
            while paso is not None:
                ruta.append(paso)
                paso = anteriores[paso]
            return ruta[::-1]
        fila, columna = actual
        for df, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            vecino = (fila + df, columna + dc)
            f, c = vecino
            if (0 <= f < filas and 0 <= c < columnas
                and laberinto[f][c] == 0 and vecino not in anteriores):
                anteriores[vecino] = actual
                pila.append(vecino)
    return None


if __name__ == "__main__":
    mapa = [
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
    ]
    copia = [fila[:] for fila in mapa]
    ruta = encontrar_ruta(mapa, (0, 0), (3, 3))
    assert ruta is not None and ruta[0] == (0, 0) and ruta[-1] == (3, 3)
    assert all(mapa[f][c] == 0 for f, c in ruta)
    assert all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1
               for a, b in zip(ruta, ruta[1:]))
    assert mapa == copia
    assert encontrar_ruta([[0, 1], [1, 0]], (0, 0), (1, 1)) is None
    assert encontrar_ruta([[0]], (0, 0), (0, 0)) == [(0, 0)]
    try:
        encontrar_ruta([[0], [0, 1]], (0, 0), (1, 0))
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba ValueError para matriz irregular")
    print("Ejercicio 245: pruebas superadas")
