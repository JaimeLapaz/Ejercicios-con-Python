"""
Enunciado:
244. Cola de Espera en Servidor: Diseña una cola de espera para un servidor
que administra conexiones de clientes concurrentes.

Solución:
Una cola FIFO protegida por Condition permite recibir conexiones desde
varios hilos y atenderlas con un límite de conexiones simultáneas.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from threading import Condition, Thread
from time import monotonic, sleep


@dataclass(frozen=True)
class Conexion:
    identificador: int
    cliente: str
    llegada: float


class Servidor:
    """Cola FIFO segura para hilos con cupo de conexiones activas."""

    def __init__(self, capacidad: int, max_espera: int | None = None) -> None:
        if type(capacidad) is not int or capacidad < 1:
            raise ValueError("La capacidad debe ser positiva")
        if max_espera is not None and (
            type(max_espera) is not int or max_espera < 0
        ):
            raise ValueError("max_espera debe ser no negativo")
        self.capacidad = capacidad
        self.max_espera = max_espera
        self._condicion = Condition()
        self._cola: deque[Conexion] = deque()
        self._activos: dict[int, Conexion] = {}
        self._siguiente_id = 1
        self._cerrado = False

    def conectar(self, cliente: str) -> int:
        """Registra una solicitud; rechaza colas llenas o servidor cerrado."""
        if not isinstance(cliente, str) or not cliente.strip():
            raise ValueError("El cliente debe tener nombre")
        with self._condicion:
            if self._cerrado:
                raise RuntimeError("Servidor cerrado")
            if self.max_espera is not None and len(self._cola) >= self.max_espera:
                raise OverflowError("Cola de espera llena")
            identificador = self._siguiente_id
            self._siguiente_id += 1
            self._cola.append(Conexion(identificador, cliente, monotonic()))
            self._condicion.notify_all()
            return identificador

    def atender(self, timeout: float | None = None) -> Conexion | None:
        """Espera una solicitud y un cupo; None si expira o se cierra."""
        if timeout is not None and timeout < 0:
            raise ValueError("timeout debe ser no negativo")
        limite = None if timeout is None else monotonic() + timeout
        with self._condicion:
            while not (self._cola and len(self._activos) < self.capacidad):
                if self._cerrado and not self._cola:
                    return None
                restante = None if limite is None else limite - monotonic()
                if restante is not None and restante <= 0:
                    return None
                self._condicion.wait(restante)
            conexion = self._cola.popleft()
            self._activos[conexion.identificador] = conexion
            return conexion

    def desconectar(self, identificador: int) -> Conexion:
        """Libera el cupo de una conexión activa."""
        with self._condicion:
            conexion = self._activos.pop(identificador)
            self._condicion.notify_all()
            return conexion

    def cerrar(self) -> None:
        """Impide nuevos clientes; se pueden drenar los pendientes."""
        with self._condicion:
            self._cerrado = True
            self._condicion.notify_all()

    def estado(self) -> tuple[int, int]:
        """Devuelve (pendientes, activos) sin condiciones de carrera."""
        with self._condicion:
            return len(self._cola), len(self._activos)


if __name__ == "__main__":
    servidor = Servidor(capacidad=1, max_espera=3)
    ids = [servidor.conectar(nombre) for nombre in ("Ana", "Luis", "Eva")]
    primero = servidor.atender(timeout=0)
    assert primero is not None and primero.identificador == ids[0]
    assert servidor.estado() == (2, 1)
    assert servidor.atender(timeout=0.01) is None

    atendidos: list[int] = []

    def consumidor() -> None:
        for _ in range(2):
            conexion = servidor.atender(timeout=1)
            assert conexion is not None
            atendidos.append(conexion.identificador)
            servidor.desconectar(conexion.identificador)

    hilo = Thread(target=consumidor)
    hilo.start()
    sleep(0.01)
    servidor.desconectar(ids[0])
    hilo.join(timeout=2)
    assert not hilo.is_alive()
    assert atendidos == ids[1:]
    assert servidor.estado() == (0, 0)
    servidor.cerrar()
    assert servidor.atender(timeout=0) is None
    try:
        servidor.conectar("Otro")
    except RuntimeError:
        pass
    else:
        raise AssertionError("El servidor cerrado debe rechazar clientes")
    print("Ejercicio 244: pruebas superadas")
