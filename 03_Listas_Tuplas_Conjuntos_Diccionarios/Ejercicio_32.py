'''
Enunciado:

32. Almacenamiento de Recetas: Diseña un programa que gestione
recetas de cocina.

Utiliza un diccionario para almacenar recetas donde cada receta tiene
un nombre, una lista de ingredientes (almacenados como tuplas de
nombre y cantidad), y un conjunto de instrucciones.

Solución:
'''


def agregar_receta(
        recetas: dict,
        nombre: str
        ) -> bool:
    '''
    Añade una nueva receta.

    Args:
        recetas (dict): Diccionario de recetas.
        nombre (str): Nombre de la receta.

    Returns:
        bool: True si se añadió y False si ya existía.
    '''
    if nombre in recetas:
        return False

    recetas[nombre] = {
        "ingredientes": [],
        "instrucciones": set()
    }

    return True


def agregar_ingrediente(
        recetas: dict,
        receta: str,
        ingrediente: str,
        cantidad: str
        ) -> bool:
    '''
    Añade un ingrediente a una receta.

    Args:
        recetas (dict): Diccionario de recetas.
        receta (str): Nombre de la receta.
        ingrediente (str): Nombre del ingrediente.
        cantidad (str): Cantidad necesaria.

    Returns:
        bool: True si se añadió correctamente.
    '''
    if receta not in recetas:
        return False

    recetas[receta]["ingredientes"].append(
        (ingrediente, cantidad)
    )

    return True


def agregar_instruccion(
        recetas: dict,
        receta: str,
        instruccion: str
        ) -> bool:
    '''
    Añade una instrucción a la receta.

    Args:
        recetas (dict): Diccionario de recetas.
        receta (str): Nombre de la receta.
        instruccion (str): Instrucción que se añadirá.

    Returns:
        bool: True si se añadió correctamente.
    '''
    if receta not in recetas:
        return False

    recetas[receta]["instrucciones"].add(
        instruccion
    )

    return True


def mostrar_receta(
        recetas: dict,
        nombre: str
        ) -> None:
    '''
    Muestra una receta completa.
    '''
    if nombre not in recetas:
        print("La receta no existe.")
        return

    receta = recetas[nombre]

    print(f"\nReceta: {nombre}")

    print("\nIngredientes:")

    for ingrediente, cantidad in receta["ingredientes"]:
        print(f"- {ingrediente}: {cantidad}")

    print("\nInstrucciones:")

    for instruccion in receta["instrucciones"]:
        print(f"- {instruccion}")


if __name__ == "__main__":
    recetas = {}

    agregar_receta(
        recetas,
        "Tortilla de patatas"
    )

    agregar_ingrediente(
        recetas,
        "Tortilla de patatas",
        "Patatas",
        "500 g"
    )

    agregar_ingrediente(
        recetas,
        "Tortilla de patatas",
        "Huevos",
        "5 unidades"
    )

    agregar_ingrediente(
        recetas,
        "Tortilla de patatas",
        "Aceite",
        "100 ml"
    )

    agregar_instruccion(
        recetas,
        "Tortilla de patatas",
        "Pelar y cortar las patatas."
    )

    agregar_instruccion(
        recetas,
        "Tortilla de patatas",
        "Freír las patatas."
    )

    agregar_instruccion(
        recetas,
        "Tortilla de patatas",
        "Batir los huevos."
    )

    agregar_instruccion(
        recetas,
        "Tortilla de patatas",
        "Mezclar y cocinar la tortilla."
    )

    mostrar_receta(
        recetas,
        "Tortilla de patatas"
    )