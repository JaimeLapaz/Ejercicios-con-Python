"""
Enunciado:

124. Cálculo de área: Escribe una función que calcule el área de una figura geométrica
después de validar que los valores de entrada sean números reales positivos.

Solución:
"""

from math import pi


def validar_positivo(valor: float, nombre: str) -> None:
    """Valida que un valor sea numérico y positivo."""
    if not isinstance(valor, (int, float)) or isinstance(valor, bool):
        raise TypeError(f"{nombre} debe ser un número real.")
    if valor <= 0:
        raise ValueError(f"{nombre} debe ser positivo.")


def calcular_area(figura: str, *medidas: float) -> float:
    """Calcula el área de un cuadrado, rectángulo, triángulo o círculo."""
    figura = figura.lower()

    if figura == "cuadrado" and len(medidas) == 1:
        validar_positivo(medidas[0], "El lado")
        return medidas[0] ** 2
    if figura == "rectangulo" and len(medidas) == 2:
        validar_positivo(medidas[0], "La base")
        validar_positivo(medidas[1], "La altura")
        return medidas[0] * medidas[1]
    if figura == "triangulo" and len(medidas) == 2:
        validar_positivo(medidas[0], "La base")
        validar_positivo(medidas[1], "La altura")
        return medidas[0] * medidas[1] / 2
    if figura == "circulo" and len(medidas) == 1:
        validar_positivo(medidas[0], "El radio")
        return pi * medidas[0] ** 2

    raise ValueError("Figura no válida o número de medidas incorrecto.")


if __name__ == "__main__":
    print("Área del cuadrado:", calcular_area("cuadrado", 4))
    print("Área del rectángulo:", calcular_area("rectangulo", 5, 3))
    print("Área del triángulo:", calcular_area("triangulo", 6, 2))
    print("Área del círculo:", calcular_area("circulo", 3))
