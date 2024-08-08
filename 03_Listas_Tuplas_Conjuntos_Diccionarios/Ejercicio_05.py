'''
Enunciado:

5. Escribir un programa que procese strings ingresados por el usuario. 
La lectura finaliza cuando se hayan procesado 50 strings. 
Al finalizar, informar la cantidad total de ocurrencias de cada carácter, 
en todos los strings ingresados. Ejemplo: "r":5, "%":3, "a":8, "9":1.
¿Cómo se podrían informar las ocurrencias de las letras del alfabeto únicamente, 
incluyendo el valor 0 para las letras que no aparecieron?

Solución:
'''

from collections import defaultdict
from typing import List, Dict

def contar_ocurrencias_caracteres(strings: List[str]) -> Dict[str, int]:
    """
    Cuenta las ocurrencias de cada carácter en una lista de strings.

    Args:
        strings (list): Lista de strings ingresados por el usuario.

    Returns:
        dict: Diccionario con las ocurrencias de cada carácter.
    """
    ocurrencias = defaultdict(int)
    
    for s in strings:
        for char in s:
            ocurrencias[char] += 1
    
    return ocurrencias

def contar_ocurrencias_letras(strings: List[str]) -> Dict[str, int]:
    """
    Cuenta las ocurrencias de cada letra del alfabeto español en una lista de strings,
    incluyendo letras que no aparecieron.

    Args:
        strings (list): Lista de strings ingresados por el usuario.

    Returns:
        dict: Diccionario con las ocurrencias de cada letra del alfabeto español.
    """
    # Letras del alfabeto español, incluyendo la ñ
    alfabeto_espanol = "abcdefghijklmnñopqrstuvwxyz"
    
    letras_ocurrencias = {letra: 0 for letra in alfabeto_espanol}
    
    for s in strings:
        for char in s.lower():
            if char in letras_ocurrencias:
                letras_ocurrencias[char] += 1
    
    return letras_ocurrencias

def main():
    strings_ingresados = []
    
    # Leer 50 strings del usuario
    for i in range(50):
        string_input = input(f"Ingrese el string {i+1}/50: ").strip()
        strings_ingresados.append(string_input)
    
    # Contar todas las ocurrencias de caracteres
    ocurrencias = contar_ocurrencias_caracteres(strings_ingresados)
    print("\nOcurrencias de todos los caracteres:")
    for char, count in ocurrencias.items():
        print(f"'{char}': {count}")

    # Contar ocurrencias de letras del alfabeto únicamente
    ocurrencias_letras = contar_ocurrencias_letras(strings_ingresados)
    print("\nOcurrencias de las letras del alfabeto:")
    for letra, count in ocurrencias_letras.items():
        print(f"'{letra}': {count}")

if __name__ == "__main__":
    main()