"""
Enunciado:

83. Escribe una función que calcule la intersección de dos
conjuntos sin utilizar el operador &.

Solución:
"""


def calcular_interseccion(conjunto1: set, conjunto2: set) -> set:
    """
    Calcula los elementos comunes entre dos conjuntos.

    Args:
        conjunto1 (set): Primer conjunto.
        conjunto2 (set): Segundo conjunto.

    Returns:
        set: Conjunto con los elementos comunes.
    """
    resultado = set()

    for elemento in conjunto1:
        if elemento in conjunto2:
            resultado.add(elemento)

    return resultado


if __name__ == "__main__":
    conjunto1 = {1, 2, 3, 4, 5}
    conjunto2 = {4, 5, 6, 7, 8}

    resultado = calcular_interseccion(conjunto1, conjunto2)

    print("Intersección:", resultado)
