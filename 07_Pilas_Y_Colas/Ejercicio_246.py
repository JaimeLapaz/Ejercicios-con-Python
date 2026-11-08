"""
Enunciado:
246. Cola de Notificaciones: Desarrolla una cola de notificaciones para una
aplicación que muestra alertas a los usuarios.

Solución:
Se mantiene una cola FIFO de avisos pendientes con identificadores únicos.
Cada usuario consulta sus avisos en orden de llegada; mostrar un aviso lo
retira de la cola y lo conserva en un historial de entregas.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class Notificacion:
    identificador: int
    usuario: str
    mensaje: str
    creada: datetime


class ColaNotificaciones:
    """Gestiona alertas pendientes por usuario sin perder el orden FIFO."""

    def __init__(self) -> None:
        self._pendientes: deque[Notificacion] = deque()
        self._mostradas: list[Notificacion] = []
        self._siguiente_id = 1

    def enviar(self, usuario: str, mensaje: str) -> Notificacion:
        """Añade una alerta al final de la cola."""
        if not isinstance(usuario, str) or not usuario.strip():
            raise ValueError("El usuario no puede estar vacío")
        if not isinstance(mensaje, str) or not mensaje.strip():
            raise ValueError("El mensaje no puede estar vacío")
        aviso = Notificacion(
            self._siguiente_id, usuario, mensaje, datetime.now(timezone.utc)
        )
        self._siguiente_id += 1
        self._pendientes.append(aviso)
        return aviso

    def mostrar_siguiente(self, usuario: str) -> Notificacion | None:
        """Entrega la primera alerta pendiente del usuario, si existe.

        Mantiene intacto el orden relativo de los avisos de otros usuarios.
        """
        if not isinstance(usuario, str) or not usuario.strip():
            raise ValueError("El usuario no puede estar vacío")
        for indice, aviso in enumerate(self._pendientes):
            if aviso.usuario == usuario:
                del self._pendientes[indice]
                self._mostradas.append(aviso)
                return aviso
        return None

    def pendientes(self, usuario: str | None = None) -> list[Notificacion]:
        """Devuelve una copia de los avisos pendientes, en orden de llegada."""
        return [
            aviso for aviso in self._pendientes
            if usuario is None or aviso.usuario == usuario
        ]

    def historial(self, usuario: str | None = None) -> list[Notificacion]:
        """Devuelve los avisos entregados sin exponer el historial interno."""
        return [
            aviso for aviso in self._mostradas
            if usuario is None or aviso.usuario == usuario
        ]

    def cancelar(self, identificador: int) -> bool:
        """Cancela un aviso aún pendiente; devuelve False si no existe."""
        for indice, aviso in enumerate(self._pendientes):
            if aviso.identificador == identificador:
                del self._pendientes[indice]
                return True
        return False


if __name__ == "__main__":
    cola = ColaNotificaciones()
    uno = cola.enviar("Ana", "Tienes un mensaje")
    dos = cola.enviar("Luis", "Actualización disponible")
    tres = cola.enviar("Ana", "Reunión a las 10")
    assert [n.identificador for n in cola.pendientes()] == [1, 2, 3]
    assert cola.mostrar_siguiente("Ana") == uno
    assert cola.mostrar_siguiente("Ana") == tres
    assert cola.mostrar_siguiente("Ana") is None
    assert cola.pendientes() == [dos]
    assert cola.cancelar(dos.identificador)
    assert not cola.cancelar(dos.identificador)
    assert cola.pendientes() == []
    assert cola.historial("Ana") == [uno, tres]
    try:
        cola.enviar("", "Aviso")
    except ValueError:
        pass
    else:
        raise AssertionError("Debe rechazarse un usuario vacío")
    print("Ejercicio 246: pruebas superadas")
