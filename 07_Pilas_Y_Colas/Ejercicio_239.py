"""
Enunciado:

239. Cola de Mensajes: Crea una cola de mensajes para un sistema de chat,
     gestionando la entrega y lectura de mensajes.

Solución:
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from enum import Enum


class EstadoMensaje(str, Enum):
    PENDIENTE = "pendiente"
    ENTREGADO = "entregado"
    LEIDO = "leido"


@dataclass(frozen=True)
class Mensaje:
    identificador: int
    remitente: str
    destinatario: str
    texto: str


class ColaMensajes:
    """Gestiona mensajes FIFO por destinatario con estados verificables.

    Enviar encola; entregar mueve el primer pendiente a la bandeja de entrada;
    leer marca el primer entregado como leído. No se permite leer mensajes
    pendientes ni volver a entregar mensajes ya entregados.
    """

    def __init__(self) -> None:
        self._siguiente_id = 1
        self._pendientes: dict[str, deque[int]] = {}
        self._recibidos: dict[str, deque[int]] = {}
        self._mensajes: dict[int, Mensaje] = {}
        self._estados: dict[int, EstadoMensaje] = {}

    def enviar(self, remitente: str, destinatario: str, texto: str) -> Mensaje:
        """Registra un mensaje pendiente y devuelve su identificador."""
        if any(not isinstance(valor, str) or not valor.strip()
               for valor in (remitente, destinatario, texto)):
            raise ValueError("Remitente, destinatario y texto no pueden estar vacíos")
        mensaje = Mensaje(self._siguiente_id, remitente, destinatario, texto)
        self._siguiente_id += 1
        self._mensajes[mensaje.identificador] = mensaje
        self._estados[mensaje.identificador] = EstadoMensaje.PENDIENTE
        self._pendientes.setdefault(destinatario, deque()).append(mensaje.identificador)
        return mensaje

    def entregar(self, destinatario: str) -> Mensaje | None:
        """Entrega el mensaje pendiente más antiguo de ese destinatario."""
        cola = self._pendientes.get(destinatario)
        if not cola:
            return None
        identificador = cola.popleft()
        self._estados[identificador] = EstadoMensaje.ENTREGADO
        self._recibidos.setdefault(destinatario, deque()).append(identificador)
        return self._mensajes[identificador]

    def leer(self, destinatario: str) -> Mensaje | None:
        """Lee el mensaje entregado más antiguo aún sin leer."""
        cola = self._recibidos.get(destinatario)
        if not cola:
            return None
        identificador = cola.popleft()
        self._estados[identificador] = EstadoMensaje.LEIDO
        return self._mensajes[identificador]

    def estado(self, identificador: int) -> EstadoMensaje:
        """Consulta el estado de un mensaje; falla si el ID no existe."""
        return self._estados[identificador]

    def pendientes(self, destinatario: str) -> int:
        return len(self._pendientes.get(destinatario, ()))

    def sin_leer(self, destinatario: str) -> int:
        return len(self._recibidos.get(destinatario, ()))


if __name__ == "__main__":
    chat = ColaMensajes()
    primero = chat.enviar("Ana", "Luis", "Hola")
    segundo = chat.enviar("Marta", "Luis", "¿Qué tal?")
    tercero = chat.enviar("Luis", "Ana", "Bien")
    assert [m.identificador for m in (primero, segundo, tercero)] == [1, 2, 3]
    assert chat.leer("Luis") is None
    assert chat.pendientes("Luis") == 2
    assert chat.entregar("Luis") == primero
    assert chat.entregar("Luis") == segundo
    assert chat.entregar("Luis") is None
    assert chat.sin_leer("Luis") == 2
    assert chat.estado(primero.identificador) == EstadoMensaje.ENTREGADO
    assert chat.leer("Luis") == primero
    assert chat.estado(primero.identificador) == EstadoMensaje.LEIDO
    assert chat.leer("Luis") == segundo
    assert chat.leer("Luis") is None
    assert chat.entregar("Ana") == tercero
    assert chat.leer("Ana") == tercero
    assert chat.pendientes("Ana") == chat.sin_leer("Ana") == 0
    for campos in (("", "Luis", "hola"), ("Ana", "", "hola"), ("Ana", "Luis", " ")):
        try:
            chat.enviar(*campos)
        except ValueError:
            pass
        else:
            raise AssertionError("Se esperaba ValueError")
    try:
        chat.estado(999)
    except KeyError:
        pass
    else:
        raise AssertionError("Se esperaba KeyError")
    print("Ejercicio 239: pruebas superadas")
