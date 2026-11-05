"""
Enunciado:

241. Editor de Texto Undo/Redo: Desarrolla un editor de texto con las
     funciones deshacer (undo) y rehacer (redo) utilizando pilas.

Solución:
Cada edición guarda el estado anterior en una pila de deshacer y limpia
la pila de rehacer. Deshacer y rehacer intercambian instantáneas entre
ambas pilas, sin perder el contenido original.
"""

from __future__ import annotations


class EditorTexto:
    """Editor sencillo basado en dos pilas de estados de texto."""

    def __init__(self, texto: str = "") -> None:
        if not isinstance(texto, str):
            raise TypeError("El texto inicial debe ser una cadena")
        self._texto = texto
        self._deshacer: list[str] = []
        self._rehacer: list[str] = []

    @property
    def texto(self) -> str:
        return self._texto

    def _aplicar(self, nuevo_texto: str) -> None:
        if nuevo_texto != self._texto:
            self._deshacer.append(self._texto)
            self._texto = nuevo_texto
            self._rehacer.clear()

    def insertar(self, posicion: int, contenido: str) -> None:
        """Inserta contenido antes de la posición indicada."""
        if not isinstance(contenido, str):
            raise TypeError("El contenido debe ser una cadena")
        self._validar_posicion(posicion)
        self._aplicar(self._texto[:posicion] + contenido + self._texto[posicion:])

    def borrar(self, inicio: int, fin: int) -> None:
        """Borra el intervalo semiabierto [inicio, fin)."""
        self._validar_posicion(inicio)
        self._validar_posicion(fin)
        if fin < inicio:
            raise ValueError("El fin no puede preceder al inicio")
        self._aplicar(self._texto[:inicio] + self._texto[fin:])

    def reemplazar(self, inicio: int, fin: int, contenido: str) -> None:
        """Sustituye un intervalo por el contenido indicado."""
        if not isinstance(contenido, str):
            raise TypeError("El contenido debe ser una cadena")
        self._validar_posicion(inicio)
        self._validar_posicion(fin)
        if fin < inicio:
            raise ValueError("El fin no puede preceder al inicio")
        self._aplicar(self._texto[:inicio] + contenido + self._texto[fin:])

    def _validar_posicion(self, posicion: int) -> None:
        if (not isinstance(posicion, int) or isinstance(posicion, bool)
                or not 0 <= posicion <= len(self._texto)):
            raise ValueError("Posición fuera de los límites del texto")

    def deshacer(self) -> bool:
        """Recupera el estado anterior; devuelve False si no hay cambios."""
        if not self._deshacer:
            return False
        self._rehacer.append(self._texto)
        self._texto = self._deshacer.pop()
        return True

    def rehacer(self) -> bool:
        """Recupera el cambio deshecho más reciente."""
        if not self._rehacer:
            return False
        self._deshacer.append(self._texto)
        self._texto = self._rehacer.pop()
        return True


if __name__ == "__main__":
    editor = EditorTexto("Hola")
    editor.insertar(4, " mundo")
    assert editor.texto == "Hola mundo"
    editor.reemplazar(0, 4, "Adiós")
    assert editor.texto == "Adiós mundo"
    editor.borrar(5, 11)
    assert editor.texto == "Adiós"
    assert editor.deshacer() and editor.texto == "Adiós mundo"
    assert editor.deshacer() and editor.texto == "Hola mundo"
    assert editor.rehacer() and editor.texto == "Adiós mundo"
    editor.insertar(len(editor.texto), "!")
    assert not editor.rehacer()
    assert editor.texto == "Adiós mundo!"
    assert editor.deshacer() and editor.texto == "Adiós mundo"
    assert editor.deshacer() and editor.texto == "Hola mundo"
    assert editor.deshacer() and editor.texto == "Hola"
    assert not editor.deshacer()
    editor.insertar(0, "")
    assert not editor.deshacer()
    try:
        editor.borrar(0, 100)
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba ValueError")
    print("Ejercicio 241: pruebas superadas")
