"""
Enunciado:

240. Cola de Prioridad Dinámica: Diseña una cola de prioridad que permita
     cambiar la prioridad de los elementos en tiempo real.

Solución:
Se utiliza un montículo mínimo con entradas versionadas. Las prioridades
menores se atienden antes; en empates se conserva el orden de inserción.
Las entradas obsoletas se descartan al extraer.
"""

from __future__ import annotations

import heapq
from itertools import count
from typing import Generic, Hashable, TypeVar

T = TypeVar("T", bound=Hashable)


class ColaPrioridadDinamica(Generic[T]):
    """Cola con inserción, actualización, cancelación y extracción prioritarias."""

    def __init__(self) -> None:
        self._heap: list[tuple[int, int, int, T]] = []
        self._vigentes: dict[T, tuple[int, int, int]] = {}
        self._orden = count()
        self._version = count()

    def agregar(self, elemento: T, prioridad: int) -> None:
        """Añade un elemento nuevo, sin permitir identificadores repetidos."""
        if not isinstance(prioridad, int) or isinstance(prioridad, bool):
            raise TypeError("La prioridad debe ser un entero")
        if elemento in self._vigentes:
            raise ValueError("El elemento ya existe; utiliza cambiar_prioridad")
        orden, version = next(self._orden), next(self._version)
        self._vigentes[elemento] = (prioridad, orden, version)
        heapq.heappush(self._heap, (prioridad, orden, version, elemento))

    def cambiar_prioridad(self, elemento: T, prioridad: int) -> None:
        """Actualiza la prioridad conservando el orden original en empates."""
        if not isinstance(prioridad, int) or isinstance(prioridad, bool):
            raise TypeError("La prioridad debe ser un entero")
        _, orden, _ = self._vigentes[elemento]
        version = next(self._version)
        self._vigentes[elemento] = (prioridad, orden, version)
        heapq.heappush(self._heap, (prioridad, orden, version, elemento))

    def cancelar(self, elemento: T) -> None:
        """Elimina lógicamente un elemento; KeyError si no existe."""
        del self._vigentes[elemento]

    def _descartar_obsoletos(self) -> None:
        while self._heap:
            prioridad, orden, version, elemento = self._heap[0]
            if self._vigentes.get(elemento) == (prioridad, orden, version):
                return
            heapq.heappop(self._heap)

    def siguiente(self) -> tuple[T, int]:
        """Consulta el próximo elemento sin retirarlo."""
        self._descartar_obsoletos()
        if not self._heap:
            raise IndexError("La cola está vacía")
        prioridad, _, _, elemento = self._heap[0]
        return elemento, prioridad

    def extraer(self) -> tuple[T, int]:
        """Extrae el elemento vigente de mayor prioridad."""
        elemento, prioridad = self.siguiente()
        heapq.heappop(self._heap)
        del self._vigentes[elemento]
        return elemento, prioridad

    def __len__(self) -> int:
        return len(self._vigentes)

    def __bool__(self) -> bool:
        return bool(self._vigentes)


if __name__ == "__main__":
    cola = ColaPrioridadDinamica[str]()
    cola.agregar("informe", 5)
    cola.agregar("correo", 2)
    cola.agregar("copia", 2)
    assert cola.siguiente() == ("correo", 2)
    cola.cambiar_prioridad("informe", 1)
    assert cola.extraer() == ("informe", 1)
    cola.cambiar_prioridad("copia", 0)
    cola.cancelar("correo")
    assert cola.extraer() == ("copia", 0)
    assert len(cola) == 0
    cola.agregar("correo", 3)
    assert cola.extraer() == ("correo", 3)
    try:
        cola.extraer()
    except IndexError:
        pass
    else:
        raise AssertionError("Se esperaba IndexError")
    try:
        cola.cambiar_prioridad("desconocido", 1)
    except KeyError:
        pass
    else:
        raise AssertionError("Se esperaba KeyError")
    print("Ejercicio 240: pruebas superadas")
