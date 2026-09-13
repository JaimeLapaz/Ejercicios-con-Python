'''
Enunciado:

73. Crea un programa que encuentre la clave con el valor máximo
en un diccionario de números enteros.

Solución:
'''


def clave_valor_maximo(diccionario: dict):
    '''
    Encuentra la clave asociada al valor máximo.

    Args:
        diccionario (dict): Diccionario con valores numéricos.

    Returns:
        any: Clave cuyo valor es el máximo.
        None: Si el diccionario está vacío.
    '''
    if not diccionario:
        return None

    clave_maxima = None
    valor_maximo = None

    for clave, valor in diccionario.items():

        if valor_maximo is None or valor > valor_maximo:
            valor_maximo = valor
            clave_maxima = clave

    return clave_maxima


if __name__ == "__main__":
    puntuaciones = {
        "Ana": 75,
        "Carlos": 92,
        "Laura": 88,
        "Miguel": 81
    }

    clave = clave_valor_maximo(
        puntuaciones
    )

    if clave is not None:
        print(
            f"La clave con el valor máximo es "
            f"'{clave}' con {puntuaciones[clave]}."
        )
    else:
        print("El diccionario está vacío.")