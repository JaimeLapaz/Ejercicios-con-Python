'''
Enunciado:

11. **Contar Palabras**: Dada una cadena de texto, crea un diccionario que cuente 
cuántas veces aparece cada palabra.

Solución:
'''

def clean_word(word: str) -> str:
    '''
    Limpia la palabra eliminando signos de puntuación y la convierte a minusculas.
    
    Args:
    word (str): La palabra a limpiar.
    Return:
    str: La palabra limpia.
    '''
    return ''.join(char for char in word if char.isalnum()).lower()

def count_word(text: str) -> dict[str, int]:
    '''
    Cuenta cuántas veces aparece cada palabra en el texto.
    
    Args:
    text (str): El texto a analizar.
    Return:
    dict[str, int]: Un diccionario con las palabras como claves y sus frecuencias como valores.
    '''
    word_counts = {}
    words = text.split()
    
    for word in words:
        cleaned_word = clean_word(word)
        if cleaned_word: # Ignorar palabras vacías después de limpiar
            word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1
            
    return word_counts

def main():
    text = "Hola, mundo. Hola, mundo. ¡Hola, mundo!"
    word_count = count_word(text)
    for word, count in word_count.items():
        print(f"{word}: {count}")
        
if __name__ == "__main__":
    main()