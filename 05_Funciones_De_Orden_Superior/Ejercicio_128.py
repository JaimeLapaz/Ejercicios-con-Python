"""
Enunciado:

128. Mapeo de Números: Escribe una función de orden superior que tome una
lista de números y una función como argumentos y aplique la función a cada
elemento de la lista.

Solución:
"""

from collections.abc import Callable

Numero = int | float


def mapear_numeros(
    numeros: list[Numero], transformacion: Callable[[Numero], Numero]
) -> list[Numero]:
    """Aplica la función recibida a cada número sin modificar la lista original."""
    return [transformacion(numero) for numero in numeros]


if __name__ == "__main__":
    valores = [1, 2, 3, 4]
    dobles = mapear_numeros(valores, lambda numero: numero * 2)
    cuadrados = mapear_numeros(valores, lambda numero: numero ** 2)

    print("Original:", valores)
    print("Dobles:", dobles)
    print("Cuadrados:", cuadrados)
    assert dobles == [2, 4, 6, 8]
    assert cuadrados == [1, 4, 9, 16]
