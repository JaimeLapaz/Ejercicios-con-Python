'''
Enunciado:

25. Diccionario de Frecuencias: Dada una lista de números,
crea un diccionario que muestre cuántas veces aparece cada número.

Solución:
'''


def contar_frecuencias(numeros: list) -> dict:
    '''
    Cuenta cuántas veces aparece cada número de una lista.

    Args:
        numeros (list): Lista de números.

    Returns:
        dict: Diccionario donde la clave es el número y
        el valor es su número de apariciones.
    '''
    frecuencias = {}

    for numero in numeros:
        if numero in frecuencias:
            frecuencias[numero] += 1
        else:
            frecuencias[numero] = 1

    return frecuencias


if __name__ == "__main__":
    numeros = [5, 2, 7, 5, 2, 5, 9, 7, 7, 7]

    resultado = contar_frecuencias(numeros)

    print(resultado)

    for numero, cantidad in resultado.items():
        print(f"El número {numero} aparece {cantidad} veces.")