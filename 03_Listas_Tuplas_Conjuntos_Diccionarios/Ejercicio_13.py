'''
Enunciado:

13. **Valor Mínimo y Máximo**: Encuentra el valor mínimo y máximo en un diccionario de números.

Solución:
'''

def valor_min_max(number_dict: dict[any, float]) -> dict[str, float]:
    '''
    Encuentra el valor mínimo y máximo en un diccionario de números.
    
    Args:
    number_dict (dict): Diccionario con números como valores.
    Return:
    dict: Diccionario con el valor mínimo y máximo.
    '''
    if not number_dict:
        raise ValueError("El diccionario no puede estar vacío")
    
    values = number_dict.values()
    max_min_dict = {"Mínimo": min(values), "Máximo": max(values)}
    
    return max_min_dict

def main():
    data = {
        'a': 3.5,
        'b': 7.2,
        'c': 1.1,
        'd': 9.8,
        'e': 4.6
    }
    
    min_max = valor_min_max(data)
    for clave, valor in min_max.items():
        print(f"{clave}: {valor:.2f}")
        
if __name__ == "__main__":
    main()