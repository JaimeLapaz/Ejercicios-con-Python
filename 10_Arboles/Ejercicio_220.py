"""
Enunciado:

220. Árbol de Huffman: Desarrolla una función para construir un árbol de
    Huffman a partir de frecuencias de caracteres y codificar texto.

Solución:
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from heapq import heappop, heappush


@dataclass
class NodoHuffman:
    """Nodo del árbol; los nodos internos no contienen caracteres."""

    frecuencia: int
    caracter: str | None = None
    izquierdo: NodoHuffman | None = None
    derecho: NodoHuffman | None = None


def construir_arbol_huffman(frecuencias: dict[str, int]) -> NodoHuffman | None:
    """Construye un árbol óptimo usando una cola de prioridad O(k log k).

    Los empates se resuelven de manera determinista por orden de carácter
    y de creación de nodos. Un diccionario vacío produce un árbol vacío.
    """
    cola: list[tuple[int, int, NodoHuffman]] = []
    for orden, (caracter, frecuencia) in enumerate(sorted(frecuencias.items())):
        if len(caracter) != 1:
            raise ValueError("Las claves deben ser caracteres individuales")
        if type(frecuencia) is not int or frecuencia <= 0:
            raise ValueError("Las frecuencias deben ser enteros positivos")
        heappush(cola, (frecuencia, orden, NodoHuffman(frecuencia, caracter)))

    siguiente_orden = len(cola)
    while len(cola) > 1:
        frecuencia_izq, _, izquierdo = heappop(cola)
        frecuencia_der, _, derecho = heappop(cola)
        padre = NodoHuffman(
            frecuencia_izq + frecuencia_der,
            izquierdo=izquierdo,
            derecho=derecho,
        )
        heappush(cola, (padre.frecuencia, siguiente_orden, padre))
        siguiente_orden += 1
    return cola[0][2] if cola else None


def generar_codigos(raiz: NodoHuffman | None) -> dict[str, str]:
    """Obtiene códigos binarios libres de prefijos para las hojas."""
    if raiz is None:
        return {}
    codigos: dict[str, str] = {}
    pendientes = [(raiz, "")]
    while pendientes:
        nodo, prefijo = pendientes.pop()
        if nodo.caracter is not None:
            codigos[nodo.caracter] = prefijo or "0"
            continue
        if nodo.derecho is not None:
            pendientes.append((nodo.derecho, prefijo + "1"))
        if nodo.izquierdo is not None:
            pendientes.append((nodo.izquierdo, prefijo + "0"))
    return codigos


def codificar_texto(texto: str, codigos: dict[str, str]) -> str:
    """Codifica texto con el diccionario obtenido del árbol de Huffman."""
    try:
        return "".join(codigos[caracter] for caracter in texto)
    except KeyError as error:
        raise ValueError(f"Carácter sin código: {error.args[0]!r}") from error


def decodificar_texto(bits: str, raiz: NodoHuffman | None) -> str:
    """Recupera el texto y rechaza bits inválidos o códigos incompletos."""
    if raiz is None:
        if bits:
            raise ValueError("No hay árbol para decodificar los bits")
        return ""
    if raiz.caracter is not None:
        if any(bit != "0" for bit in bits):
            raise ValueError("Código inválido para un árbol de un solo carácter")
        return raiz.caracter * len(bits)

    resultado: list[str] = []
    actual = raiz
    for bit in bits:
        if bit == "0":
            siguiente = actual.izquierdo
        elif bit == "1":
            siguiente = actual.derecho
        else:
            raise ValueError("Los códigos solo pueden contener 0 y 1")
        if siguiente is None:
            raise ValueError("Secuencia de bits inválida")
        actual = siguiente
        if actual.caracter is not None:
            resultado.append(actual.caracter)
            actual = raiz
    if actual is not raiz:
        raise ValueError("Secuencia de bits incompleta")
    return "".join(resultado)


if __name__ == "__main__":
    texto = "abracadabra"
    arbol = construir_arbol_huffman(dict(Counter(texto)))
    codigos = generar_codigos(arbol)
    comprimido = codificar_texto(texto, codigos)
    assert decodificar_texto(comprimido, arbol) == texto
    assert len(comprimido) < 8 * len(texto)
    assert len(set(codigos.values())) == len(codigos)
    assert all(not segundo.startswith(primero)
               for caracter, primero in codigos.items()
               for otro, segundo in codigos.items() if caracter != otro)

    unico = construir_arbol_huffman({"x": 5})
    assert generar_codigos(unico) == {"x": "0"}
    assert decodificar_texto("000", unico) == "xxx"
    assert construir_arbol_huffman({}) is None
    assert decodificar_texto("", None) == ""
    assert codificar_texto("", {}) == ""
    for incorrectas in ({"a": 0}, {"ab": 2}, {"a": -3}):
        try:
            construir_arbol_huffman(incorrectas)
        except ValueError:
            pass
        else:
            raise AssertionError("Se esperaba ValueError")
    print("Ejercicio 220: pruebas superadas")
