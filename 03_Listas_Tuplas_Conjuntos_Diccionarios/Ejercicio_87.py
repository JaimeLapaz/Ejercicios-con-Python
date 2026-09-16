"""
Enunciado:

87. Desarrolla un programa que encuentre la diferencia
simétrica entre dos conjuntos.

Solución:
"""


def diferencia_simetrica(conjunto1: set, conjunto2: set) -> set:
    """
    Obtiene los elementos presentes en uno de los conjuntos,
    pero no en ambos.

    Args:
        conjunto1 (set): Primer conjunto.
        conjunto2 (set): Segundo conjunto.

    Returns:
        set: Diferencia simétrica.
    """
    resultado = set()

    for elemento in conjunto1:
        if elemento not in conjunto2:
            resultado.add(elemento)

    for elemento in conjunto2:
        if elemento not in conjunto1:
            resultado.add(elemento)

    return resultado


if __name__ == "__main__":
    conjunto1 = {1, 2, 3, 4, 5}
    conjunto2 = {4, 5, 6, 7, 8}

    resultado = diferencia_simetrica(conjunto1, conjunto2)

    print("Diferencia simétrica:", resultado)
