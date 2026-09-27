"""
Enunciado:

117. Convertir a mayúsculas: Implementa una función que tome una
cadena como entrada y la convierta a mayúsculas, validando que sea
una cadena de texto.

Solución:
"""


def convertir_a_mayusculas(texto: str) -> str:
    """
    Valida una cadena y devuelve su contenido en mayúsculas.

    Raises:
        TypeError: Si el valor recibido no es una cadena.
    """
    if not isinstance(texto, str):
        raise TypeError("El valor debe ser una cadena de texto.")

    return texto.upper()


if __name__ == "__main__":
    ejemplos = ("Hola, Python", "validación de datos", "")

    for texto in ejemplos:
        print(f"{texto!r} -> {convertir_a_mayusculas(texto)!r}")
