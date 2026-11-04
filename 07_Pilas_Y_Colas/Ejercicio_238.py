"""
Enunciado:

238. Pila de Historiales: Implementa una pila de historiales de navegación web,
     permitiendo navegar hacia atrás y hacia adelante.

Solución:
"""

from __future__ import annotations


class HistorialNavegacion:
    """Historial con dos pilas y una página actual.

    Visitar una página nueva descarta el historial de avance. Retroceder o
    avanzar cuando no hay páginas disponibles deja el estado sin cambios.
    Cada operación cuesta O(1).
    """

    def __init__(self, pagina_inicial: str | None = None) -> None:
        self._atras: list[str] = []
        self._adelante: list[str] = []
        self._actual: str | None = None
        if pagina_inicial is not None:
            self.visitar(pagina_inicial)

    @staticmethod
    def _validar_pagina(pagina: str) -> None:
        if not isinstance(pagina, str) or not pagina.strip():
            raise ValueError("La página debe ser un texto no vacío")

    @property
    def actual(self) -> str | None:
        """Devuelve la página abierta o None si no se ha visitado ninguna."""
        return self._actual

    @property
    def puede_retroceder(self) -> bool:
        return bool(self._atras)

    @property
    def puede_avanzar(self) -> bool:
        return bool(self._adelante)

    def visitar(self, pagina: str) -> None:
        """Abre una página y elimina la rama de avance anterior."""
        self._validar_pagina(pagina)
        if self._actual is not None:
            self._atras.append(self._actual)
        self._actual = pagina
        self._adelante.clear()

    def retroceder(self) -> str | None:
        """Vuelve a la página anterior, si existe."""
        if self._atras:
            assert self._actual is not None
            self._adelante.append(self._actual)
            self._actual = self._atras.pop()
        return self._actual

    def avanzar(self) -> str | None:
        """Recupera la página siguiente, si existe."""
        if self._adelante:
            assert self._actual is not None
            self._atras.append(self._actual)
            self._actual = self._adelante.pop()
        return self._actual

    def estado(self) -> tuple[tuple[str, ...], str | None, tuple[str, ...]]:
        """Expone copias inmutables de las pilas para inspección."""
        return tuple(self._atras), self._actual, tuple(self._adelante)


if __name__ == "__main__":
    historial = HistorialNavegacion()
    assert historial.retroceder() is None
    assert historial.avanzar() is None
    historial.visitar("inicio")
    historial.visitar("noticias")
    historial.visitar("articulo")
    assert historial.retroceder() == "noticias"
    assert historial.retroceder() == "inicio"
    assert historial.retroceder() == "inicio"
    assert historial.avanzar() == "noticias"
    assert historial.puede_avanzar
    historial.visitar("busqueda")
    assert historial.actual == "busqueda"
    assert not historial.puede_avanzar
    assert historial.avanzar() == "busqueda"
    assert historial.estado() == (("inicio", "noticias"), "busqueda", ())
    for pagina in ("", "  ", None, 42):
        try:
            historial.visitar(pagina)
        except ValueError:
            pass
        else:
            raise AssertionError("Se esperaba ValueError")
    print("Ejercicio 238: pruebas superadas")
