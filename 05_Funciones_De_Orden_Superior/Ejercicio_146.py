"""
Enunciado:

146. Transformación de Imágenes: Diseña una función de orden superior
que tome una imagen (representada como una matriz de píxeles) y una
función de transformación, y aplique la transformación a la imagen.

Solución:
"""

from collections.abc import Callable
from typing import TypeVar

Pixel = TypeVar("Pixel")
PixelTransformado = TypeVar("PixelTransformado")


def transformar_imagen(
    imagen: list[list[Pixel]],
    transformacion: Callable[[Pixel], PixelTransformado],
) -> list[list[PixelTransformado]]:
    """Aplica la transformación a cada píxel y crea una nueva imagen."""
    return [
        [transformacion(pixel) for pixel in fila]
        for fila in imagen
    ]


if __name__ == "__main__":
    imagen = [
        [(255, 0, 0), (0, 255, 0)],
        [(0, 0, 255), (255, 255, 255)],
    ]

    def a_grises(pixel: tuple[int, int, int]) -> int:
        """Calcula un nivel de gris sencillo mediante el promedio RGB."""
        return sum(pixel) // 3

    grises = transformar_imagen(imagen, a_grises)
    invertida = transformar_imagen(
        imagen, lambda pixel: tuple(255 - canal for canal in pixel)
    )

    print("Escala de grises:", grises)
    print("Colores invertidos:", invertida)
    assert grises == [[85, 85], [85, 255]]
    assert invertida == [
        [(0, 255, 255), (255, 0, 255)],
        [(255, 255, 0), (0, 0, 0)],
    ]
