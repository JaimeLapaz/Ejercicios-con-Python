"""
Enunciado:

134. Filtrado de Palabras Largas: Diseña una función de orden superior
que tome una lista de palabras y una función de filtro basada en la
longitud como argumentos, y devuelva las palabras que pasen el filtro.

Solución:
"""

from collections.abc import Callable


def filtrar_por_longitud(
    palabras: list[str], criterio: Callable[[int], bool]
) -> list[str]:
    """Selecciona las palabras cuya longitud satisface el criterio."""
    return [palabra for palabra in palabras if criterio(len(palabra))]


if __name__ == "__main__":
    palabras = ["sol", "luna", "estrella", "mar", "universo"]
    largas = filtrar_por_longitud(palabras, lambda longitud: longitud >= 5)
    cortas = filtrar_por_longitud(palabras, lambda longitud: longitud <= 3)

    print("Palabras de al menos cinco letras:", largas)
    print("Palabras de hasta tres letras:", cortas)
    assert largas == ["estrella", "universo"]
    assert cortas == ["sol", "mar"]
