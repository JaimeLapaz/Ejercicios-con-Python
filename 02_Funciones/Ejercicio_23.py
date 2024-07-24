'''
23. Definir un procedimiento `histograma()` que tome una lista de números enteros e imprima un 
histograma en la pantalla. Ejemplo: `histograma([4, 9, 7])` debería imprimir lo siguiente:

    ```text
    ****
    *********
    *******
    ```
'''

def histograma(lista):
    '''
    Esta función dibuja el histograma de una lista de números enteros.
    
    Args:
    lista (list): Lista de números enteros.
    
    Return:
    none
    '''
    # Recorremos la lista
    for i in lista:
        # Imprimimos '*' por el elemento de la lista.
        print('*'*i)
        
def main():
    lista = [4, 9, 7]
    histograma(lista) 
    
if __name__ == "__main__":
    main()