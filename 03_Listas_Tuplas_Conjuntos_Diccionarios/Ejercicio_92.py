"""
Enunciado:

92. Desarrolla una función que encuentre la subsecuencia
más larga creciente en una lista de números.

Solución:
"""


def subsecuencia_creciente_mas_larga(numeros: list) -> list:
    """
    Encuentra la subsecuencia estrictamente creciente más larga.

    Args:
        numeros (list): Lista de números.

    Returns:
        list: Subsecuencia creciente más larga.
    """
    if not numeros:
        return []

    longitud = [1] * len(numeros)
    anterior = [-1] * len(numeros)

    for actual in range(len(numeros)):
        for previo in range(actual):
            if numeros[previo] < numeros[actual]:
                nueva_longitud = longitud[previo] + 1

                if nueva_longitud > longitud[actual]:
                    longitud[actual] = nueva_longitud
                    anterior[actual] = previo

    posicion_final = 0

    for posicion in range(1, len(longitud)):
        if longitud[posicion] > longitud[posicion_final]:
            posicion_final = posicion

    resultado = []
    posicion = posicion_final

    while posicion != -1:
        resultado.append(numeros[posicion])

        posicion = anterior[posicion]

    resultado.reverse()

    return resultado


if __name__ == "__main__":
    numeros = [10, 22, 9, 33, 21, 50, 41, 60]

    resultado = subsecuencia_creciente_mas_larga(numeros)

    print("Lista original:")
    print(numeros)

    print("\nSubsecuencia creciente más larga:")
    print(resultado)

    print("Longitud:", len(resultado))
