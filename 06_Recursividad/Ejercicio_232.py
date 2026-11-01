"""
Enunciado:

232. Árbol de Recursión: Crea una función recursiva que genere un árbol
    de recursión para calcular el n-ésimo término de la secuencia de Fibonacci.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NodoFibonacci:
    """Una llamada a F(n) y las dos llamadas recursivas que realiza."""

    n: int
    resultado: int
    izquierdo: NodoFibonacci | None = None
    derecho: NodoFibonacci | None = None


def generar_arbol_fibonacci(n: int) -> NodoFibonacci:
    """Construye el árbol completo de llamadas para F(n).

    F(0) = 0 y F(1) = 1. Cada nodo interior conserva las llamadas
    F(n-1) y F(n-2), aunque sus subproblemas se repitan: el objetivo
    es representar la recursión, no memorizar resultados.

    Tiempo y espacio O(phi**n), donde phi es la razón áurea.
    Se limita n a 20 para evitar árboles excesivamente grandes.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n debe ser un entero")
    if not 0 <= n <= 20:
        raise ValueError("n debe estar entre 0 y 20")

    def construir(indice: int) -> NodoFibonacci:
        if indice <= 1:
            return NodoFibonacci(indice, indice)
        izquierdo = construir(indice - 1)
        derecho = construir(indice - 2)
        return NodoFibonacci(
            indice, izquierdo.resultado + derecho.resultado, izquierdo, derecho
        )

    return construir(n)


def mostrar_arbol(raiz: NodoFibonacci, profundidad_maxima: int = 3) -> str:
    """Representa las llamadas por niveles, con profundidad acotada.

    La raíz ocupa el nivel 0; «...» indica ramas omitidas.
    """
    if not isinstance(profundidad_maxima, int) or isinstance(profundidad_maxima, bool):
        raise TypeError("profundidad_maxima debe ser un entero")
    if profundidad_maxima < 0:
        raise ValueError("profundidad_maxima no puede ser negativa")

    lineas: list[str] = []

    def recorrer(nodo: NodoFibonacci, nivel: int) -> None:
        lineas.append(f"{'  ' * nivel}F({nodo.n}) = {nodo.resultado}")
        if nodo.izquierdo is None:
            return
        if nivel == profundidad_maxima:
            lineas.append(f"{'  ' * (nivel + 1)}...")
            return
        recorrer(nodo.izquierdo, nivel + 1)
        if nodo.derecho is not None:
            recorrer(nodo.derecho, nivel + 1)

    recorrer(raiz, 0)
    return "\n".join(lineas)


def contar_nodos(raiz: NodoFibonacci | None) -> int:
    """Cuenta las llamadas, incluidas las repetidas, en el árbol."""
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz.izquierdo) + contar_nodos(raiz.derecho)


if __name__ == "__main__":
    assert generar_arbol_fibonacci(0) == NodoFibonacci(0, 0)
    assert generar_arbol_fibonacci(1) == NodoFibonacci(1, 1)
    arbol = generar_arbol_fibonacci(4)
    assert arbol.resultado == 3
    assert arbol.izquierdo is not None and arbol.izquierdo.n == 3
    assert arbol.derecho is not None and arbol.derecho.n == 2
    assert contar_nodos(arbol) == 9
    assert mostrar_arbol(arbol, 0) == "F(4) = 3\n  ..."
    assert "F(2) = 1" in mostrar_arbol(arbol, 2)
    assert contar_nodos(None) == 0

    anterior, actual = 0, 1
    for indice in range(16):
        nodo = generar_arbol_fibonacci(indice)
        assert nodo.resultado == anterior
        anterior, actual = actual, anterior + actual

    for invalido in (-1, 21):
        try:
            generar_arbol_fibonacci(invalido)
        except ValueError:
            pass
        else:
            raise AssertionError("Se esperaba ValueError")
    for invalido in (True, 2.5, "5"):
        try:
            generar_arbol_fibonacci(invalido)
        except TypeError:
            pass
        else:
            raise AssertionError("Se esperaba TypeError")
    try:
        mostrar_arbol(arbol, -1)
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba ValueError")
    print("Ejercicio 232: pruebas superadas")
