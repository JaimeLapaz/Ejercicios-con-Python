"""
Enunciado:

198. Simulación de Procesos: Implementa una clase SimulacionProcesos que
    utilice una cola de prioridad para simular la ejecución de procesos
    con diferentes prioridades.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Proceso:
    """Proceso con duración positiva y prioridad numérica."""

    nombre: str
    duracion: int
    prioridad: int


@dataclass
class NodoPrioridad:
    """Nodo de la cola enlazada de procesos."""

    proceso: Proceso
    siguiente: NodoPrioridad | None = None


class ColaPrioridad:
    """Mayor prioridad primero; a igualdad, respeta el orden de llegada."""

    def __init__(self) -> None:
        self._frente: NodoPrioridad | None = None
        self._longitud = 0

    def insertar(self, proceso: Proceso) -> None:
        nuevo = NodoPrioridad(proceso)
        if (self._frente is None
                or proceso.prioridad > self._frente.proceso.prioridad):
            nuevo.siguiente = self._frente
            self._frente = nuevo
        else:
            actual = self._frente
            while (actual.siguiente is not None
                   and actual.siguiente.proceso.prioridad >= proceso.prioridad):
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        self._longitud += 1

    def extraer(self) -> Proceso:
        if self._frente is None:
            raise IndexError("No hay procesos pendientes")
        proceso = self._frente.proceso
        self._frente = self._frente.siguiente
        self._longitud -= 1
        return proceso

    def __len__(self) -> int:
        return self._longitud

    def __iter__(self) -> Iterator[Proceso]:
        actual = self._frente
        while actual is not None:
            yield actual.proceso
            actual = actual.siguiente


class SimulacionProcesos:
    """Simula una CPU no expropiativa, con un proceso cada vez."""

    def __init__(self) -> None:
        self._cola = ColaPrioridad()
        self._tiempo = 0
        self._historial: list[tuple[str, int, int]] = []

    def agregar_proceso(self, nombre: str, duracion: int, prioridad: int) -> None:
        """Añade un proceso; las prioridades más altas se ejecutan antes."""
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser una cadena no vacía")
        if type(duracion) is not int or duracion <= 0:
            raise ValueError("La duración debe ser un entero positivo")
        if type(prioridad) is not int:
            raise TypeError("La prioridad debe ser un entero")
        self._cola.insertar(Proceso(nombre.strip(), duracion, prioridad))

    def ejecutar_siguiente(self) -> tuple[str, int, int]:
        """Ejecuta el proceso prioritario y devuelve (nombre, inicio, fin)."""
        proceso = self._cola.extraer()
        inicio = self._tiempo
        self._tiempo += proceso.duracion
        resultado = (proceso.nombre, inicio, self._tiempo)
        self._historial.append(resultado)
        return resultado

    def ejecutar_todos(self) -> list[tuple[str, int, int]]:
        """Ejecuta los procesos pendientes y devuelve solo esta tanda."""
        resultados = []
        while len(self._cola):
            resultados.append(self.ejecutar_siguiente())
        return resultados

    def pendientes(self) -> list[Proceso]:
        return list(self._cola)

    def historial(self) -> list[tuple[str, int, int]]:
        return self._historial.copy()

    @property
    def tiempo(self) -> int:
        return self._tiempo


if __name__ == "__main__":
    simulacion = SimulacionProcesos()
    for nombre, duracion, prioridad in (
        ("Normal", 4, 1), ("Urgente A", 2, 5),
        ("Urgente B", 3, 5), ("Baja", 1, -1),
    ):
        simulacion.agregar_proceso(nombre, duracion, prioridad)
    assert [p.nombre for p in simulacion.pendientes()] == [
        "Urgente A", "Urgente B", "Normal", "Baja",
    ]
    assert simulacion.ejecutar_todos() == [
        ("Urgente A", 0, 2), ("Urgente B", 2, 5),
        ("Normal", 5, 9), ("Baja", 9, 10),
    ]
    assert simulacion.tiempo == 10 and simulacion.pendientes() == []
    assert simulacion.ejecutar_todos() == []
    simulacion.agregar_proceso("Extra", 2, 0)
    assert simulacion.ejecutar_siguiente() == ("Extra", 10, 12)
    try:
        simulacion.ejecutar_siguiente()
    except IndexError:
        pass
    else:
        raise AssertionError("Se esperaba IndexError")
    try:
        simulacion.agregar_proceso("Inválido", 0, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba ValueError")
    print("Historial:", simulacion.historial())
