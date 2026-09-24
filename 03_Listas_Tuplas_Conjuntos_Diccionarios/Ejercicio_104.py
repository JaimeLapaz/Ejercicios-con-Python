"""
Enunciado:

104. Implementa una función que elimine duplicados de una lista
manteniendo el orden original y almacene los elementos únicos
en un conjunto.

Solución:
"""


def eliminar_duplicados(lista: list) -> tuple:
    """
    Elimina duplicados conservando el orden de primera aparición.

    Args:
        lista (list): Lista original.

    Returns:
        tuple: Lista sin duplicados y conjunto de elementos únicos.
    """
    elementos_unicos = set()
    lista_sin_duplicados = []

    for elemento in lista:
        if elemento not in elementos_unicos:
            elementos_unicos.add(elemento)
            lista_sin_duplicados.append(elemento)

    return lista_sin_duplicados, elementos_unicos


if __name__ == "__main__":
    numeros = [4, 2, 4, 7, 2, 9, 7, 1]

    sin_duplicados, unicos = eliminar_duplicados(numeros)

    print(f"Lista original: {numeros}")
    print(f"Lista sin duplicados: {sin_duplicados}")
    print(f"Conjunto de elementos únicos: {unicos}")

    print("\nSegunda prueba:")
    palabras = ["python", "java", "python", "c", "java"]
    print(eliminar_duplicados(palabras))
