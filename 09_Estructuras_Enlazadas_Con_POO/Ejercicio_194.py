"""
Enunciado:

194. Cola con Listas Enlazadas: Crea una clase Cola utilizando una lista
    enlazada que permita realizar operaciones de encolamiento y desencolamiento.

Solución:
"""

from __future__ import annotations

from typing import Generic, Iterator, TypeVar

from Ejercicio_188 import Nodo

T = TypeVar("T")


class Cola(Generic[T]):
    """Cola FIFO enlazada: encolar y desencolar en O(1)."""

    def __init__(self) -> None:
        self._frente: Nodo[T] | None = None
        self._final: Nodo[T] | None = None
        self._longitud = 0

    def encolar(self, valor: T) -> None:
        """Añade un elemento al final de la cola."""
        nuevo = Nodo(valor)
        if self._final is None:
            self._frente = nuevo
        else:
            self._final.siguiente = nuevo
        self._final = nuevo
        self._longitud += 1

    def desencolar(self) -> T:
        """Retira el primer elemento o lanza IndexError si está vacía."""
        if self._frente is None:
            raise IndexError("No se puede desencolar una cola vacía")
        valor = self._frente.valor
        self._frente = self._frente.siguiente
        if self._frente is None:
            self._final = None
        self._longitud -= 1
        return valor

    def ver_frente(self) -> T:
        """Consulta el primer elemento sin extraerlo."""
        if self._frente is None:
            raise IndexError("La cola está vacía")
        return self._frente.valor

    def esta_vacia(self) -> bool:
        return self._frente is None

    def __len__(self) -> int:
        return self._longitud

    def __iter__(self) -> Iterator[T]:
        """Recorre la cola desde el frente hasta el final."""
        actual = self._frente
        while actual is not None:
            yield actual.valor
            actual = actual.siguiente


if __name__ == "__main__":
    cola = Cola[str]()
    assert cola.esta_vacia() and len(cola) == 0
    for operacion in (cola.desencolar, cola.ver_frente):
        try:
            operacion()
        except IndexError:
            pass
        else:
            raise AssertionError("Una cola vacía debe lanzar IndexError")

    for tarea in ("primera", "segunda", "tercera"):
        cola.encolar(tarea)
    assert list(cola) == ["primera", "segunda", "tercera"]
    assert cola.ver_frente() == "primera" and len(cola) == 3
    assert cola.desencolar() == "primera"
    cola.encolar("cuarta")
    assert list(cola) == ["segunda", "tercera", "cuarta"]
    assert [cola.desencolar() for _ in range(3)] == [
        "segunda", "tercera", "cuarta"
    ]
    assert cola.esta_vacia() and len(cola) == 0
    cola.encolar("reinicio")
    assert cola.desencolar() == "reinicio"
    print("Cola vacía:", cola.esta_vacia())
