"""
Enunciado:

90. Diseña una función que divida una lista
en sub-listas de tamaño fijo.

Solución:
"""


def dividir_lista(lista: list, tamanio: int) -> list:
    """
    Divide una lista en sublistas de tamaño fijo.

    Args:
        lista (list): Lista original.
        tamanio (int): Tamaño máximo de cada sublista.

    Returns:
        list: Lista que contiene las sublistas.

    Raises:
        ValueError: Si el tamaño no es mayor que cero.
    """
    if tamanio <= 0:
        raise ValueError("El tamaño debe ser mayor que cero.")

    resultado = []

    for posicion in range(0, len(lista), tamanio):
        sublista = lista[posicion : posicion + tamanio]

        resultado.append(sublista)

    return resultado


if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    resultado = dividir_lista(numeros, 3)

    print("Lista original:")
    print(numeros)

    print("\nSublistas:")

    for sublista in resultado:
        print(sublista)
