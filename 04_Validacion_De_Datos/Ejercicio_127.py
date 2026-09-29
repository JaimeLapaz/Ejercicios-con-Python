"""
Enunciado:

127. Eliminar elementos duplicados: Desarrolla una función que elimine elementos
duplicados de una lista después de validar que la entrada sea una lista de valores.

Solución:
"""

def eliminar_duplicados(valores: list) -> list:
    """Devuelve una lista sin duplicados, conservando el orden original."""
    if not isinstance(valores, list):
        raise TypeError("La entrada debe ser una lista.")

    resultado = []
    for valor in valores:
        if valor not in resultado:
            resultado.append(valor)
    return resultado


if __name__ == "__main__":
    valores = [3, 1, 3, 2, 1, 4, 2, 5]
    print("Lista original:", valores)
    print("Sin duplicados:", eliminar_duplicados(valores))
