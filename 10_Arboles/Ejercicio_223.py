"""
Enunciado:

223. Árbol Sufijo: Diseña una clase ArbolSufijo que construya un árbol
    de sufijo a partir de una cadena de texto y permita buscar subcadenas.

Solución:
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class NodoSufijo:
    """Nodo de un árbol de sufijos con aristas etiquetadas por intervalos."""

    hijos: dict[str, Arista] = field(default_factory=dict)
    indice_sufijo: int | None = None


@dataclass
class Arista:
    """Etiqueta [inicio, fin) sobre el texto original más un terminador."""

    inicio: int
    fin: int
    destino: NodoSufijo


class ArbolSufijo:
    """Árbol de sufijos comprimido, construido por inserción de sufijos.

    La construcción emplea O(n²) tiempo en el peor caso y O(n) nodos.
    Buscar una subcadena de longitud m cuesta O(m); obtener todas sus
    posiciones añade el recorrido de las hojas coincidentes.
    """

    def __init__(self, texto: str) -> None:
        self.texto = texto
        # El terminador distingue incluso los sufijos que son prefijos de otros.
        # Nunca puede aparecer en el texto recibido.
        codigo = 0
        while chr(codigo) in texto:
            codigo += 1
        self._terminador = chr(codigo)
        self._cadena = texto + self._terminador
        self.raiz = NodoSufijo()
        for inicio in range(len(self._cadena)):
            self._insertar_sufijo(inicio)

    def _insertar_sufijo(self, inicio: int) -> None:
        cadena = self._cadena
        posicion = inicio
        nodo = self.raiz
        while True:
            arista = nodo.hijos.get(cadena[posicion])
            if arista is None:
                nodo.hijos[cadena[posicion]] = Arista(
                    posicion, len(cadena), NodoSufijo(indice_sufijo=inicio)
                )
                return

            comun = 0
            while (arista.inicio + comun < arista.fin
                   and cadena[arista.inicio + comun] == cadena[posicion + comun]):
                comun += 1

            if arista.inicio + comun == arista.fin:
                posicion += comun
                nodo = arista.destino
                continue

            # Dividir la arista existente en el primer carácter diferente.
            intermedio = NodoSufijo()
            nodo.hijos[cadena[arista.inicio]] = Arista(
                arista.inicio, arista.inicio + comun, intermedio
            )
            arista.inicio += comun
            intermedio.hijos[cadena[arista.inicio]] = arista
            posicion += comun
            intermedio.hijos[cadena[posicion]] = Arista(
                posicion, len(cadena), NodoSufijo(indice_sufijo=inicio)
            )
            return

    def _nodo_coincidente(self, subcadena: str) -> NodoSufijo | None:
        """Localiza el subárbol de una coincidencia, incluso a mitad de arista."""
        if self._terminador in subcadena:
            return None
        if not subcadena:
            return self.raiz
        posicion = 0
        nodo = self.raiz
        while posicion < len(subcadena):
            arista = nodo.hijos.get(subcadena[posicion])
            if arista is None:
                return None
            for indice in range(arista.inicio, arista.fin):
                if posicion == len(subcadena):
                    return arista.destino
                if self._cadena[indice] != subcadena[posicion]:
                    return None
                posicion += 1
            nodo = arista.destino
        return nodo

    def buscar(self, subcadena: str) -> bool:
        """Indica si el texto contiene la subcadena (incluida la vacía)."""
        return self._nodo_coincidente(subcadena) is not None

    def posiciones(self, subcadena: str) -> list[int]:
        """Devuelve los índices iniciales de todas las coincidencias, ordenados."""
        if not subcadena:
            return list(range(len(self.texto) + 1))
        nodo = self._nodo_coincidente(subcadena)
        if nodo is None:
            return []
        resultado: list[int] = []
        pendientes = [nodo]
        while pendientes:
            actual = pendientes.pop()
            if actual.indice_sufijo is not None:
                if actual.indice_sufijo + len(subcadena) <= len(self.texto):
                    resultado.append(actual.indice_sufijo)
            else:
                pendientes.extend(arista.destino for arista in actual.hijos.values())
        return sorted(resultado)

    def __contains__(self, subcadena: str) -> bool:
        return self.buscar(subcadena)


if __name__ == "__main__":
    arbol = ArbolSufijo("banana")
    assert arbol.buscar("ana")
    assert arbol.posiciones("ana") == [1, 3]
    assert arbol.posiciones("na") == [2, 4]
    assert arbol.posiciones("banana") == [0]
    assert arbol.posiciones("bananas") == []
    assert arbol.posiciones("") == list(range(7))
    assert "nan" in arbol and "nab" not in arbol
    assert ArbolSufijo("").posiciones("") == [0]
    assert not ArbolSufijo("").buscar("a")
    especial = ArbolSufijo("\x00a\x00")
    assert especial.posiciones("\x00") == [0, 2]
    assert especial.posiciones("a\x00") == [1]
    assert ArbolSufijo("á🙂á").posiciones("á") == [0, 2]
    print("Ejercicio 223: pruebas superadas")
