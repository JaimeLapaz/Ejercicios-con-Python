"""
Enunciado:

113. Búsqueda en lista: Implementa una función que busque un elemento
en una lista y valide que el elemento exista en la lista antes de buscarlo.

Solución:
"""


def buscar_elemento(lista: list, elemento):
    """
    Busca un elemento después de comprobar que existe.

    Returns:
        int | None: Índice de la primera aparición o None si no existe.
    """
    if not isinstance(lista, list):
        raise TypeError("La entrada debe ser una lista.")

    if elemento not in lista:
        return None

    return lista.index(elemento)


if __name__ == "__main__":
    datos = ["Python", "Java", "C++", "JavaScript"]

    for lenguaje in ("Java", "Rust"):
        posicion = buscar_elemento(datos, lenguaje)

        if posicion is None:
            print(f"{lenguaje} no existe en la lista.")
        else:
            print(f"{lenguaje} está en la posición {posicion}.")
