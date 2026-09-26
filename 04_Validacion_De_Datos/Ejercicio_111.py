"""
Enunciado:

111. Edad válida: Desarrolla una función que solicite la edad del usuario
y la valide para asegurarse de que sea un número positivo.

Solución:
"""


def validar_edad(edad: str) -> int:
    """Convierte y valida una edad introducida como texto."""
    try:
        edad_numero = int(edad)
    except (TypeError, ValueError):
        raise ValueError("La edad debe ser un número entero.") from None

    if edad_numero <= 0:
        raise ValueError("La edad debe ser un número positivo.")

    return edad_numero


if __name__ == "__main__":
    ejemplos = ["25", "0", "veinte"]

    for ejemplo in ejemplos:
        try:
            print(f"Edad válida: {validar_edad(ejemplo)}")
        except ValueError as error:
            print(f"Entrada {ejemplo!r}: {error}")
