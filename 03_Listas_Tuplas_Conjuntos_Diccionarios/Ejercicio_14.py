'''
Enunciado:

14. **Eliminar Claves**: Escribe una función que elimine las claves de un diccionario si su valor es mayor que un cierto umbral.

Solución:
'''

def remove_keys_above_threshold(data: dict[any, float], threshold: float) -> dict[any, float]:
    '''
    Elimina las claves del diccionario cuyo valor sea mayor que el umbral dado.
    
    Args:
    data (dict[any, float]): Diccionario con claves de cualquier tipo y números como valores.
    threshold (float): Umbral para determinar si una clave debe ser eliminada.
    Return:
    dict[any, float]: Diccionario con claves eliminadas según el umbral.
    '''
    
    return {key: value for key, value in data.items() if value <= threshold}

def main():
    data = {
        'apple': 3.5,
        'banana': 7.2,
        'cherry': 1.1,
        'date': 9.8,
        'fig': 4.6
    }
    
    threshold = 5.0
    filtered_data = remove_keys_above_threshold(data, threshold)
    
    print("Diccionario original:", data)
    print("Diccionario filtrado:", filtered_data)
    
if __name__ == "__main__":
    main()