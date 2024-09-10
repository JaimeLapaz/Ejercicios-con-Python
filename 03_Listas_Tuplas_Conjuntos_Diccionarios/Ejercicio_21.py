'''
Enunciado:

21. **Buscar Clave**: Escribe una función que busque una clave en un diccionario y devuelva 
su valor o un mensaje de error si no se encuentra.

Solución:
'''

# Función para buscar una clave en un diccionario
def buscar_clave(diccionario: dict, clave: str) -> any:
    ''' 
    Esta función busca una clave en un diccionario.
    
    Args:
    diccionario (dict): Diccionario con las claves y valores.
    clave (str): La clave a buscar.
    
    Return:
    any: el valor o un mensaje de error.
    '''
    if clave in diccionario:
        return diccionario[clave]
    else:
        return f"Error: La clave '{clave}' no se encuentra en el diccionario."
    
    
if __name__ == "__main__":
    # Crear un diccionario
    productos = {
        'manzanas': 1.20,
        'pan': 1.50,
        'leche': 1.80,
        'auriculares': 30.99,
        'teclado': 25.00
    }

    # Búsqueda de claves
    resultado1 = buscar_clave(productos, 'pan')         # Clave existente
    resultado2 = buscar_clave(productos, 'telefono')    # Clave no existente

    print(resultado1)  # Debería devolver el valor asociado a 'pan'
    print(resultado2)  # Debería devolver un mensaje de error