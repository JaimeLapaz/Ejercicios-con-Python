"""
Enunciado:

119. Factorial de un número: Desarrolla una función que calcule el factorial de un
número después de validar que sea un número entero no negativo.

Solución:
"""

def factorial(numero: int) -> int:
    """Calcula el factorial de un entero no negativo."""
    if not isinstance(numero, int) or isinstance(numero, bool):
        raise TypeError("El número debe ser un entero.")
    if numero < 0:
        raise ValueError("El número debe ser no negativo.")

    resultado = 1
    for valor in range(2, numero + 1):
        resultado *= valor
    return resultado


if __name__ == "__main__":
    for numero in (0, 1, 5, 7):
        print(f"{numero}! = {factorial(numero)}")
