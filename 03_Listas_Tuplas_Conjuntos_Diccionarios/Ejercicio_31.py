'''
Enunciado:

31. Registro de Películas: Crea un diccionario que contenga
información sobre películas, donde cada película tiene un título,
un año de lanzamiento y una lista de actores principales
representados como tuplas (nombre del actor, papel en la película).

Solución:
'''


def agregar_pelicula(
        peliculas: dict,
        identificador: int,
        titulo: str,
        anio: int
        ) -> None:
    '''
    Agrega una película al registro.

    Args:
        peliculas (dict): Diccionario de películas.
        identificador (int): Identificador único.
        titulo (str): Título de la película.
        anio (int): Año de lanzamiento.
    '''
    peliculas[identificador] = {
        "titulo": titulo,
        "anio": anio,
        "actores": []
    }


def agregar_actor(
        peliculas: dict,
        identificador: int,
        actor: str,
        papel: str
        ) -> bool:
    '''
    Agrega un actor a una película.

    Args:
        peliculas (dict): Registro de películas.
        identificador (int): Identificador de la película.
        actor (str): Nombre del actor.
        papel (str): Personaje interpretado.

    Returns:
        bool: True si se agregó correctamente.
    '''
    if identificador not in peliculas:
        return False

    peliculas[identificador]["actores"].append(
        (actor, papel)
    )

    return True


def mostrar_pelicula(
        peliculas: dict,
        identificador: int
        ) -> None:
    '''
    Muestra la información de una película.
    '''
    if identificador not in peliculas:
        print("La película no existe.")
        return

    pelicula = peliculas[identificador]

    print(f"\nTítulo: {pelicula['titulo']}")
    print(f"Año: {pelicula['anio']}")

    print("Actores:")

    for actor, papel in pelicula["actores"]:
        print(f"- {actor}: {papel}")


if __name__ == "__main__":
    peliculas = {}

    agregar_pelicula(
        peliculas,
        1,
        "El Señor de los Anillos",
        2001
    )

    agregar_actor(
        peliculas,
        1,
        "Elijah Wood",
        "Frodo Bolsón"
    )

    agregar_actor(
        peliculas,
        1,
        "Ian McKellen",
        "Gandalf"
    )

    agregar_actor(
        peliculas,
        1,
        "Viggo Mortensen",
        "Aragorn"
    )

    mostrar_pelicula(peliculas, 1)