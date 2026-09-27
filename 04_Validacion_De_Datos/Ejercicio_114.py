"""
Enunciado:

114. Número positivo o negativo: Crea una función que tome un número
como entrada y determine si es positivo, negativo o cero.

Solución:
"""


def clasificar_numero(numero: int | float) -> str:
    """
    Determina si un número es positivo, negativo o cero.

    Raises:
        TypeError: Si el valor no es numérico.
    """
    if isinstance(numero, bool) or not isinstance(numero, (int, float)):
        raise TypeError("El valor debe ser un número.")

    if numero > 0:
        return "positivo"

    if numero < 0:
        return "negativo"

    return "cero"


if __name__ == "__main__":
    numeros = (12, -4.5, 0)

    for numero in numeros:
        print(f"{numero} es {clasificar_numero(numero)}.")
