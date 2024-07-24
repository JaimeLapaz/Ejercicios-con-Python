'''
Enunciado:

17. Escribir una función que tome un carácter y devuelva `True` si es una vocal, 
de lo contrario devuelve `False`.

Solución:
'''

def es_vocal(caracter):
    '''
    Esta función comprueba si una letra es vocal o no.
    
    Args:
    caracter (str): La letra a comprobar.
    
    Return:
    bool: True si la letra es vocal, False en caso contrario.
    '''
    # Definimos un conjunto de vocales
    vocales = {'a', 'e', 'i', 'o', 'u'}
    
    # Comprobamos si el caracter está en el conjunto de vocales.
    if caracter.lower() in vocales:
        return True
    else:
        return False
    
def main():
    print(es_vocal('a'))  # Salida: True
    print(es_vocal('b'))  # Salida: False
    print(es_vocal('E'))  # Salida: True
    print(es_vocal('z'))  # Salida: False
    
if __name__ == "__main__":
    main()