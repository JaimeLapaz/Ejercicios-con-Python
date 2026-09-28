"""
Enunciado:

122. Divisores de un número: Crea una función que encuentre todos los divisores de un
número después de validar que el número sea un entero positivo.

Solución:
"""

def divisores(numero: int) -> list[int]:
    """Devuelve todos los divisores de un entero positivo."""
    if not isinstance(numero, int) or isinstance(numero, bool):
        raise TypeError("El número debe ser un entero.")
    if numero <= 0:
        raise ValueError("El número debe ser positivo.")

    return [divisor for divisor in range(1, numero + 1) if numero % divisor == 0]


if __name__ == "__main__":
    for numero in (1, 12, 28):
        print(f"Divisores de {numero}: {divisores(numero)}")
