"""
Enunciado:

98. Implementa una función que tome una lista de números
y devuelva una tupla con el valor mínimo y máximo.

Solución:
"""


def obtener_minimo_maximo(numeros: list) -> tuple | None:
    """
    Obtiene el valor mínimo y máximo de una lista.

    Args:
        numeros (list): Lista de números.

    Returns:
        tuple | None: Tupla (mínimo, máximo) o None
        si la lista está vacía.
    """
    if not numeros:
        return None

    minimo = numeros[0]
    maximo = numeros[0]

    for numero in numeros[1:]:
        if numero < minimo:
            minimo = numero

        if numero > maximo:
            maximo = numero

    return minimo, maximo


if __name__ == "__main__":
    numeros = [15, -4, 27, 8, 3, 42, 11]

    resultado = obtener_minimo_maximo(numeros)

    if resultado is not None:
        minimo, maximo = resultado

        print(f"Valor mínimo: {minimo}")
        print(f"Valor máximo: {maximo}")
    else:
        print("La lista está vacía.")
