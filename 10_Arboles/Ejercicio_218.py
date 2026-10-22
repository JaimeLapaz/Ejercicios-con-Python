"""
Enunciado:

218. Árbol de Segmento: Diseña una clase ArbolSegmento que implemente un
    árbol de segmento para consultas de rangos en un arreglo.

Solución:
"""

from __future__ import annotations


class ArbolSegmento:
    """Árbol de segmentos para sumas y actualizaciones puntuales en O(log n).

    Los intervalos de consulta son semiabiertos: [inicio, fin).
    """

    def __init__(self, valores: list[int]) -> None:
        self._n = len(valores)
        self._capacidad = 1
        while self._capacidad < self._n:
            self._capacidad *= 2
        self._arbol = [0] * (2 * self._capacidad)
        for indice, valor in enumerate(valores):
            self._arbol[self._capacidad + indice] = valor
        for indice in range(self._capacidad - 1, 0, -1):
            self._arbol[indice] = (
                self._arbol[2 * indice] + self._arbol[2 * indice + 1]
            )

    def consultar(self, inicio: int, fin: int) -> int:
        """Suma los elementos desde inicio (incluido) hasta fin (excluido)."""
        if not 0 <= inicio <= fin <= self._n:
            raise IndexError("Rango de consulta fuera de los límites")
        izquierda = inicio + self._capacidad
        derecha = fin + self._capacidad
        suma = 0
        while izquierda < derecha:
            if izquierda % 2:
                suma += self._arbol[izquierda]
                izquierda += 1
            if derecha % 2:
                derecha -= 1
                suma += self._arbol[derecha]
            izquierda //= 2
            derecha //= 2
        return suma

    def actualizar(self, indice: int, valor: int) -> None:
        """Sustituye el elemento indicado y actualiza sus antecesores."""
        if not 0 <= indice < self._n:
            raise IndexError("Índice fuera de los límites")
        posicion = self._capacidad + indice
        self._arbol[posicion] = valor
        while posicion > 1:
            posicion //= 2
            self._arbol[posicion] = (
                self._arbol[2 * posicion] + self._arbol[2 * posicion + 1]
            )

    def __len__(self) -> int:
        return self._n


if __name__ == "__main__":
    arbol = ArbolSegmento([2, -1, 4, 7, 3])
    assert arbol.consultar(0, 5) == 15
    assert arbol.consultar(1, 4) == 10
    assert arbol.consultar(2, 2) == 0
    arbol.actualizar(2, 10)
    assert arbol.consultar(1, 4) == 16
    assert arbol.consultar(0, 5) == 21
    assert ArbolSegmento([]).consultar(0, 0) == 0
    for operacion in (lambda: arbol.consultar(-1, 2),
                      lambda: arbol.consultar(3, 6),
                      lambda: arbol.actualizar(5, 0)):
        try:
            operacion()
        except IndexError:
            pass
        else:
            raise AssertionError("Se esperaba IndexError")
    print("Ejercicio 218: pruebas superadas")
