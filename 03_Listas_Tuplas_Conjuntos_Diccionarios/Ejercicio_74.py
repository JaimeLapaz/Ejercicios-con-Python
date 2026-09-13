'''
Enunciado:

74. Implementa una función que fusione dos diccionarios
sin utilizar el operador de actualización (update).

Solución:
'''


def fusionar_diccionarios(
        diccionario1: dict,
        diccionario2: dict
        ) -> dict:
    '''
    Fusiona dos diccionarios sin utilizar update().

    Si una clave aparece en ambos diccionarios,
    prevalece el valor del segundo.

    Args:
        diccionario1 (dict): Primer diccionario.
        diccionario2 (dict): Segundo diccionario.

    Returns:
        dict: Nuevo diccionario fusionado.
    '''
    resultado = {}

    for clave, valor in diccionario1.items():
        resultado[clave] = valor

    for clave, valor in diccionario2.items():
        resultado[clave] = valor

    return resultado


if __name__ == "__main__":
    productos1 = {
        "teclado": 29.99,
        "ratón": 15.50,
        "monitor": 199.99
    }

    productos2 = {
        "monitor": 189.99,
        "auriculares": 39.99,
        "webcam": 49.99
    }

    productos = fusionar_diccionarios(
        productos1,
        productos2
    )

    print(productos)