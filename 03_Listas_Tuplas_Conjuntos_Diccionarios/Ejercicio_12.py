'''
Enunciado:

12. **Eliminar Duplicados**: Elimina los elementos duplicados de una lista y almacénalos en un diccionario.

Solución:
'''

def remove_duplicates(items: list[any]) -> dict[any, int]:
    '''
    Elimina duplicados de la lista y los almacena en un diccionario con el número de apariciones.
    
    Args:
    items (list[any]): La lista de elementos a procesar.
    Return:
    dict[any, int]: Un diccionario con los elementos únicos como claves y las apariciones como valor.
    '''
    item_count = {}
    
    for item in items:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1
    
    return item_count

def main():
    items = [1, "apple", 2, "apple", 3.5, 3.5, "banana", (1, 2), (1, 2), (2, 3)]
    unique_items = remove_duplicates(items)
    
    print("Elementos sin duplicados:")
    for item, count in unique_items.items():
        print(f"Elemento: {item}, Aparece: {count} veces")
    
if __name__ == "__main__":
    main()