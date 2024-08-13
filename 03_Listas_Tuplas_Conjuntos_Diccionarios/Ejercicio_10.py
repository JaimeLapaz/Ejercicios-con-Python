'''
Enunciado:

10. **Unir Diccionarios**: Combina dos diccionarios en uno solo.

Solución:
'''

def unir_diccionarios(dict1: dict, dict2: dict) -> dict:
    """
    Esta función une dos diccionarios en uno solo. En caso de que una clave esté en ambos diccionarios,
    se utiliza el valor del segundo diccionario.

    Args:
        dict1 (dict): El primer diccionario a unir.
        dict2 (dict): El segundo diccionario a unir.

    Returns:
        dict: La unión de los dos diccionarios.
    """
    union = {**dict1, **dict2}
    
    return union

if __name__ == "__main__":
    # Ejemplo de uso
    calificaciones_dic1 = {
        "Juan": 85.5,
        "María": 92.0,
        "Pedro": 78.0
    }

    calificaciones_dic2 = {
        "Laura": 88.5,
        "Sofía": 91.0,
        "Pedro": 95.0  # Este valor sobrescribirá el de Pedro en dic1
    }

    calificaciones_unidas = unir_diccionarios(calificaciones_dic1, calificaciones_dic2)
    print(calificaciones_unidas)