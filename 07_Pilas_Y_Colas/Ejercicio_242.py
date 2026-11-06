"""
Enunciado:

242. Cola de Impresión: Implementa una cola de impresión para administrar
     documentos que deben imprimirse, considerando prioridades y tiempos de espera.

Solución:
Se usa un montículo mínimo con prioridad numérica (menor = más urgente)
y orden FIFO en empates. El tiempo de espera se calcula con un reloj
inyectable y puede aplicarse envejecimiento para evitar inanición.
"""

from __future__ import annotations

from dataclasses import dataclass
import heapq
from itertools import count
from time import monotonic
from typing import Callable


@dataclass(frozen=True)
class Documento:
    identificador: int
    nombre: str
    paginas: int
    prioridad: int
    llegada: float


class ColaImpresion:
    """Gestiona documentos pendientes con prioridad y tiempo de espera."""

    def __init__(
        self, reloj: Callable[[], float] = monotonic,
        intervalo_envejecimiento: float | None = None,
    ) -> None:
        if intervalo_envejecimiento is not None and intervalo_envejecimiento <= 0:
            raise ValueError("El intervalo de envejecimiento debe ser positivo")
        self._reloj = reloj
        self._intervalo = intervalo_envejecimiento
        self._secuencia = count(1)
        self._pendientes: dict[int, Documento] = {}
        self._heap: list[tuple[int, int]] = []

    def agregar(self, nombre: str, paginas: int, prioridad: int = 5) -> int:
        """Encola un documento y devuelve su identificador único."""
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if type(paginas) is not int or paginas <= 0:
            raise ValueError("Las páginas deben ser un entero positivo")
        if type(prioridad) is not int or prioridad < 0:
            raise ValueError("La prioridad debe ser un entero no negativo")
        identificador = next(self._secuencia)
        documento = Documento(
            identificador, nombre, paginas, prioridad, self._reloj()
        )
        self._pendientes[identificador] = documento
        heapq.heappush(self._heap, (prioridad, identificador))
        return identificador

    def cancelar(self, identificador: int) -> Documento:
        """Cancela un trabajo; las entradas obsoletas se ignoran al extraer."""
        return self._pendientes.pop(identificador)

    def _elegir(self, ahora: float) -> Documento:
        if not self._pendientes:
            raise IndexError("No hay documentos pendientes")
        if self._intervalo is not None:
            # El envejecimiento modifica la prioridad efectiva con el tiempo.
            return min(
                self._pendientes.values(),
                key=lambda d: (
                    d.prioridad - int(max(0.0, ahora - d.llegada) // self._intervalo),
                    d.identificador,
                ),
            )
        while self._heap and self._heap[0][1] not in self._pendientes:
            heapq.heappop(self._heap)
        return self._pendientes[self._heap[0][1]]

    def siguiente(self) -> tuple[Documento, float]:
        """Consulta el siguiente trabajo y los segundos que lleva esperando."""
        ahora = self._reloj()
        documento = self._elegir(ahora)
        return documento, max(0.0, ahora - documento.llegada)

    def imprimir(self) -> tuple[Documento, float]:
        """Retira el próximo documento e informa de su espera."""
        documento, espera = self.siguiente()
        del self._pendientes[documento.identificador]
        return documento, espera

    def __len__(self) -> int:
        return len(self._pendientes)


if __name__ == "__main__":
    tiempo = [100.0]
    cola = ColaImpresion(reloj=lambda: tiempo[0])
    primero = cola.agregar("Informe", 4, prioridad=3)
    segundo = cola.agregar("Factura", 1, prioridad=1)
    tercero = cola.agregar("Carta", 2, prioridad=1)
    tiempo[0] += 12
    assert cola.siguiente()[0].identificador == segundo
    assert cola.imprimir()[1] == 12
    assert cola.imprimir()[0].identificador == tercero
    assert cola.imprimir()[0].identificador == primero
    assert len(cola) == 0
    try:
        cola.imprimir()
    except IndexError:
        pass
    else:
        raise AssertionError("Se esperaba IndexError")
    antigua = ColaImpresion(reloj=lambda: tiempo[0], intervalo_envejecimiento=5)
    vieja = antigua.agregar("Antiguo", 1, prioridad=6)
    tiempo[0] += 30
    antigua.agregar("Urgente", 1, prioridad=1)
    assert antigua.imprimir()[0].identificador == vieja
    cancelada = antigua.agregar("Cancelar", 1)
    assert antigua.cancelar(cancelada).nombre == "Cancelar"
    print("Ejercicio 242: pruebas superadas")
