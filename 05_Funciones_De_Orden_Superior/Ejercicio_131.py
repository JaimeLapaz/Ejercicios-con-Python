"""
Enunciado:

131. Transformación de Texto: Crea una función de orden superior que tome
una cadena de texto y una función de transformación como argumentos,
y aplique la función de transformación a cada palabra en la cadena.

Solución:
"""

from collections.abc import Callable
import re


def transformar_palabras(texto: str, transformar: Callable[[str], str]) -> str:
    """Transforma cada palabra conservando los espacios y saltos de línea."""
    return re.sub(r"\S+", lambda coincidencia: transformar(coincidencia.group()), texto)


if __name__ == "__main__":
    original = "hola   mundo\npython"
    mayusculas = transformar_palabras(original, str.upper)
    longitudes = transformar_palabras(original, lambda palabra: str(len(palabra)))

    print("Original:", repr(original))
    print("Mayúsculas:", repr(mayusculas))
    print("Longitudes:", repr(longitudes))
    assert mayusculas == "HOLA   MUNDO\nPYTHON"
    assert longitudes == "4   5\n6"
