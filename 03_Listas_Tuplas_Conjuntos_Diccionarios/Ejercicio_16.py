'''
Enunciado:

16. **Calcular Histograma**: Crea un histograma de letras a partir de una cadena de texto.

Solución:
'''

def calculate_histogram(text: str) -> dict[str, int]:
    '''
    Calcula un histograma de letras a partir de una cadena de texto.
    
    Args:
    text (str): La cadena de texto a partir de la cual se calculará el histograma.
    
    Return:
    dict[str, int]: Un diccionario donde las claves son las letras del texto y los valores son 
    las veces que cada letra aparece en la cadena.
    '''
    
    histogram = {}
    
    for char in text:
        if char.isalpha(): # Considerar solo caracteres alfabéticos
            char.lower()
            if char in histogram:
                histogram[char] += 1
            else:
                histogram[char] = 1
    
    return histogram

def main():
    text = "Hola, mundo"
    histogram = calculate_histogram(text)
    
    print("Histograma de letras:")
    for letter, count in histogram.items():
        print(f"{letter}:", "#"*count)
        
if __name__ == "__main__":
    main()