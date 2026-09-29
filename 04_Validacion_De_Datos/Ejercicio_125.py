"""
Enunciado:

125. Suma de elementos pares: Implementa una función que tome una lista de números
y calcule la suma de los elementos pares, validando que los elementos sean números.

Solución:
"""

def sumar_pares(numeros: list[int]) -> int:
    """Valida una lista de enteros y devuelve la suma de sus elementos pares."""
    if not isinstance(numeros, list):
        raise TypeError("La entrada debe ser una lista.")

    for numero in numeros:
        if not isinstance(numero, int) or isinstance(numero, bool):
            raise TypeError("Todos los elementos deben ser números enteros.")

    return sum(numero for numero in numeros if numero % 2 == 0)


if __name__ == "__main__":
    valores = [1, 2, 3, 4, 6, 9]
    print("Lista:", valores)
    print("Suma de pares:", sumar_pares(valores))
