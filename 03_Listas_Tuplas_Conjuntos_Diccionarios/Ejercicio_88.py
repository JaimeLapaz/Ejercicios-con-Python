"""
Enunciado:

88. Escribe una función que elimine elementos duplicados
de una lista sin cambiar su orden.

Solución:
"""


def eliminar_duplicados(lista: list) -> list:
    """
    Elimina elementos duplicados manteniendo el orden original.

    Args:
        lista (list): Lista que puede contener duplicados.

    Returns:
        list: Nueva lista sin elementos repetidos.
    """
    resultado = []
    vistos = set()

    for elemento in lista:
        if elemento not in vistos:
            resultado.append(elemento)
            vistos.add(elemento)

    return resultado


if __name__ == "__main__":
    numeros = [1, 2, 2, 3, 1, 4, 5, 3, 6, 4]

    resultado = eliminar_duplicados(numeros)

    print("Lista original:")
    print(numeros)

    print("\nLista sin duplicados:")
    print(resultado)
