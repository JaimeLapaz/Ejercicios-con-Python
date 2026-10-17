"""
Enunciado:

206. Almacenamiento de Datos: Implementa una clase AlmacenamientoDatos que
utilice una cola de prioridad para almacenar y recuperar datos con
marcas de tiempo.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class Registro(Generic[T]):
    """Dato asociado a una marca de tiempo normalizada a UTC."""

    dato: T
    marca_tiempo: datetime


@dataclass
class NodoRegistro(Generic[T]):
    """Nodo de una cola de prioridad simplemente enlazada."""

    registro: Registro[T]
    siguiente: NodoRegistro[T] | None = None


class AlmacenamientoDatos(Generic[T]):
    """Recupera primero los registros más antiguos, con FIFO en empates."""

    def __init__(self) -> None:
        self._primero: NodoRegistro[T] | None = None
        self._cantidad = 0

    @staticmethod
    def _normalizar(marca_tiempo: datetime) -> datetime:
        """Exige una fecha con zona horaria para ordenar sin ambigüedades."""
        if not isinstance(marca_tiempo, datetime):
            raise TypeError("La marca de tiempo debe ser un datetime")
        if marca_tiempo.tzinfo is None or marca_tiempo.utcoffset() is None:
            raise ValueError("La marca de tiempo debe incluir zona horaria")
        return marca_tiempo.astimezone(timezone.utc)

    def almacenar(self, dato: T, marca_tiempo: datetime) -> None:
        """Inserta el registro por fecha ascendente en una lista enlazada."""
        registro = Registro(dato, self._normalizar(marca_tiempo))
        nuevo = NodoRegistro(registro)
        if (self._primero is None or
                registro.marca_tiempo < self._primero.registro.marca_tiempo):
            nuevo.siguiente = self._primero
            self._primero = nuevo
        else:
            actual = self._primero
            while (actual.siguiente is not None and
                   actual.siguiente.registro.marca_tiempo <= registro.marca_tiempo):
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        self._cantidad += 1

    def consultar_siguiente(self) -> Registro[T]:
        """Consulta el dato más antiguo sin retirarlo."""
        if self._primero is None:
            raise IndexError("No hay registros almacenados")
        return self._primero.registro

    def recuperar(self) -> Registro[T]:
        """Extrae el dato más antiguo de la cola de prioridad."""
        registro = self.consultar_siguiente()
        assert self._primero is not None
        self._primero = self._primero.siguiente
        self._cantidad -= 1
        return registro

    def recuperar_hasta(self, limite: datetime) -> list[Registro[T]]:
        """Extrae todos los registros anteriores o iguales al límite."""
        limite_utc = self._normalizar(limite)
        resultado: list[Registro[T]] = []
        while (self._primero is not None and
               self._primero.registro.marca_tiempo <= limite_utc):
            resultado.append(self.recuperar())
        return resultado

    def pendientes(self) -> list[Registro[T]]:
        """Devuelve una instantánea ordenada sin modificar la cola."""
        resultado: list[Registro[T]] = []
        actual = self._primero
        while actual is not None:
            resultado.append(actual.registro)
            actual = actual.siguiente
        return resultado

    def __len__(self) -> int:
        return self._cantidad


if __name__ == "__main__":
    almacenamiento: AlmacenamientoDatos[str] = AlmacenamientoDatos()
    base = datetime(2026, 10, 17, 10, tzinfo=timezone.utc)
    antes = base - timedelta(hours=1)
    almacenamiento.almacenar("segundo", base)
    almacenamiento.almacenar("primero", antes)
    almacenamiento.almacenar("tercero", base)
    almacenamiento.almacenar("cuarto", base.astimezone(timezone(timedelta(hours=2))))
    assert len(almacenamiento) == 4
    assert almacenamiento.consultar_siguiente().dato == "primero"
    assert [r.dato for r in almacenamiento.recuperar_hasta(antes)] == ["primero"]
    assert [r.dato for r in almacenamiento.pendientes()] == [
        "segundo", "tercero", "cuarto"
    ]
    assert [almacenamiento.recuperar().dato for _ in range(3)] == [
        "segundo", "tercero", "cuarto"
    ]
    assert len(almacenamiento) == 0
    try:
        almacenamiento.recuperar()
    except IndexError:
        pass
    else:
        raise AssertionError("La cola vacía debe lanzar IndexError")
    try:
        almacenamiento.almacenar("sin zona", datetime(2026, 10, 17))
    except ValueError:
        pass
    else:
        raise AssertionError("Debe rechazarse una marca de tiempo sin zona")
    print("Pruebas superadas")
