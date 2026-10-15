"""
Enunciado:

202. Planificador de Tareas: Implementa una clase PlanificadorTareas
que utilice una cola de prioridad para planificar tareas con
diferentes niveles de urgencia.

Solución:
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class NodoTarea:
    descripcion: str
    urgencia: int
    siguiente: NodoTarea | None = None


class PlanificadorTareas:
    """Planificador enlazado: mayor urgencia primero y FIFO en empates."""

    def __init__(self) -> None:
        self._primera: NodoTarea | None = None

    def agregar_tarea(self, descripcion: str, urgencia: int) -> None:
        if not descripcion.strip():
            raise ValueError("La descripción no puede estar vacía")
        if urgencia < 0:
            raise ValueError("La urgencia no puede ser negativa")
        nueva = NodoTarea(descripcion, urgencia)
        if self._primera is None or urgencia > self._primera.urgencia:
            nueva.siguiente = self._primera
            self._primera = nueva
            return
        actual = self._primera
        while actual.siguiente is not None and actual.siguiente.urgencia >= urgencia:
            actual = actual.siguiente
        nueva.siguiente = actual.siguiente
        actual.siguiente = nueva

    def siguiente_tarea(self) -> tuple[str, int]:
        if self._primera is None:
            raise IndexError("No hay tareas pendientes")
        tarea = self._primera
        self._primera = tarea.siguiente
        return tarea.descripcion, tarea.urgencia

    def pendientes(self) -> list[tuple[str, int]]:
        resultado: list[tuple[str, int]] = []
        actual = self._primera
        while actual is not None:
            resultado.append((actual.descripcion, actual.urgencia))
            actual = actual.siguiente
        return resultado


if __name__ == "__main__":
    planificador = PlanificadorTareas()
    planificador.agregar_tarea("Correo", 1)
    planificador.agregar_tarea("Incidencia", 5)
    planificador.agregar_tarea("Reunión", 3)
    planificador.agregar_tarea("Otra incidencia", 5)
    assert planificador.siguiente_tarea() == ("Incidencia", 5)
    assert planificador.siguiente_tarea() == ("Otra incidencia", 5)
    assert planificador.pendientes() == [("Reunión", 3), ("Correo", 1)]
    print("Pruebas superadas")
