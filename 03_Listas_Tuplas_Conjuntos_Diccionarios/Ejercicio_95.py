"""
Enunciado:

95. Diseña un programa que almacene información sobre películas
en un diccionario, donde cada película tiene un título, una lista
de actores principales y una tupla con la fecha de lanzamiento
y la duración.

Solución:
"""


def agregar_pelicula(
    peliculas: dict, titulo: str, actores: list, fecha_lanzamiento: str, duracion: int
) -> bool:
    """
    Agrega una película al registro.

    Args:
        peliculas (dict): Diccionario de películas.
        titulo (str): Título de la película.
        actores (list): Actores principales.
        fecha_lanzamiento (str): Fecha de lanzamiento.
        duracion (int): Duración en minutos.

    Returns:
        bool: True si se agregó y False si ya existía.
    """
    if titulo in peliculas:
        return False

    if duracion <= 0:
        return False

    peliculas[titulo] = {"actores": actores, "datos": (fecha_lanzamiento, duracion)}

    return True


def buscar_pelicula(peliculas: dict, titulo: str):
    """
    Busca una película por su título.

    Args:
        peliculas (dict): Diccionario de películas.
        titulo (str): Título que queremos buscar.

    Returns:
        dict | None: Información de la película o None.
    """
    return peliculas.get(titulo)


def mostrar_pelicula(peliculas: dict, titulo: str) -> None:
    """
    Muestra la información de una película.

    Args:
        peliculas (dict): Diccionario de películas.
        titulo (str): Título de la película.
    """
    pelicula = buscar_pelicula(peliculas, titulo)

    if pelicula is None:
        print("La película no existe.")
        return

    fecha, duracion = pelicula["datos"]

    print(f"\nTítulo: {titulo}")
    print("Actores principales:")

    for actor in pelicula["actores"]:
        print(f"- {actor}")

    print(f"Fecha de lanzamiento: {fecha}")
    print(f"Duración: {duracion} minutos")


if __name__ == "__main__":
    peliculas = {}

    agregar_pelicula(
        peliculas,
        "Interstellar",
        ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
        "07/11/2014",
        169,
    )

    agregar_pelicula(
        peliculas,
        "Origen",
        ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
        "16/07/2010",
        148,
    )

    mostrar_pelicula(peliculas, "Interstellar")
