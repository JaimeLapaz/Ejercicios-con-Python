"""
Enunciado:

81. Crea una función que divida una lista de números en dos
listas de tuplas, una con números pares y otra con números impares.

Solución:
"""


def separar_pares_impares(numeros: list) -> tuple:
    """
    Divide los números en pares e impares.

    Cada número se almacena dentro de una tupla.

    Args:
        numeros (list): Lista de números enteros.

    Returns:
        tuple: Dos listas, una de pares y otra de impares.
    """
    pares = []
    impares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append((numero,))
        else:
            impares.append((numero,))

    return pares, impares


if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    pares, impares = separar_pares_impares(numeros)

    print("Pares:")
    print(pares)

    print("\nImpares:")
    print(impares)
