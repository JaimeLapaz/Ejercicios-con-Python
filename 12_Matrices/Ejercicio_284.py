"""Ejercicio 284 — Ranking de Páginas Web.

Enunciado:
    Implementa el algoritmo PageRank utilizando matrices para calcular
    el ranking de páginas web.

Solución:
    Construir una matriz de transición estocástica por columnas.
    Las páginas sin enlaces salientes distribuyen su peso uniformemente.
    Aplicar el método de la potencia con amortiguación y teletransporte
    hasta que la diferencia entre iteraciones sea suficientemente pequeña.
"""
from collections.abc import Mapping, Sequence
from math import isfinite, isclose


def matriz_transicion(enlaces: Mapping[str, Sequence[str]]) -> tuple[list[str], list[list[float]]]:
    """Devuelve las páginas y la matriz P, donde P[i][j] representa j -> i."""
    paginas = list(enlaces)
    n = len(paginas)
    if not n:
        raise ValueError("Se requiere al menos una página")
    indices = {pagina: i for i, pagina in enumerate(paginas)}
    matriz = [[0.0] * n for _ in range(n)]
    for j, pagina in enumerate(paginas):
        destinos = set(enlaces[pagina])
        if not destinos.issubset(indices):
            raise ValueError("Todos los destinos deben estar registrados")
        if destinos:
            for destino in destinos:
                matriz[indices[destino]][j] = 1.0 / len(destinos)
        else:
            for i in range(n):
                matriz[i][j] = 1.0 / n
    return paginas, matriz


def pagerank(
    enlaces: Mapping[str, Sequence[str]],
    amortiguacion: float = 0.85,
    tolerancia: float = 1e-10,
    max_iteraciones: int = 1000,
) -> dict[str, float]:
    """Calcula puntuaciones cuya suma es uno, ordenadas de mayor a menor.

    Cada iteración cuesta O(n²) con la representación matricial densa.
    """
    if not 0 <= amortiguacion < 1:
        raise ValueError("La amortiguación debe pertenecer a [0, 1)")
    if not isfinite(tolerancia) or tolerancia <= 0:
        raise ValueError("La tolerancia debe ser positiva y finita")
    if max_iteraciones <= 0:
        raise ValueError("Se requiere al menos una iteración")

    paginas, matriz = matriz_transicion(enlaces)
    n = len(paginas)
    rango = [1.0 / n] * n
    teletransporte = (1.0 - amortiguacion) / n

    for _ in range(max_iteraciones):
        nuevo = [
            teletransporte + amortiguacion * sum(
                peso * valor for peso, valor in zip(fila, rango)
            )
            for fila in matriz
        ]
        diferencia = sum(abs(a - b) for a, b in zip(nuevo, rango))
        rango = nuevo
        if diferencia <= tolerancia:
            total = sum(rango)
            orden = sorted(range(n), key=lambda i: (-rango[i], paginas[i]))
            return {paginas[i]: rango[i] / total for i in orden}
    raise RuntimeError("PageRank no convergió dentro del límite de iteraciones")


if __name__ == '__main__':
    red = {"A": ["B", "C"], "B": ["C"], "C": ["A"], "D": []}
    paginas, matriz = matriz_transicion(red)
    assert all(isclose(sum(columna), 1.0) for columna in zip(*matriz))
    resultado = pagerank(red)
    assert isclose(sum(resultado.values()), 1.0)
    assert list(resultado)[0] == "C"
    assert all(valor > 0 for valor in resultado.values())
    # Verificar la ecuación de punto fijo r = dPr + (1-d)/n.
    for i, pagina in enumerate(paginas):
        esperado = 0.15 / len(paginas) + 0.85 * sum(
            matriz[i][j] * resultado[p] for j, p in enumerate(paginas)
        )
        assert isclose(resultado[pagina], esperado, abs_tol=1e-9)
    assert pagerank({"A": []}) == {"A": 1.0}
    assert pagerank({"A": ["B"], "B": ["A"]}) == {"A": 0.5, "B": 0.5}
    assert pagerank(red, amortiguacion=0) == dict.fromkeys(red, 0.25)
    assert matriz_transicion({"A": ["B", "B"], "B": []})[1][1][0] == 1.0
    try:
        pagerank({"A": ["B"]})
    except ValueError:
        pass
    else:
        raise AssertionError("Se aceptó un destino desconocido")
    try:
        pagerank(red, max_iteraciones=1)
    except RuntimeError:
        pass
    else:
        raise AssertionError("Se aceptó una iteración sin convergencia")
    for pagina, puntuacion in resultado.items():
        print(f"{pagina}: {puntuacion:.6f}")
    print("Ejercicio 284: pruebas superadas")
