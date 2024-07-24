'''
Enunciado:

20. Definir una función `es_palindromo()` que reconozca palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas). 
Ejemplo: `es_palindromo("radar")` debería devolver `True`.

Solución:
'''

def es_palindromo(text):
    '''
    Esta función comprueba si una palabra es un palíndromo o no.
    
    Args:
    text (str): La palabra a comprobar.
    
    Return:
    bool: True si la palabra es un palíndromo, False en caso contrario.
    '''
    # Comprobamos si tienen el mismo aspecto escritas de forma inversa.
    if text == text[::-1]:
        return True
    else:
        return False
    

def main():
    # Comprobamos si la palabra es un palíndromo.
    print(es_palindromo("radar")) # Salida: True
    print(es_palindromo("hola")) # Salida: False

if __name__ == "__main__":
    main()