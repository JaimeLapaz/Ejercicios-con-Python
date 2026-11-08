"""
Enunciado:
247. Editor de Código con Funcionalidad "Deshacer" y "Rehacer":
Implementa un editor de código con funciones de deshacer (undo) y rehacer
(redo) utilizando pilas para mantener el historial de cambios.

Solución:
Cada edición guarda una instantánea anterior en la pila de deshacer.
Deshacer traslada el estado actual a la pila de rehacer y recupera el
anterior; una edición nueva invalida los estados que podían rehacerse.
"""
from __future__ import annotations


class EditorCodigo:
    """Editor de texto con dos pilas de instantáneas de contenido."""

    def __init__(self, contenido: str = "") -> None:
        if not isinstance(contenido, str):
            raise TypeError("El contenido debe ser texto")
        self._contenido = contenido
        self._deshacer: list[str] = []
        self._rehacer: list[str] = []

    @property
    def contenido(self) -> str:
        """Devuelve el código actual."""
        return self._contenido

    def _guardar(self, nuevo: str) -> None:
        if nuevo != self._contenido:
            self._deshacer.append(self._contenido)
            self._contenido = nuevo
            self._rehacer.clear()

    def insertar(self, posicion: int, texto: str) -> None:
        """Inserta texto en un índice válido (incluido el final)."""
        if not isinstance(texto, str):
            raise TypeError("El texto debe ser una cadena")
        self._validar_posicion(posicion, permitir_final=True)
        self._guardar(
            self._contenido[:posicion] + texto + self._contenido[posicion:]
        )

    def eliminar(self, inicio: int, fin: int) -> None:
        """Elimina el intervalo semiabierto [inicio, fin)."""
        self._validar_intervalo(inicio, fin)
        self._guardar(self._contenido[:inicio] + self._contenido[fin:])

    def reemplazar(self, inicio: int, fin: int, texto: str) -> None:
        """Sustituye el intervalo [inicio, fin) por el texto indicado."""
        if not isinstance(texto, str):
            raise TypeError("El texto debe ser una cadena")
        self._validar_intervalo(inicio, fin)
        self._guardar(self._contenido[:inicio] + texto + self._contenido[fin:])

    def _validar_posicion(self, posicion: int, permitir_final: bool) -> None:
        limite = len(self._contenido)
        if type(posicion) is not int or not (
            0 <= posicion <= limite if permitir_final
            else 0 <= posicion < limite
        ):
            raise IndexError("Posición fuera del contenido")

    def _validar_intervalo(self, inicio: int, fin: int) -> None:
        if (type(inicio) is not int or type(fin) is not int
                or not 0 <= inicio <= fin <= len(self._contenido)):
            raise IndexError("Intervalo inválido")

    def deshacer(self) -> bool:
        """Recupera la edición anterior; False si no hay cambios."""
        if not self._deshacer:
            return False
        self._rehacer.append(self._contenido)
        self._contenido = self._deshacer.pop()
        return True

    def rehacer(self) -> bool:
        """Reaplica el último cambio deshecho; False si no existe."""
        if not self._rehacer:
            return False
        self._deshacer.append(self._contenido)
        self._contenido = self._rehacer.pop()
        return True


if __name__ == "__main__":
    editor = EditorCodigo("print('hola')")
    editor.insertar(len(editor.contenido), "\nprint('adiós')")
    assert editor.contenido.endswith("print('adiós')")
    editor.reemplazar(7, 11, "mundo")
    assert editor.contenido.startswith("print('mundo')")
    assert editor.deshacer()
    assert editor.contenido.startswith("print('hola')")
    assert editor.rehacer()
    assert editor.contenido.startswith("print('mundo')")
    editor.eliminar(0, 6)
    assert editor.deshacer()
    assert editor.deshacer()
    editor.insertar(0, "# código\n")
    assert not editor.rehacer()
    assert editor.contenido.startswith("# código")
    try:
        editor.eliminar(100, 101)
    except IndexError:
        pass
    else:
        raise AssertionError("Debe rechazarse un intervalo inválido")
    print("Ejercicio 247: pruebas superadas")
