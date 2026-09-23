"""
Enunciado:

102. Escribe una función que encuentre el elemento más común
en una lista de tuplas y muestre cuántas veces aparece.

Solución:
"""


def elemento_mas_comun(tuplas: list):
    """
    Encuentra el elemento individual más repetido entre las tuplas.

    Args:
        tuplas (list): Lista de tuplas.

    Returns:
        tuple | None: Tupla (elemento, apariciones), o None si no hay datos.
    """
    frecuencias = {}

    for tupla in tuplas:
        for elemento in tupla:
            frecuencias[elemento] = frecuencias.get(elemento, 0) + 1

    if not frecuencias:
        return None

    mas_comun = None
    mayor_frecuencia = 0

    for elemento, frecuencia in frecuencias.items():
        if frecuencia > mayor_frecuencia:
            mas_comun = elemento
            mayor_frecuencia = frecuencia

    return mas_comun, mayor_frecuencia


if __name__ == "__main__":
    datos = [
        ("Python", "Django"),
        ("JavaScript", "React"),
        ("Python", "Flask"),
        ("JavaScript", "Python"),
    ]

    resultado = elemento_mas_comun(datos)

    if resultado is not None:
        elemento, apariciones = resultado
        print(f"Elemento más común: {elemento}")
        print(f"Apariciones: {apariciones}")
    else:
        print("La lista no contiene elementos.")

    print("\nSegunda prueba:")
    print(elemento_mas_comun([]))
