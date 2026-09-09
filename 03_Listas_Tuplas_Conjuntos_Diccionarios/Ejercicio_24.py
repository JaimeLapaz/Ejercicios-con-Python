'''
Enunciado:

24. Unir Listas en Diccionario: Convierte dos listas en un diccionario,
utilizando una como claves y la otra como valores.

Solución:
'''


def listas_a_diccionario(claves: list, valores: list) -> dict:
    '''
    Convierte dos listas en un diccionario.

    Args:
        claves (list): Lista que contiene las claves.
        valores (list): Lista que contiene los valores.

    Returns:
        dict: Diccionario creado a partir de las dos listas.

    Raises:
        ValueError: Si las listas no tienen la misma longitud.
    '''
    if len(claves) != len(valores):
        raise ValueError("Las dos listas deben tener la misma longitud.")

    return dict(zip(claves, valores))


if __name__ == "__main__":
    nombres = ["Ana", "Luis", "Marta", "Carlos"]
    edades = [25, 31, 22, 28]

    personas = listas_a_diccionario(nombres, edades)

    print(personas)