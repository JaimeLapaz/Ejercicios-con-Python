"""
Enunciado:

77. Desarrolla un programa que calcule la suma de los valores
en un diccionario anidado.

Solución:
"""


def sumar_diccionario_anidado(diccionario: dict) -> float:
    """
    Suma todos los valores numéricos de un diccionario anidado.

    Args:
        diccionario (dict): Diccionario que puede contener
        otros diccionarios.

    Returns:
        float: Suma de todos los valores numéricos.
    """
    total = 0

    for valor in diccionario.values():
        if isinstance(valor, dict):
            total += sumar_diccionario_anidado(valor)

        elif isinstance(valor, (int, float)):
            total += valor

    return total


if __name__ == "__main__":
    ventas = {
        "enero": {"tienda1": 1200, "tienda2": 850},
        "febrero": {"tienda1": 900, "tienda2": {"mañana": 400, "tarde": 500}},
    }

    total = sumar_diccionario_anidado(ventas)

    print(f"Suma total: {total}")
