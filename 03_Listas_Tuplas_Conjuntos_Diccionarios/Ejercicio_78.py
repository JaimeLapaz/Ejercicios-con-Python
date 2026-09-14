"""
Enunciado:

78. Escribe una función que tome una lista de tuplas y las ordene
en función del segundo elemento de cada tupla.

Solución:
"""


def ordenar_por_segundo_elemento(tuplas: list) -> list:
    """
    Ordena una lista de tuplas utilizando el segundo elemento.

    Args:
        tuplas (list): Lista de tuplas.

    Returns:
        list: Nueva lista ordenada.
    """
    return sorted(tuplas, key=lambda tupla: tupla[1])


if __name__ == "__main__":
    estudiantes = [("Ana", 8), ("Carlos", 5), ("Laura", 10), ("Miguel", 7)]

    ordenados = ordenar_por_segundo_elemento(estudiantes)

    print("Lista original:")
    print(estudiantes)

    print("\nOrdenada por el segundo elemento:")
    print(ordenados)
