"""
Enunciado:

82. Desarrolla un programa que encuentre la tupla más común
en una lista de tuplas.

Solución:
"""


def tupla_mas_comun(tuplas: list):
    """
    Encuentra la tupla que aparece más veces.

    Args:
        tuplas (list): Lista de tuplas.

    Returns:
        tuple | None: Tupla más frecuente o None si la lista
        está vacía.
    """
    if not tuplas:
        return None

    frecuencias = {}

    for tupla in tuplas:
        if tupla in frecuencias:
            frecuencias[tupla] += 1
        else:
            frecuencias[tupla] = 1

    mas_comun = None
    mayor_frecuencia = 0

    for tupla, frecuencia in frecuencias.items():
        if frecuencia > mayor_frecuencia:
            mayor_frecuencia = frecuencia
            mas_comun = tupla

    return mas_comun


def contar_apariciones(tuplas: list, tupla_buscada: tuple) -> int:
    """
    Cuenta cuántas veces aparece una tupla.

    Args:
        tuplas (list): Lista de tuplas.
        tupla_buscada (tuple): Tupla a buscar.

    Returns:
        int: Número de apariciones.
    """
    contador = 0

    for tupla in tuplas:
        if tupla == tupla_buscada:
            contador += 1

    return contador


if __name__ == "__main__":
    coordenadas = [(1, 2), (3, 4), (1, 2), (5, 6), (1, 2), (3, 4), (7, 8)]

    resultado = tupla_mas_comun(coordenadas)

    if resultado is not None:
        apariciones = contar_apariciones(coordenadas, resultado)

        print(f"La tupla más común es {resultado}.")

        print(f"Aparece {apariciones} veces.")
    else:
        print("La lista está vacía.")
