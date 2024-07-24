'''
Enunciado:

19. Definir una función `inversa()` que calcule la inversión de una cadena. 
Por ejemplo, la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".

Salida:
'''

def inversa(texto):
    '''
    Esta función invierte el orden de una cadena de texto.
    
    Args:
    texto (str): Cadena de texto a invertir.
    
    Return:
    str: Cadena de texto invertida.
    '''
    
    # Recorremos la cadena de texto en sentido inverso
    texto_inverso = texto[::-1]
    
    return texto_inverso

def main():
    texto = "estoy probando"
    print(inversa(texto)) # Salida: "odnaborp yotse"

if __name__ == "__main__":
    main()