'''
Enunciado:

21. Definir una función `superposicion()` que tome dos listas y 
devuelva `True` si tienen al menos un miembro en común o devuelva `False` de lo contrario. 
Escribir la función usando el bucle `for` anidado.

Solución:
'''

def superposicion(lista1, lista2):
    '''
    Esta función comprueba si las dos listas tienen al menos un miembro en común.
    
    Args:
    lista1 (list): lista 1 a comparar.
    lista2 (list): lista 2 a comparar.
    
    Return:
    bool: True si las dos listas tienen al menos un miembro en común.
    '''
    # Iteramos sobre cada elemento de la primera lista
    for i in lista1:
        # Iteramos sobre cada elemento de la segunda lista
        for j in lista2:
            # Comprobamos si hay una coincidencia
            if i == j:
                return True
    # Si no se encuentra ninguna coincidencia, devolvemos False
    return False

def main():
    print(superposicion([1, 2, 3], [4, 5, 6]))  # Salida: False
    print(superposicion([1, 2, 3], [3, 4, 5]))  # Salida: True
    print(superposicion(['a', 'b', 'c'], ['x', 'y', 'c']))  # Salida: True
    print(superposicion(['a', 'b', 'c'], ['x', 'y', 'z']))  # Salida: False

if __name__ == "__main__":
    main()