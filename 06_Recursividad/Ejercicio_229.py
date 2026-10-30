"""
Enunciado:

229. Generación de Subconjuntos: Diseña una función recursiva que genere
    todos los subconjuntos de un conjunto dado.

Solución:
"""

from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


def generar_subconjuntos(elementos: set[T]) -> list[set[T]]:
    """Genera el conjunto potencia mediante inclusión/exclusión recursiva.

    Devuelve 2**n subconjuntos sin duplicados y no modifica la entrada.
    El orden de salida depende de la iteración del conjunto de entrada.
    Complejidad: O(n * 2**n) en tiempo y memoria para la salida.
    """
    valores = list(elementos)
    subconjuntos: list[set[T]] = []
    actual: set[T] = set()

    def explorar(indice: int) -> None:
        if indice == len(valores):
            subconjuntos.append(actual.copy())
            return

        explorar(indice + 1)  # Excluir el elemento actual.
        actual.add(valores[indice])
        explorar(indice + 1)  # Incluir el elemento actual.
        actual.remove(valores[indice])  # Restaurar para otras ramas.

    explorar(0)
    return subconjuntos


if __name__ == "__main__":
    assert generar_subconjuntos(set()) == [set()]
    assert {frozenset(s) for s in generar_subconjuntos({1, 2})} == {
        frozenset(), frozenset({1}), frozenset({2}), frozenset({1, 2})
    }

    entrada = {1, 2, 3}
    resultado = generar_subconjuntos(entrada)
    assert entrada == {1, 2, 3}
    assert len(resultado) == 8
    assert len({frozenset(s) for s in resultado}) == 8
    assert all(s <= entrada for s in resultado)
    assert any(s == entrada for s in resultado)
    assert any(not s for s in resultado)
    assert len(generar_subconjuntos(set(range(10)))) == 1024
    print("Ejercicio 229: pruebas superadas")
