"""
Enunciado:

203. Manejo de Mensajes: Desarrolla una clase ManejoMensajes que utilice
una cola para gestionar mensajes entrantes y una pila para mostrar los
mensajes más recientes.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class NodoMensaje:
    """Nodo de una estructura enlazada de mensajes."""

    texto: str
    siguiente: NodoMensaje | None = None


class ManejoMensajes:
    """Procesa mensajes en orden FIFO y consulta el historial en orden LIFO."""

    def __init__(self) -> None:
        self._primero: NodoMensaje | None = None
        self._ultimo: NodoMensaje | None = None
        self._reciente: NodoMensaje | None = None

    def recibir_mensaje(self, texto: str) -> None:
        """Añade el mensaje a la cola y a la pila de mensajes recibidos."""
        texto = texto.strip()
        if not texto:
            raise ValueError("El mensaje no puede estar vacío")

        nuevo = NodoMensaje(texto)
        if self._ultimo is None:
            self._primero = nuevo
        else:
            self._ultimo.siguiente = nuevo
        self._ultimo = nuevo
        self._reciente = NodoMensaje(texto, self._reciente)

    def procesar_mensaje(self) -> str:
        """Retira el mensaje pendiente más antiguo (FIFO)."""
        if self._primero is None:
            raise IndexError("No hay mensajes pendientes")
        texto = self._primero.texto
        self._primero = self._primero.siguiente
        if self._primero is None:
            self._ultimo = None
        return texto

    def mensajes_recientes(self, limite: int = 5) -> list[str]:
        """Muestra los últimos mensajes recibidos, sin alterar la pila."""
        if limite < 0:
            raise ValueError("El límite no puede ser negativo")
        resultado: list[str] = []
        actual = self._reciente
        while actual is not None and len(resultado) < limite:
            resultado.append(actual.texto)
            actual = actual.siguiente
        return resultado

    def mensajes_pendientes(self) -> list[str]:
        """Devuelve los mensajes en el orden en que se procesarán."""
        resultado: list[str] = []
        actual = self._primero
        while actual is not None:
            resultado.append(actual.texto)
            actual = actual.siguiente
        return resultado


if __name__ == "__main__":
    mensajes = ManejoMensajes()
    mensajes.recibir_mensaje("Hola")
    mensajes.recibir_mensaje("¿Qué tal?")
    mensajes.recibir_mensaje("Hasta luego")
    assert mensajes.mensajes_pendientes() == ["Hola", "¿Qué tal?", "Hasta luego"]
    assert mensajes.mensajes_recientes(2) == ["Hasta luego", "¿Qué tal?"]
    assert mensajes.mensajes_recientes(0) == []
    assert mensajes.procesar_mensaje() == "Hola"
    assert mensajes.mensajes_recientes() == ["Hasta luego", "¿Qué tal?", "Hola"]
    assert mensajes.procesar_mensaje() == "¿Qué tal?"
    assert mensajes.procesar_mensaje() == "Hasta luego"
    assert mensajes.mensajes_pendientes() == []
    try:
        mensajes.procesar_mensaje()
    except IndexError:
        pass
    else:
        raise AssertionError("Una cola vacía debe lanzar IndexError")
    print("Pruebas superadas")
