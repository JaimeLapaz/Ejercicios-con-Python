"""
Enunciado:

109. Promedio de una lista: Implementa una función que reciba una lista de
números y calcule su promedio, asegurándose de que todos sean numéricos.

Solución:
"""


def calcular_promedio(numeros: list) -> float:
    """Valida una lista de números y calcula su promedio."""
    if not isinstance(numeros, list):
        raise TypeError("La entrada debe ser una lista.")

    if not numeros:
        raise ValueError("La lista no puede estar vacía.")

    total = 0

    for numero in numeros:
        if isinstance(numero, bool) or not isinstance(numero, (int, float)):
            raise TypeError("Todos los elementos deben ser números.")

        total += numero

    return total / len(numeros)


if __name__ == "__main__":
    print(f"Promedio: {calcular_promedio([8, 7.5, 9, 10]):.2f}")

    try:
        calcular_promedio([5, "seis", 7])
    except TypeError as error:
        print(f"Error: {error}")
