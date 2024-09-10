'''
Enunciado:

18. **Contar Vocales**: Cuenta cuántas vocales hay en una cadena de texto y almacena el 
resultado en un diccionario.

Solución:
'''

# Función para contar las vocales de un string y añadirlas a un diccionario.
def contar_vocales(cadena: str) -> dict:
    '''
    Esta función cuenta y almacena las vocales de una cadena de texto.
    
    Args:
    cadena (str): La cadena de texto a procesar.
    
    Return:
    dict: Un diccionario con las vocales como claves y sus conteos como valores.
    '''
    conteo_vocales = {vocal: 0 for vocal in "aeiou"}
    
    for caracter in cadena:
        if caracter.lower() in conteo_vocales:
            conteo_vocales[caracter.lower()] += 1
    
    return conteo_vocales

if  __name__ == "__main__":
    # Ejemplo de uso de la función
    texto = "Hola Mundo, este es un ejercicio para contar vocales."
    resultado = contar_vocales(texto)
    print("Conteo de vocales:", resultado)