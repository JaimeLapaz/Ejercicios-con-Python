"""
Enunciado:

196. Cola de Prioridad con Lista Enlazada: Diseña una clase ColaPrioridad
    utilizando una lista enlazada que permita insertar elementos con
    diferentes prioridades y realizar extracciones basadas en prioridad.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterator, TypeVar

T = TypeVar("T")


@dataclass
class NodoPrioridad(Generic[T]):
    """Nodo de la lista con prioridad y enlace al siguiente."""

    valor: T
    prioridad: int
    siguiente: NodoPrioridad[T] | None = None


class ColaPrioridad(Generic[T]):
    """Cola enlazada con prioridad numérica descendente y orden estable."""

    def __init__(self) -> None:
        self._frente: NodoPrioridad[T] | None = None
        self._longitud = 0

    def insertar(self, valor: T, prioridad: int) -> None:
        """Inserta ordenadamente en O(n), respetando empates por llegada."""
        if not isinstance(prioridad, int) or isinstance(prioridad, bool):
            raise TypeError("La prioridad debe ser un entero")
        nuevo = NodoPrioridad(valor, prioridad)
        if self._frente is None or prioridad > self._frente.prioridad:
            nuevo.siguiente = self._frente
            self._frente = nuevo
        else:
            actual = self._frente
            while (actual.siguiente is not None
                   and actual.siguiente.prioridad >= prioridad):
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        self._longitud += 1

    def extraer(self) -> T:
        """Extrae el valor más prioritario en O(1)."""
        if self._frente is None:
            raise IndexError("La cola de prioridad está vacía")
        valor = self._frente.valor
        self._frente = self._frente.siguiente
        self._longitud -= 1
        return valor

    def consultar(self) -> tuple[T, int]:
        """Consulta el valor y la prioridad sin extraer."""
        if self._frente is None:
            raise IndexError("La cola de prioridad está vacía")
        return self._frente.valor, self._frente.prioridad

    def esta_vacia(self) -> bool:
        return self._frente is None

    def __len__(self) -> int:
        return self._longitud

    def __iter__(self) -> Iterator[tuple[T, int]]:
        actual = self._frente
        while actual is not None:
            yield actual.valor, actual.prioridad
            actual = actual.siguiente


if __name__ == "__main__":
    cola = ColaPrioridad[str]()
    assert cola.esta_vacia() and len(cola) == 0
    for operacion in (cola.extraer, cola.consultar):
        try:
            operacion()
        except IndexError:
            pass
        else:
            raise AssertionError("La cola vacía debe lanzar IndexError")

    for nombre, prioridad in (
        ("normal", 1), ("urgente A", 5), ("baja", -1),
        ("urgente B", 5), ("media", 3),
    ):
        cola.insertar(nombre, prioridad)
    assert list(cola) == [
        ("urgente A", 5), ("urgente B", 5), ("media", 3),
        ("normal", 1), ("baja", -1),
    ]
    assert cola.consultar() == ("urgente A", 5) and len(cola) == 5
    assert [cola.extraer() for _ in range(5)] == [
        "urgente A", "urgente B", "media", "normal", "baja",
    ]
    assert cola.esta_vacia()
    cola.insertar("nuevo", 0)
    assert cola.extraer() == "nuevo"
    try:
        cola.insertar("invalido", 1.5)
    except TypeError:
        pass
    else:
        raise AssertionError("Se esperaba TypeError")
    print("Cola de prioridad vacía:", cola.esta_vacia())
