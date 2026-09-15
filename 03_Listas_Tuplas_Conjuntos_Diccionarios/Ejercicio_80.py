"""
Enunciado:

80. Diseña un programa que combine dos listas de tuplas en una
sola lista, eliminando duplicados basados en el primer elemento
de cada tupla.

Solución:
"""


def combinar_tuplas(lista1: list, lista2: list) -> list:
    """
    Combina dos listas de tuplas evitando claves duplicadas.

    El primer elemento de cada tupla se utiliza para determinar
    si ya existe un elemento equivalente.

    Args:
        lista1 (list): Primera lista de tuplas.
        lista2 (list): Segunda lista de tuplas.

    Returns:
        list: Lista combinada sin duplicados.
    """
    resultado = []
    elementos_vistos = set()

    for tupla in lista1 + lista2:
        if not tupla:
            continue

        clave = tupla[0]

        if clave not in elementos_vistos:
            resultado.append(tupla)
            elementos_vistos.add(clave)

    return resultado


if __name__ == "__main__":
    productos1 = [("teclado", 29.99), ("ratón", 15.50), ("monitor", 199.99)]

    productos2 = [("monitor", 189.99), ("webcam", 49.99), ("auriculares", 39.99)]

    productos = combinar_tuplas(productos1, productos2)

    print("Lista combinada:")

    for producto in productos:
        print(producto)
