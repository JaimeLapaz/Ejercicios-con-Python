"""
Enunciado:

76. Crea una función que encuentre todas las claves que tienen
valores iguales en dos diccionarios diferentes.

Solución:
"""


def claves_con_valores_iguales(diccionario1: dict, diccionario2: dict) -> list:
    """
    Encuentra claves comunes con el mismo valor.

    Args:
        diccionario1 (dict): Primer diccionario.
        diccionario2 (dict): Segundo diccionario.

    Returns:
        list: Lista de claves con valores iguales.
    """
    resultado = []

    for clave, valor in diccionario1.items():
        if clave in diccionario2:
            if diccionario2[clave] == valor:
                resultado.append(clave)

    return resultado


if __name__ == "__main__":
    notas1 = {"Ana": 8, "Carlos": 7, "Laura": 9, "Miguel": 6}

    notas2 = {"Ana": 8, "Carlos": 9, "Laura": 9, "Pedro": 6}

    coincidencias = claves_con_valores_iguales(notas1, notas2)

    print("Claves con el mismo valor:", coincidencias)
