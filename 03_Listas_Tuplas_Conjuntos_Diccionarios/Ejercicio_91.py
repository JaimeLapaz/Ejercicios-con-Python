"""
Enunciado:

91. Crea un programa que realice una rotación a la izquierda
en una lista (los elementos se desplazan hacia la izquierda).

Solución:
"""


def rotar_izquierda(lista: list, posiciones: int = 1) -> list:
    """
    Rota los elementos de una lista hacia la izquierda.

    Args:
        lista (list): Lista original.
        posiciones (int): Número de posiciones que se rotará.

    Returns:
        list: Nueva lista rotada.
    """
    if not lista:
        return []

    posiciones = posiciones % len(lista)

    return lista[posiciones:] + lista[:posiciones]


if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]

    resultado = rotar_izquierda(numeros)

    print("Lista original:")
    print(numeros)

    print("\nRotación de una posición:")
    print(resultado)

    resultado = rotar_izquierda(numeros, 2)

    print("\nRotación de dos posiciones:")
    print(resultado)
