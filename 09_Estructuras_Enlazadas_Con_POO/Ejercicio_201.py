"""
Enunciado:

201. Ordenamiento con Cola de Prioridad: Diseña una clase
OrdenadorColaPrioridad que utilice una cola de prioridad para ordenar
una lista de elementos.

Solución:
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T", int, float)


@dataclass
class Nodo(Generic[T]):
    valor: T
    siguiente: Nodo[T] | None = None


class OrdenadorColaPrioridad(Generic[T]):
    """Cola de prioridad enlazada, ordenada de menor a mayor."""

    def __init__(self) -> None:
        self._inicio: Nodo[T] | None = None

    def insertar(self, valor: T) -> None:
        nuevo = Nodo(valor)
        if self._inicio is None or valor < self._inicio.valor:
            nuevo.siguiente = self._inicio
            self._inicio = nuevo
            return
        actual = self._inicio
        while actual.siguiente is not None and actual.siguiente.valor <= valor:
            actual = actual.siguiente
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

    def extraer(self) -> T:
        if self._inicio is None:
            raise IndexError("La cola de prioridad está vacía")
        valor = self._inicio.valor
        self._inicio = self._inicio.siguiente
        return valor

    def ordenar(self, elementos: list[T]) -> list[T]:
        """Devuelve una nueva lista ordenada sin modificar la original."""
        cola: OrdenadorColaPrioridad[T] = OrdenadorColaPrioridad()
        for elemento in elementos:
            cola.insertar(elemento)
        resultado: list[T] = []
        while cola._inicio is not None:
            resultado.append(cola.extraer())
        return resultado


if __name__ == "__main__":
    ordenador: OrdenadorColaPrioridad[int] = OrdenadorColaPrioridad()
    numeros = [5, -1, 3, 3, 0]
    assert ordenador.ordenar(numeros) == [-1, 0, 3, 3, 5]
    assert numeros == [5, -1, 3, 3, 0]
    assert ordenador.ordenar([]) == []
    print("Pruebas superadas")
