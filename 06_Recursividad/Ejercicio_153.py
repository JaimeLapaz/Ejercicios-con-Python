"""
Enunciado:

153. Suma de Elementos en Lista: Implementa una función recursiva
que calcule la suma de todos los elementos en una lista.

Solución:
"""

Numero = int | float


def sumar_elementos(numeros: list[Numero]) -> Numero:
    """Devuelve recursivamente la suma de los elementos de una lista."""
    if not numeros:
        return 0
    return numeros[0] + sumar_elementos(numeros[1:])


if __name__ == "__main__":
    valores = [4, 7, -2, 5]
    decimales = [1.5, 2.5, 3.0]

    print("Suma:", sumar_elementos(valores))
    print("Suma de decimales:", sumar_elementos(decimales))
    assert sumar_elementos(valores) == 14
    assert sumar_elementos(decimales) == 7.0
    assert sumar_elementos([]) == 0
