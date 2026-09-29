"""
Enunciado:

126. Ordenar una lista: Crea una función que ordene una lista de números de manera
ascendente después de validar que los elementos sean números.

Solución:
"""

def ordenar_numeros(numeros: list[float]) -> list[float]:
    """Valida los elementos y devuelve una nueva lista ordenada."""
    if not isinstance(numeros, list):
        raise TypeError("La entrada debe ser una lista.")

    for numero in numeros:
        if not isinstance(numero, (int, float)) or isinstance(numero, bool):
            raise TypeError("Todos los elementos de la lista deben ser números.")

    return sorted(numeros)


if __name__ == "__main__":
    valores = [7, 2.5, -3, 10, 0, 4]
    print("Lista original:", valores)
    print("Lista ordenada:", ordenar_numeros(valores))
