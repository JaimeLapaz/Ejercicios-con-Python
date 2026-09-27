"""
Enunciado:

115. Número primo: Desarrolla una función que verifique si un número
es primo después de validar que sea un número entero positivo.

Solución:
"""


def es_primo(numero: int) -> bool:
    """
    Comprueba si un entero positivo es primo.

    Raises:
        TypeError: Si el valor no es un entero.
        ValueError: Si el entero no es positivo.
    """
    if isinstance(numero, bool) or not isinstance(numero, int):
        raise TypeError("El número debe ser un entero.")

    if numero <= 0:
        raise ValueError("El número debe ser positivo.")

    if numero == 1:
        return False

    divisor = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False

        divisor += 1

    return True


if __name__ == "__main__":
    for numero in (1, 2, 17, 20):
        resultado = "es primo" if es_primo(numero) else "no es primo"
        print(f"{numero} {resultado}.")
