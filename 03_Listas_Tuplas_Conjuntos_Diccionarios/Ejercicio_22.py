'''
Enunciado:

22. Eliminar Clave: Elimina una clave específica de un diccionario si existe.

Solución:
'''


def eliminar_clave(diccionario: dict, clave: str) -> bool:
    '''
    Elimina una clave de un diccionario si existe.

    Args:
        diccionario (dict): Diccionario sobre el que trabajar.
        clave (str): Clave que se quiere eliminar.

    Returns:
        bool: True si se eliminó la clave, False si no existía.
    '''
    if clave in diccionario:
        del diccionario[clave]
        return True

    return False


if __name__ == "__main__":
    productos = {
        "manzanas": 1.20,
        "pan": 1.50,
        "leche": 1.80,
        "teclado": 25.00
    }

    clave = "pan"

    if eliminar_clave(productos, clave):
        print(f"La clave '{clave}' ha sido eliminada.")
    else:
        print(f"La clave '{clave}' no existe.")

    print(productos)