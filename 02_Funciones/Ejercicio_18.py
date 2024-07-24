'''
Enunciado:

18. Escribir una función `sum()` y una función `multip()` que sumen y 
multipliquen respectivamente todos los números de una lista. 
Por ejemplo: `sum([1, 2, 3, 4])` debería devolver 10 y 
`multip([1, 2, 3, 4])` debería devolver 24.
'''

def sum(lista):
    '''
    Esta función suma todos los elementos de una lista.
    
    Args:
    lista (list): lista de números enteros o flotantes.
    
    Return:
    suma (int): suma de todos los elementos de la lista.
    '''
    # Inicializamos la suma en 0
    suma = 0
    
    # Iteramos entre los elementos de la lista
    for i in lista:
        # Sumamos los elementos de la lista
        suma += i
    
    return suma

def multip(lista):
    '''
    Esta función multiplica todos los elementos de una lista.
    
    Agrs:
    lista (list): lista de números enteros o flotantes.
    
    Return:
    producto (int): producto de todos los elementos de la lista.
    '''
    # Inicializamos el producto en 1 ya que vamos a multiplicar.
    producto = 1
    
    # Iteramos entre los elementos de la lista
    for i in lista:
        # Multiplicamos los elementos de la lista
        producto *= i
    
    return producto

def main():
    # Creamos una lista de números enteros
    lista = [1, 2, 3, 4]
    print(sum(lista)) # Salida: 10
    print(multip(lista)) # Salida: 24
    
if __name__ == "__main__":
    main()