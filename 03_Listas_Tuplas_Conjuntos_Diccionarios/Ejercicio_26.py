'''
Enunciado:

26. Diccionario de Traducción: Crea un diccionario que traduzca
palabras de un idioma a otro.

Solución:
'''


def traducir(diccionario: dict, palabra: str) -> str:
    '''
    Traduce una palabra utilizando un diccionario.

    Args:
        diccionario (dict): Diccionario con las traducciones.
        palabra (str): Palabra que se quiere traducir.

    Returns:
        str: Traducción o mensaje indicando que no existe.
    '''
    palabra = palabra.lower()

    if palabra in diccionario:
        return diccionario[palabra]

    return f"No conozco la traducción de '{palabra}'."


if __name__ == "__main__":
    espanol_ingles = {
        "hola": "hello",
        "adiós": "goodbye",
        "casa": "house",
        "perro": "dog",
        "gato": "cat",
        "libro": "book",
        "agua": "water"
    }

    print(traducir(espanol_ingles, "casa"))
    print(traducir(espanol_ingles, "GATO"))
    print(traducir(espanol_ingles, "ordenador"))