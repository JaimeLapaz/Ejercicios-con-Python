"""
Enunciado:

154. Cambio de Moneda: Diseña una función recursiva que determine
todas las formas posibles de dar cambio a una cantidad dada
utilizando monedas de diferentes denominaciones.

Solución:
"""


def formas_de_cambio(cantidad: int, monedas: list[int]) -> list[list[int]]:
    """Devuelve las combinaciones de monedas que suman la cantidad."""
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")
    if any(moneda <= 0 for moneda in monedas):
        raise ValueError("Las denominaciones deben ser positivas.")

    denominaciones = sorted(set(monedas), reverse=True)

    def buscar(restante: int, indice: int) -> list[list[int]]:
        if restante == 0:
            return [[]]
        if restante < 0 or indice == len(denominaciones):
            return []

        moneda = denominaciones[indice]
        usando_actual = [
            [moneda, *forma]
            for forma in buscar(restante - moneda, indice)
        ]
        sin_actual = buscar(restante, indice + 1)
        return usando_actual + sin_actual

    return buscar(cantidad, 0)


if __name__ == "__main__":
    formas = formas_de_cambio(5, [1, 2, 5])
    print("Formas de dar cambio a 5:", formas)

    assert formas == [[5], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
    assert formas_de_cambio(0, [1, 2]) == [[]]
    assert formas_de_cambio(3, [2]) == []

    try:
        formas_de_cambio(4, [0, 2])
    except ValueError as error:
        print("Denominación no válida:", error)
