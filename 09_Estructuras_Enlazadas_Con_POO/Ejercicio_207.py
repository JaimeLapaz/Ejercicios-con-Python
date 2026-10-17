"""
Enunciado:

207. Planificador de Vuelos: Desarrolla una clase PlanificadorVuelos que
utilice una cola de prioridad para programar vuelos en un aeropuerto
con diferentes horarios de despegue.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone


@dataclass(frozen=True)
class Vuelo:
    """Vuelo con horario de despegue expresado en UTC."""

    codigo: str
    destino: str
    despegue: datetime


@dataclass
class NodoVuelo:
    """Nodo de la cola de prioridad enlazada."""

    vuelo: Vuelo
    siguiente: NodoVuelo | None = None


class PlanificadorVuelos:
    """Planifica por despegue ascendente y mantiene FIFO en empates."""

    def __init__(self) -> None:
        self._primero: NodoVuelo | None = None
        self._codigos: set[str] = set()

    @staticmethod
    def _normalizar(hora: datetime) -> datetime:
        if not isinstance(hora, datetime):
            raise TypeError("El horario debe ser un datetime")
        if hora.tzinfo is None or hora.utcoffset() is None:
            raise ValueError("El horario debe incluir zona horaria")
        return hora.astimezone(timezone.utc)

    def programar_vuelo(self, codigo: str, destino: str, despegue: datetime) -> None:
        """Inserta un vuelo por horario sin perder el orden de los empates."""
        codigo = codigo.strip().upper()
        destino = destino.strip()
        if not codigo or not destino:
            raise ValueError("El código y el destino son obligatorios")
        hora = self._normalizar(despegue)
        if codigo in self._codigos:
            raise ValueError(f"El vuelo {codigo} ya está programado")
        nuevo = NodoVuelo(Vuelo(codigo, destino, hora))
        if self._primero is None or hora < self._primero.vuelo.despegue:
            nuevo.siguiente = self._primero
            self._primero = nuevo
        else:
            actual = self._primero
            while (actual.siguiente is not None and
                   actual.siguiente.vuelo.despegue <= hora):
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        self._codigos.add(codigo)

    def proximo_vuelo(self) -> Vuelo:
        """Consulta el próximo despegue sin eliminarlo."""
        if self._primero is None:
            raise IndexError("No hay vuelos programados")
        return self._primero.vuelo

    def despegar_siguiente(self) -> Vuelo:
        """Retira el vuelo con despegue más temprano."""
        vuelo = self.proximo_vuelo()
        assert self._primero is not None
        self._primero = self._primero.siguiente
        self._codigos.remove(vuelo.codigo)
        return vuelo

    def cancelar_vuelo(self, codigo: str) -> Vuelo:
        """Retira un vuelo por su código o lanza KeyError si no existe."""
        codigo = codigo.strip().upper()
        anterior: NodoVuelo | None = None
        actual = self._primero
        while actual is not None and actual.vuelo.codigo != codigo:
            anterior, actual = actual, actual.siguiente
        if actual is None:
            raise KeyError(f"No existe el vuelo {codigo}")
        if anterior is None:
            self._primero = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        self._codigos.remove(codigo)
        return actual.vuelo

    def reprogramar_vuelo(self, codigo: str, nueva_hora: datetime) -> None:
        """Cambia el horario, preservando los datos del vuelo."""
        hora = self._normalizar(nueva_hora)
        vuelo = self.cancelar_vuelo(codigo)
        self.programar_vuelo(vuelo.codigo, vuelo.destino, hora)

    def vuelos_programados(self) -> list[Vuelo]:
        """Consulta el orden de salida sin modificar la cola."""
        resultado: list[Vuelo] = []
        actual = self._primero
        while actual is not None:
            resultado.append(actual.vuelo)
            actual = actual.siguiente
        return resultado

    def __len__(self) -> int:
        return len(self._codigos)


if __name__ == "__main__":
    planificador = PlanificadorVuelos()
    base = datetime(2026, 10, 17, 10, tzinfo=timezone.utc)
    planificador.programar_vuelo("IB200", "Madrid", base + timedelta(hours=2))
    planificador.programar_vuelo("VY100", "Barcelona", base)
    planificador.programar_vuelo("UX300", "Granada", base)
    assert [v.codigo for v in planificador.vuelos_programados()] == [
        "VY100", "UX300", "IB200"
    ]
    assert planificador.proximo_vuelo().codigo == "VY100"
    planificador.reprogramar_vuelo("IB200", base - timedelta(hours=1))
    assert planificador.despegar_siguiente().codigo == "IB200"
    assert planificador.cancelar_vuelo("UX300").destino == "Granada"
    assert planificador.despegar_siguiente().codigo == "VY100"
    assert len(planificador) == 0
    try:
        planificador.proximo_vuelo()
    except IndexError:
        pass
    else:
        raise AssertionError("La cola vacía debe lanzar IndexError")
    planificador.programar_vuelo("IB200", "Madrid", base)
    try:
        planificador.programar_vuelo("ib200", "Madrid", base)
    except ValueError:
        pass
    else:
        raise AssertionError("Los códigos duplicados deben rechazarse")
    try:
        planificador.reprogramar_vuelo("IB200", datetime(2026, 10, 17))
    except ValueError:
        pass
    else:
        raise AssertionError("Debe rechazarse un horario sin zona")
    assert planificador.proximo_vuelo().despegue == base
    print("Pruebas superadas")
