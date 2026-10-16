"""
Enunciado:

204. Gestor de Descargas: Crea una clase GestorDescargas que utilice
una cola para gestionar descargas de archivos y una cola de prioridad
para priorizarlas.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Descarga:
    """Solicitud de descarga; un número mayor implica más prioridad."""

    archivo: str
    prioridad: int


@dataclass
class NodoDescarga:
    """Nodo reutilizable en la cola FIFO y la cola de prioridad."""

    descarga: Descarga
    siguiente: NodoDescarga | None = None


class GestorDescargas:
    """Recibe solicitudes FIFO y las despacha por prioridad estable."""

    def __init__(self) -> None:
        self._entrada: NodoDescarga | None = None
        self._final: NodoDescarga | None = None
        self._prioritarias: NodoDescarga | None = None

    def agregar_descarga(self, archivo: str, prioridad: int = 0) -> None:
        """Encola una descarga para su posterior planificación."""
        archivo = archivo.strip()
        if not archivo:
            raise ValueError("El nombre del archivo no puede estar vacío")
        if prioridad < 0:
            raise ValueError("La prioridad no puede ser negativa")
        nuevo = NodoDescarga(Descarga(archivo, prioridad))
        if self._final is None:
            self._entrada = nuevo
        else:
            self._final.siguiente = nuevo
        self._final = nuevo

    def _priorizar_pendientes(self) -> None:
        """Mueve la cola FIFO a una cola ordenada por prioridad."""
        while self._entrada is not None:
            nodo = self._entrada
            self._entrada = nodo.siguiente
            if self._entrada is None:
                self._final = None
            nodo.siguiente = None
            if (self._prioritarias is None or
                    nodo.descarga.prioridad > self._prioritarias.descarga.prioridad):
                nodo.siguiente = self._prioritarias
                self._prioritarias = nodo
                continue
            actual = self._prioritarias
            while (actual.siguiente is not None and
                   actual.siguiente.descarga.prioridad >= nodo.descarga.prioridad):
                actual = actual.siguiente
            nodo.siguiente = actual.siguiente
            actual.siguiente = nodo

    def siguiente_descarga(self) -> Descarga:
        """Extrae la descarga más urgente, conservando FIFO en empates."""
        self._priorizar_pendientes()
        if self._prioritarias is None:
            raise IndexError("No hay descargas pendientes")
        descarga = self._prioritarias.descarga
        self._prioritarias = self._prioritarias.siguiente
        return descarga

    def descargas_pendientes(self) -> list[Descarga]:
        """Consulta el orden de ejecución sin retirar descargas."""
        self._priorizar_pendientes()
        resultado: list[Descarga] = []
        actual = self._prioritarias
        while actual is not None:
            resultado.append(actual.descarga)
            actual = actual.siguiente
        return resultado


if __name__ == "__main__":
    gestor = GestorDescargas()
    gestor.agregar_descarga("manual.pdf", 1)
    gestor.agregar_descarga("informe.csv", 4)
    gestor.agregar_descarga("datos.zip", 4)
    assert gestor.descargas_pendientes() == [
        Descarga("informe.csv", 4), Descarga("datos.zip", 4),
        Descarga("manual.pdf", 1),
    ]
    assert gestor.siguiente_descarga() == Descarga("informe.csv", 4)
    gestor.agregar_descarga("urgente.txt", 10)
    assert gestor.siguiente_descarga() == Descarga("urgente.txt", 10)
    assert gestor.siguiente_descarga() == Descarga("datos.zip", 4)
    assert gestor.siguiente_descarga() == Descarga("manual.pdf", 1)
    assert gestor.descargas_pendientes() == []
    try:
        gestor.siguiente_descarga()
    except IndexError:
        pass
    else:
        raise AssertionError("Una cola vacía debe lanzar IndexError")
    print("Pruebas superadas")
