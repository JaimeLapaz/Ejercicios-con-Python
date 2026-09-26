"""
Enunciado:

108. Suma de dos números: Escribe una función que tome dos números como entrada
y devuelva su suma después de validar que ambos sean números.

Solución:
"""


def sumar_numeros(numero_1, numero_2):
    """Valida dos números y devuelve su suma."""
    if isinstance(numero_1, bool) or not isinstance(numero_1, (int, float)):
        raise TypeError("El primer valor debe ser un número.")

    if isinstance(numero_2, bool) or not isinstance(numero_2, (int, float)):
        raise TypeError("El segundo valor debe ser un número.")

    return numero_1 + numero_2


if __name__ == "__main__":
    print(sumar_numeros(10, 5.5))

    try:
        print(sumar_numeros(8, "2"))
    except TypeError as error:
        print(f"Error: {error}")
