'''
Enunciado:

22. Definir una función `generar_n_caracteres()` que tome un entero n y 
devuelva el carácter multiplicado por n. Por ejemplo: `generar_n_caracteres(5, "x")` 
debería devolver "xxxxx".

Solución:
'''

def generar_n_caracteres(n, caracter):
    '''
    Esta función repite el caracter el número de veces indicado.
    
    Args:
    n (int): Número de veces que se debe repetir el caracter.
    caracter (str): Caracter a repetir.
    
    Return:
    str: Caracter repetido la cantidad de veces indicada.
    '''
    
    return caracter*n

def main():
    print(generar_n_caracteres(5, "x")) # Salida "xxxxx"
    
if __name__ == "__main__":
    main()