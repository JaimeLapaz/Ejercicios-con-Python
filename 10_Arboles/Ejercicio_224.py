"""
Enunciado:

224. Árbol KD: Implementa una clase ArbolKD para representar un árbol KD
    (árbol binario de búsqueda en k dimensiones) y realizar consultas en
    espacios multidimensionales.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Iterable, Sequence

Punto = tuple[float, ...]


@dataclass
class NodoKD:
    """Nodo que divide el espacio por una coordenada distinta en cada nivel."""

    punto: Punto
    izquierdo: NodoKD | None = None
    derecho: NodoKD | None = None


class ArbolKD:
    """Árbol KD para puntos únicos de k dimensiones.

    La construcción inicial utiliza medianas para equilibrar el árbol.
    Las consultas por rango son inclusivas y las distancias, euclídeas.
    """

    def __init__(
        self, dimensiones: int, puntos: Iterable[Sequence[float]] = ()
    ) -> None:
        if isinstance(dimensiones, bool) or not isinstance(dimensiones, int):
            raise TypeError("El número de dimensiones debe ser un entero")
        if dimensiones <= 0:
            raise ValueError("El número de dimensiones debe ser positivo")
        self.dimensiones = dimensiones
        normalizados = {self._normalizar(punto) for punto in puntos}
        self.raiz = self._construir(list(normalizados), 0)
        self._cantidad = len(normalizados)

    def _normalizar(self, punto: Sequence[float]) -> Punto:
        """Valida las coordenadas y devuelve una tupla inmutable."""
        coordenadas = tuple(punto)
        if len(coordenadas) != self.dimensiones:
            raise ValueError("El punto no tiene las dimensiones esperadas")
        for valor in coordenadas:
            if isinstance(valor, bool) or not isinstance(valor, (int, float)):
                raise TypeError("Cada coordenada debe ser un número real")
        resultado = tuple(float(valor) for valor in coordenadas)
        if not all(isfinite(valor) for valor in resultado):
            raise ValueError("Las coordenadas deben ser finitas")
        return resultado

    def _construir(self, puntos: list[Punto], profundidad: int) -> NodoKD | None:
        if not puntos:
            return None
        eje = profundidad % self.dimensiones
        puntos.sort(key=lambda punto: (punto[eje], punto))
        medio = len(puntos) // 2
        return NodoKD(
            puntos[medio],
            self._construir(puntos[:medio], profundidad + 1),
            self._construir(puntos[medio + 1 :], profundidad + 1),
        )

    def insertar(self, punto: Sequence[float]) -> bool:
        """Inserta un punto nuevo; devuelve False si ya existe."""
        objetivo = self._normalizar(punto)
        if self.raiz is None:
            self.raiz = NodoKD(objetivo)
            self._cantidad += 1
            return True
        actual = self.raiz
        profundidad = 0
        while True:
            if actual.punto == objetivo:
                return False
            eje = profundidad % self.dimensiones
            izquierda = (objetivo[eje], objetivo) < (actual.punto[eje], actual.punto)
            siguiente = actual.izquierdo if izquierda else actual.derecho
            if siguiente is None:
                if izquierda:
                    actual.izquierdo = NodoKD(objetivo)
                else:
                    actual.derecho = NodoKD(objetivo)
                self._cantidad += 1
                return True
            actual = siguiente
            profundidad += 1

    def buscar(self, punto: Sequence[float]) -> bool:
        """Comprueba si el punto exacto pertenece al árbol."""
        objetivo = self._normalizar(punto)
        actual = self.raiz
        profundidad = 0
        while actual is not None:
            if actual.punto == objetivo:
                return True
            eje = profundidad % self.dimensiones
            if (objetivo[eje], objetivo) < (actual.punto[eje], actual.punto):
                actual = actual.izquierdo
            else:
                actual = actual.derecho
            profundidad += 1
        return False

    def buscar_rango(
        self, minimos: Sequence[float], maximos: Sequence[float]
    ) -> list[Punto]:
        """Lista ordenada de puntos en el hiperrrectángulo cerrado indicado."""
        inferior = self._normalizar(minimos)
        superior = self._normalizar(maximos)
        if any(a > b for a, b in zip(inferior, superior)):
            raise ValueError("Cada mínimo debe ser menor o igual a su máximo")
        encontrados: list[Punto] = []

        def recorrer(nodo: NodoKD | None, profundidad: int) -> None:
            if nodo is None:
                return
            if all(a <= x <= b for a, x, b in zip(inferior, nodo.punto, superior)):
                encontrados.append(nodo.punto)
            eje = profundidad % self.dimensiones
            if inferior[eje] <= nodo.punto[eje]:
                recorrer(nodo.izquierdo, profundidad + 1)
            if superior[eje] >= nodo.punto[eje]:
                recorrer(nodo.derecho, profundidad + 1)

        recorrer(self.raiz, 0)
        return sorted(encontrados)

    def vecino_mas_cercano(self, punto: Sequence[float]) -> Punto | None:
        """Devuelve el vecino más cercano, o None si el árbol está vacío.

        En caso de empate elige el punto lexicográficamente menor.
        La poda usa la distancia al hiperplano de división.
        """
        objetivo = self._normalizar(punto)
        mejor: Punto | None = None
        mejor_distancia = float("inf")

        def distancia_cuadrada(otro: Punto) -> float:
            return sum((a - b) ** 2 for a, b in zip(objetivo, otro))

        def recorrer(nodo: NodoKD | None, profundidad: int) -> None:
            nonlocal mejor, mejor_distancia
            if nodo is None:
                return
            distancia = distancia_cuadrada(nodo.punto)
            if (mejor is None or distancia < mejor_distancia
                    or (distancia == mejor_distancia and nodo.punto < mejor)):
                mejor = nodo.punto
                mejor_distancia = distancia
            eje = profundidad % self.dimensiones
            diferencia = objetivo[eje] - nodo.punto[eje]
            cercano, lejano = (
                (nodo.izquierdo, nodo.derecho) if diferencia < 0
                else (nodo.derecho, nodo.izquierdo)
            )
            recorrer(cercano, profundidad + 1)
            if diferencia ** 2 <= mejor_distancia:
                recorrer(lejano, profundidad + 1)

        recorrer(self.raiz, 0)
        return mejor

    def __len__(self) -> int:
        return self._cantidad


if __name__ == "__main__":
    arbol = ArbolKD(2, [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)])
    assert len(arbol) == 6
    assert arbol.buscar((5, 4)) and not arbol.buscar((3, 4))
    assert arbol.buscar_rango((2, 2), (7, 4)) == [(2.0, 3.0), (5.0, 4.0), (7.0, 2.0)]
    assert arbol.vecino_mas_cercano((9, 2)) == (8.0, 1.0)
    assert arbol.insertar((3, 4)) and not arbol.insertar((3, 4))
    assert arbol.buscar((3, 4)) and len(arbol) == 7
    assert ArbolKD(3).vecino_mas_cercano((1, 2, 3)) is None
    assert ArbolKD(1, [(1,), (-1,)]).vecino_mas_cercano((0,)) == (-1.0,)
    try:
        arbol.buscar((1, 2, 3))
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba ValueError por dimensión incorrecta")
    print("Ejercicio 224: pruebas superadas")
