"""
Enunciado:

121. Raíz cuadrada: Implementa una función que calcule la raíz cuadrada de un número
positivo después de validar la entrada.

Solución:
"""

from math import sqrt


def raiz_cuadrada(numero: float) -> float:
    """Calcula la raíz cuadrada de un número real positivo."""
    if isinstance(numero, bool) or not isinstance(numero, (int, float)):
        raise TypeError("El valor debe ser un número real.")
    if numero <= 0:
        raise ValueError("El número debe ser positivo.")

    return sqrt(numero)


if __name__ == "__main__":
    for numero in (4, 25, 2.5):
        print(f"√{numero} = {raiz_cuadrada(numero):.4f}")
