"""
Enunciado:

205. Simulación de Tráfico: Diseña una clase SimulacionTrafico que
utilice una cola de prioridad para simular el tráfico de vehículos
con diferentes prioridades en una intersección.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Vehiculo:
    """Vehículo esperando paso; mayor prioridad pasa antes."""

    identificador: str
    prioridad: int


@dataclass
class NodoVehiculo:
    """Nodo de una cola de prioridad enlazada."""

    vehiculo: Vehiculo
    siguiente: NodoVehiculo | None = None


class SimulacionTrafico:
    """Gestiona una intersección con prioridad y orden FIFO en empates."""

    def __init__(self) -> None:
        self._primero: NodoVehiculo | None = None

    def llegada(self, identificador: str, prioridad: int = 0) -> None:
        """Incorpora un vehículo en el lugar que le corresponde."""
        identificador = identificador.strip()
        if not identificador:
            raise ValueError("El identificador no puede estar vacío")
        if prioridad < 0:
            raise ValueError("La prioridad no puede ser negativa")
        nuevo = NodoVehiculo(Vehiculo(identificador, prioridad))
        if self._primero is None or prioridad > self._primero.vehiculo.prioridad:
            nuevo.siguiente = self._primero
            self._primero = nuevo
            return
        actual = self._primero
        while (actual.siguiente is not None and
               actual.siguiente.vehiculo.prioridad >= prioridad):
            actual = actual.siguiente
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

    def pasar_siguiente(self) -> Vehiculo:
        """Autoriza el paso del vehículo con mayor prioridad."""
        if self._primero is None:
            raise IndexError("No hay vehículos esperando")
        vehiculo = self._primero.vehiculo
        self._primero = self._primero.siguiente
        return vehiculo

    def orden_de_paso(self) -> list[Vehiculo]:
        """Consulta el orden previsto sin modificar la intersección."""
        resultado: list[Vehiculo] = []
        actual = self._primero
        while actual is not None:
            resultado.append(actual.vehiculo)
            actual = actual.siguiente
        return resultado


if __name__ == "__main__":
    trafico = SimulacionTrafico()
    trafico.llegada("Coche A", 1)
    trafico.llegada("Ambulancia", 10)
    trafico.llegada("Coche B", 1)
    trafico.llegada("Autobús", 3)
    assert trafico.orden_de_paso() == [
        Vehiculo("Ambulancia", 10), Vehiculo("Autobús", 3),
        Vehiculo("Coche A", 1), Vehiculo("Coche B", 1),
    ]
    assert trafico.pasar_siguiente() == Vehiculo("Ambulancia", 10)
    assert trafico.pasar_siguiente() == Vehiculo("Autobús", 3)
    assert trafico.pasar_siguiente() == Vehiculo("Coche A", 1)
    assert trafico.pasar_siguiente() == Vehiculo("Coche B", 1)
    assert trafico.orden_de_paso() == []
    try:
        trafico.pasar_siguiente()
    except IndexError:
        pass
    else:
        raise AssertionError("Una cola vacía debe lanzar IndexError")
    print("Pruebas superadas")
