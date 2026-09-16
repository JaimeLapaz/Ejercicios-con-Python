"""
Enunciado:

84. Implementa una función que verifique si un conjunto
es un subconjunto de otro conjunto.

Solución:
"""


def es_subconjunto(conjunto1: set, conjunto2: set) -> bool:
    """
    Comprueba si el primer conjunto es subconjunto del segundo.

    Args:
        conjunto1 (set): Conjunto que queremos comprobar.
        conjunto2 (set): Conjunto principal.

    Returns:
        bool: True si todos los elementos del primero
        aparecen en el segundo.
    """
    for elemento in conjunto1:
        if elemento not in conjunto2:
            return False

    return True


if __name__ == "__main__":
    conjunto1 = {2, 4}
    conjunto2 = {1, 2, 3, 4, 5}

    if es_subconjunto(conjunto1, conjunto2):
        print(f"{conjunto1} es subconjunto de {conjunto2}.")
    else:
        print(f"{conjunto1} no es subconjunto de {conjunto2}.")
