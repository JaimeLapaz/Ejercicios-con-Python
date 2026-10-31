"""
Enunciado:

231. Recorrido de Laberinto: Escribe una función recursiva que encuentre
    una ruta a través de un laberinto utilizando backtracking.

Solución:
"""

from __future__ import annotations

from typing import Sequence

Coordenada = tuple[int, int]


def encontrar_ruta(
    laberinto: Sequence[Sequence[int]],
    inicio: Coordenada = (0, 0),
    destino: Coordenada | None = None,
) -> list[Coordenada] | None:
    """Encuentra una ruta entre dos casillas mediante DFS recursivo y backtracking.

    Un 0 indica paso libre y un 1 una pared. Se permiten movimientos
    horizontales y verticales; el destino predeterminado es la esquina
    inferior derecha. Devuelve la ruta (incluyendo extremos) o None.
    No modifica el laberinto. Tiempo O(filas * columnas), memoria O(filas * columnas).
    En laberintos muy grandes puede alcanzarse el límite de recursión de Python.
    """
    if not laberinto or not laberinto[0]:
        raise ValueError("El laberinto debe tener al menos una casilla")
    filas, columnas = len(laberinto), len(laberinto[0])
    if any(len(fila) != columnas for fila in laberinto):
        raise ValueError("El laberinto debe ser rectangular")
    if any(casilla not in (0, 1) for fila in laberinto for casilla in fila):
        raise ValueError("Las casillas deben ser 0 (libre) o 1 (pared)")

    if destino is None:
        destino = (filas - 1, columnas - 1)
    for posicion in (inicio, destino):
        if (len(posicion) != 2 or
                any(not isinstance(valor, int) or isinstance(valor, bool)
                    for valor in posicion) or
                not (0 <= posicion[0] < filas and 0 <= posicion[1] < columnas)):
            raise ValueError("Las coordenadas deben estar dentro del laberinto")

    if laberinto[inicio[0]][inicio[1]] == 1 or laberinto[destino[0]][destino[1]] == 1:
        return None

    visitadas: set[Coordenada] = set()
    ruta: list[Coordenada] = []

    def explorar(fila: int, columna: int) -> bool:
        posicion = (fila, columna)
        if (not 0 <= fila < filas or not 0 <= columna < columnas or
                laberinto[fila][columna] == 1 or posicion in visitadas):
            return False
        visitadas.add(posicion)
        ruta.append(posicion)
        if posicion == destino:
            return True
        for df, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if explorar(fila + df, columna + dc):
                return True
        ruta.pop()  # Deshacer la elección al volver de un callejón sin salida.
        return False

    return ruta if explorar(*inicio) else None


if __name__ == "__main__":
    laberinto = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
    ]
    copia = [fila.copy() for fila in laberinto]
    ruta = encontrar_ruta(laberinto)
    assert ruta is not None and ruta[0] == (0, 0) and ruta[-1] == (3, 4)
    assert len(set(ruta)) == len(ruta)
    assert all(laberinto[f][c] == 0 for f, c in ruta)
    assert all(abs(f1 - f2) + abs(c1 - c2) == 1
               for (f1, c1), (f2, c2) in zip(ruta, ruta[1:]))
    assert laberinto == copia
    assert encontrar_ruta([[0]]) == [(0, 0)]
    assert encontrar_ruta([[1]]) is None
    assert encontrar_ruta([[0, 1], [1, 0]]) is None
    assert encontrar_ruta([[0, 0], [0, 0]], (1, 0), (0, 1)) is not None
    for entrada in ([], [[]], [[0], [0, 1]], [[0, 2]]):
        try:
            encontrar_ruta(entrada)
        except ValueError:
            pass
        else:
            raise AssertionError("Se esperaba ValueError")
    try:
        encontrar_ruta([[0]], destino=(2, 0))
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba ValueError")
    print("Ejercicio 231: pruebas superadas")
