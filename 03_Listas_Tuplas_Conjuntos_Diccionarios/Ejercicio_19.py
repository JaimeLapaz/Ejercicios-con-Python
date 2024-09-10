'''
Enunciado:

19. **Ordenar Diccionario**: Ordena un diccionario por sus claves o valores.

Solución:
'''

# Función para ordenar un diccionario por claves o valores:
def ordenar_diccionario(diccionario: dict, orden: str = 'clave', reverso: bool = False) -> dict:
    '''
    Esta función ordena un diccionario por claves o valores, de forma ascendento o descendente.
    
    Args:
    diccionario (dict): El diccionario a ordenar.
    orden (str, optional): Si es 'clave' ordena por claves, si es 'valor' ordena por valor.
    reverso (bool, optional): Si es True, ordena de forma descendente. Defaults to False
    
    Return:
    dict: El diccionario ordenado.
    '''
    
    if  orden == 'clave':
        diccionario_ordenado = dict(sorted(diccionario.items(), key = lambda item: item[0], reverse = reverso))
    
    elif orden == 'valor':
        diccionario_ordenado = dict(sorted(diccionario.items(), key = lambda item: item[1], reverse = reverso))
        
    else:
        raise ValueError("El parámetro 'por' debe ser 'clave' o 'valor'")
    
    return diccionario_ordenado

if __name__ == "__main__":
    # Diccionario de ejemplo
    productos = {
        'manzanas': 1.20,
        'pan': 1.50,
        'leche': 1.80,
        'auriculares': 30.99,
        'teclado': 25.00
    }
    
    # Ejemplo de uso:

    # 1. Ordenar por clave en orden ascendente
    print("Ordenado por clave (ascendente):")
    print(ordenar_diccionario(productos, orden = 'clave'))

    # 2. Ordenar por clave en orden descendente
    print("\nOrdenado por clave (descendente):")
    print(ordenar_diccionario(productos, orden = 'clave', reverso=True))

    # 3. Ordenar por valor en orden ascendente
    print("\nOrdenado por valor (ascendente):")
    print(ordenar_diccionario(productos, orden = 'valor'))

    # 4. Ordenar por valor en orden descendente
    print("\nOrdenado por valor (descendente):")
    print(ordenar_diccionario(productos, orden = 'valor', reverso=True))