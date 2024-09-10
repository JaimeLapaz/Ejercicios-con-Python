'''
Enunciado:

20. **Diccionario Vacío**: Verifica si un diccionario está vacío o no.

Solución:
'''

# Función para verificar si un diccionario está vacío
def es_vacio(diccionario: dict) -> bool:
    '''
    Verifica si un diccionario está vacío o no.
    
    Args:
    diccionario (dict): Diccionario a verificar si es vacío o no.
    
    Return:
    bool: True si está vacío, False si no está vacío.
    '''
    
    if not diccionario:
        print('El diccionario está vacío')
        return True
    elif diccionario:
        print('El diccionario no está vacío')
        return False

if __name__ == "__main__":
    # Ejemplo de uso:

    # Diccionario vacío
    diccionario_vacio = {}

    # Diccionario no vacío
    diccionario_no_vacio = {'clave1': 'valor1', 'clave2': 'valor2'}
    
    # Verificar si los diccionarios están vacíos
    es_vacio(diccionario_vacio)  # Debería indicar que está vacío
    es_vacio(diccionario_no_vacio) # Debería indicar que no está vacío