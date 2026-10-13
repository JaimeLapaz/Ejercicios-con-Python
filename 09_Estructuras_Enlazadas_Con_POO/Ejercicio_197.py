"""
Enunciado:

197. Administrador de Tareas: Crea una clase AdministradorTareas que utilice
    una cola para gestionar tareas pendientes y una lista enlazada para
    llevar un registro de tareas completadas.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator


@dataclass
class Nodo:
    """Nodo de una lista simplemente enlazada."""

    tarea: str
    siguiente: Nodo | None = None


class ListaEnlazada:
    """Lista con inserción al final y extracción por el principio en O(1)."""

    def __init__(self) -> None:
        self._cabeza: Nodo | None = None
        self._cola: Nodo | None = None
        self._longitud = 0

    def agregar(self, tarea: str) -> None:
        nuevo = Nodo(tarea)
        if self._cola is None:
            self._cabeza = nuevo
        else:
            self._cola.siguiente = nuevo
        self._cola = nuevo
        self._longitud += 1

    def extraer_primero(self) -> str:
        if self._cabeza is None:
            raise IndexError("No hay tareas pendientes")
        tarea = self._cabeza.tarea
        self._cabeza = self._cabeza.siguiente
        if self._cabeza is None:
            self._cola = None
        self._longitud -= 1
        return tarea

    def __len__(self) -> int:
        return self._longitud

    def __iter__(self) -> Iterator[str]:
        actual = self._cabeza
        while actual is not None:
            yield actual.tarea
            actual = actual.siguiente


class AdministradorTareas:
    """Gestiona una cola FIFO de pendientes y un historial enlazado."""

    def __init__(self) -> None:
        self._pendientes = ListaEnlazada()
        self._completadas = ListaEnlazada()

    def agregar_tarea(self, tarea: str) -> None:
        """Encola una descripción no vacía."""
        if not isinstance(tarea, str):
            raise TypeError("La tarea debe ser una cadena")
        if not tarea.strip():
            raise ValueError("La tarea no puede estar vacía")
        self._pendientes.agregar(tarea.strip())

    def completar_siguiente(self) -> str:
        """Completa la tarea más antigua y la añade al historial."""
        tarea = self._pendientes.extraer_primero()
        self._completadas.agregar(tarea)
        return tarea

    def tareas_pendientes(self) -> list[str]:
        return list(self._pendientes)

    def tareas_completadas(self) -> list[str]:
        return list(self._completadas)

    def __len__(self) -> int:
        return len(self._pendientes)


if __name__ == "__main__":
    administrador = AdministradorTareas()
    assert len(administrador) == 0
    try:
        administrador.completar_siguiente()
    except IndexError:
        pass
    else:
        raise AssertionError("Una cola vacía debe lanzar IndexError")

    for tarea in ("Estudiar Python", "Resolver ejercicios", "Repasar"):
        administrador.agregar_tarea(tarea)
    assert administrador.tareas_pendientes() == [
        "Estudiar Python", "Resolver ejercicios", "Repasar",
    ]
    assert administrador.completar_siguiente() == "Estudiar Python"
    assert administrador.completar_siguiente() == "Resolver ejercicios"
    assert administrador.tareas_pendientes() == ["Repasar"]
    assert administrador.tareas_completadas() == [
        "Estudiar Python", "Resolver ejercicios",
    ]
    assert administrador.completar_siguiente() == "Repasar"
    administrador.agregar_tarea("Nueva tarea")
    assert administrador.tareas_pendientes() == ["Nueva tarea"]
    try:
        administrador.agregar_tarea("  ")
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba ValueError")
    print("Completadas:", administrador.tareas_completadas())
