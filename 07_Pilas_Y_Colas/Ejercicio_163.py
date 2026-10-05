"""
Enunciado:

163. Pila con Límite: Implementa una pila con límite de tamaño
utilizando una lista y controla el desbordamiento.

Solución:
"""


def apilar(pila: list[int], elemento: int, limite: int) -> None:
    """Añade un elemento si la pila todavía tiene capacidad."""
    if limite <= 0:
        raise ValueError("El límite debe ser mayor que cero.")
    if len(pila) >= limite:
        raise OverflowError("La pila ha alcanzado su límite.")
    pila.append(elemento)


def desapilar(pila: list[int]) -> int:
    """Retira y devuelve el elemento situado en la cima."""
    if not pila:
        raise IndexError("La pila está vacía.")
    return pila.pop()


if __name__ == "__main__":
    pila: list[int] = []
    apilar(pila, 10, 3)
    apilar(pila, 20, 3)
    apilar(pila, 30, 3)
    print("Pila:", pila)
    assert pila == [10, 20, 30]
    assert desapilar(pila) == 30

    try:
        apilar(pila, 30, 2)
    except OverflowError as error:
        print("Desbordamiento controlado:", error)
