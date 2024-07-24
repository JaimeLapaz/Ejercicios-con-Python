'''
Enunciado:

16. Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que Python tiene la función `len()` incorporada, pero escribirla por 
nosotros mismos resulta un muy buen ejercicio).

Solución:
'''

def calcular_longitud(elemento):
    '''
    Esta función calcula la longitud de una cadena de texto sin usar la función len().
    
    Args:
    elemento (srt) o (list): cadena de texto o lista.
    
    Return:
    int: Longitud de la cadena de texto o la lista.
    '''
    # Inicializamos la longitud en 0
    longitud = 0
    
    # Iteramos entre los elementos de la cadena de texto o la lista
    for i in elemento:
        # Incrementamos la longitud por cada iteracción.
        longitud += 1
    
    return longitud

def main():
    # Ejemplos de uso:
    lista_ejemplo = [1, 2, 3, 4, 5]
    cadena_ejemplo = "Hola, mundo!"

    print("Longitud de la lista:", calcular_longitud(lista_ejemplo))  # Salida: 5
    print("Longitud de la cadena:", calcular_longitud(cadena_ejemplo))  # Salida: 12
    
if __name__ == "__main__":
    main()