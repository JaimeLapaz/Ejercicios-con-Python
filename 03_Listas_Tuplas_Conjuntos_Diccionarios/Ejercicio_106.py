"""
Enunciado:

106. Desarrolla una función que encuentre la intersección de múltiples
conjuntos almacenados en un diccionario.

Solución:
"""


def interseccion_conjuntos(conjuntos: dict) -> set:
    """Devuelve los elementos comunes a todos los conjuntos."""
    if not conjuntos:
        return set()

    valores = list(conjuntos.values())

    if not all(isinstance(conjunto, set) for conjunto in valores):
        raise TypeError("Todos los valores deben ser conjuntos.")

    resultado = valores[0].copy()

    for conjunto in valores[1:]:
        resultado.intersection_update(conjunto)

    return resultado


def mostrar_interseccion(conjuntos: dict) -> None:
    """Muestra los elementos comunes."""
    comunes = interseccion_conjuntos(conjuntos)

    if not comunes:
        print("No hay elementos comunes.")
        return

    print("Elementos comunes:")
    for elemento in sorted(comunes):
        print(f"- {elemento}")


if __name__ == "__main__":
    lenguajes = {
        "Ana": {"Python", "JavaScript", "SQL"},
        "Carlos": {"Python", "Java", "SQL"},
        "Laura": {"Python", "C#", "SQL"},
    }

    mostrar_interseccion(lenguajes)

    print("\nSegunda prueba:")
    mostrar_interseccion({"A": {1, 2}, "B": {3, 4}})
