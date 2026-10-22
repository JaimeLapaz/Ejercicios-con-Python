"""
Enunciado:

219. Árbol Trie: Implementa una clase ArbolTrie que represente un árbol
    trie para almacenar palabras y permita buscar prefijos y palabras completas.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class NodoTrie:
    """Nodo con transiciones por carácter y marca de fin de palabra."""

    hijos: dict[str, NodoTrie] = field(default_factory=dict)
    es_palabra: bool = False


class ArbolTrie:
    """Trie que distingue mayúsculas y permite la cadena vacía."""

    def __init__(self) -> None:
        self.raiz = NodoTrie()
        self._cantidad = 0

    def insertar(self, palabra: str) -> bool:
        """Añade una palabra; devuelve False si ya estaba almacenada."""
        nodo = self.raiz
        for caracter in palabra:
            nodo = nodo.hijos.setdefault(caracter, NodoTrie())
        if nodo.es_palabra:
            return False
        nodo.es_palabra = True
        self._cantidad += 1
        return True

    def _encontrar(self, texto: str) -> NodoTrie | None:
        nodo = self.raiz
        for caracter in texto:
            siguiente = nodo.hijos.get(caracter)
            if siguiente is None:
                return None
            nodo = siguiente
        return nodo

    def buscar(self, palabra: str) -> bool:
        """Comprueba si existe la palabra completa."""
        nodo = self._encontrar(palabra)
        return nodo is not None and nodo.es_palabra

    def empieza_por(self, prefijo: str) -> bool:
        """Comprueba si existe una ruta para el prefijo indicado."""
        return self._encontrar(prefijo) is not None

    def palabras_con_prefijo(self, prefijo: str) -> list[str]:
        """Devuelve todas las palabras coincidentes en orden lexicográfico."""
        inicio = self._encontrar(prefijo)
        if inicio is None:
            return []
        resultado: list[str] = []
        pendientes = [(inicio, prefijo)]
        while pendientes:
            nodo, texto = pendientes.pop()
            if nodo.es_palabra:
                resultado.append(texto)
            for caracter in sorted(nodo.hijos, reverse=True):
                pendientes.append((nodo.hijos[caracter], texto + caracter))
        return resultado

    def __len__(self) -> int:
        return self._cantidad


if __name__ == "__main__":
    trie = ArbolTrie()
    assert trie.empieza_por("")
    assert not trie.buscar("casa")
    for palabra in ("casa", "casco", "cas", "cama", "sol"):
        assert trie.insertar(palabra)
    assert not trie.insertar("casa")
    assert len(trie) == 5
    assert trie.buscar("cas") and trie.buscar("casa")
    assert not trie.buscar("ca") and not trie.buscar("CASA")
    assert trie.empieza_por("ca") and not trie.empieza_por("per")
    assert trie.palabras_con_prefijo("cas") == ["cas", "casa", "casco"]
    assert trie.palabras_con_prefijo("xyz") == []
    assert trie.insertar("") and trie.buscar("")
    assert len(trie) == 6
    print("Ejercicio 219: pruebas superadas")
