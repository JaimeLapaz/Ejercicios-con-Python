'''
Enunciado:

7. **Contar Elementos**: Escribe una función que cuente cuántas veces aparece cada elemento en una lista y lo almacene en un diccionario.

Solución:
'''

def contar_elementos(lista: list) -> dict:
    """
    Cuenta los elementos de una lista y los pasa a un diccionario.
    
    Args:
    lista (list): La lista a contar.
    
    Return:
    dict: Un diccionario con los elementos de la lista como claves y sus frecuencias.
    """
    conteo = {}
    for elemento in lista:
        if elemento in conteo:
            conteo[elemento] += 1
        else:
            conteo[elemento] = 1
    
    return conteo

if __name__ == "__main__":
    # Ejemplo de uso
    lista_de_ejemplo = ["manzana", "banana", "manzana", "naranja", "banana", "manzana", "kiwi"]
    resultado = contar_elementos(lista_de_ejemplo)
    print(resultado)
            