"""
Enunciado:

89. Implementa un programa que encuentre el elemento
que más se repite en una lista.

Solución:
"""


def elemento_mas_repetido(lista: list):
    """
    Encuentra el elemento que aparece más veces.

    Args:
        lista (list): Lista de elementos.

    Returns:
        any: Elemento más repetido.
        None: Si la lista está vacía.
    """
    if not lista:
        return None

    frecuencias = {}

    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1

    mas_repetido = None
    mayor_frecuencia = 0

    for elemento, frecuencia in frecuencias.items():
        if frecuencia > mayor_frecuencia:
            mas_repetido = elemento
            mayor_frecuencia = frecuencia

    return mas_repetido


def contar_apariciones(lista: list, elemento) -> int:
    """
    Cuenta cuántas veces aparece un elemento.

    Args:
        lista (list): Lista de elementos.
        elemento: Elemento que queremos contar.

    Returns:
        int: Número de apariciones.
    """
    contador = 0

    for valor in lista:
        if valor == elemento:
            contador += 1

    return contador


if __name__ == "__main__":
    numeros = [4, 2, 7, 4, 9, 4, 2, 7, 7, 7]

    resultado = elemento_mas_repetido(numeros)

    if resultado is not None:
        apariciones = contar_apariciones(numeros, resultado)

        print(f"El elemento más repetido es {resultado}.")

        print(f"Aparece {apariciones} veces.")
    else:
        print("La lista está vacía.")
