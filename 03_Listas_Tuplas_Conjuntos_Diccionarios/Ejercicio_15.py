'''
Enunciado:

15. **Invertir Diccionario**: Crea una función que invierta las claves y los valores en un diccionario.

Solución:
'''

def invert_dict(data: dict[any, any]) -> dict[any, any]:
    '''
    Invierte las claves y valores de un diccionario.
    
    Args:
    data (dict): Diccionario a invertir.
    
    Return:
    dict: Diccionario invertido.
    '''
    
    return {value: key for key, value in data.items()}

def main():
    data = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }
    
    inverted_data = invert_dict(data)
    
    print("Diccionario original:", data)
    print("Diccionario invertido:", inverted_data)

if __name__ == "__main__":
    main()