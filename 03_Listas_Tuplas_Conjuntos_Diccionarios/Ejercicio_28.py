'''
Enunciado:

28. Puntuaciones de Jugadores: Diseña un juego que registre las
puntuaciones de múltiples jugadores.

Crea un diccionario que almacene el nombre de cada jugador como clave
y una tupla de sus puntuaciones como valor. Luego, permite que los
jugadores agreguen nuevas puntuaciones a sus registros.

Solución:
'''


def agregar_jugador(jugadores: dict, nombre: str) -> None:
    '''
    Añade un jugador al diccionario.

    Args:
        jugadores (dict): Diccionario de jugadores.
        nombre (str): Nombre del nuevo jugador.
    '''
    if nombre not in jugadores:
        jugadores[nombre] = ()


def agregar_puntuacion(
        jugadores: dict,
        nombre: str,
        puntuacion: int
        ) -> None:
    '''
    Añade una puntuación al historial de un jugador.

    Args:
        jugadores (dict): Diccionario de jugadores.
        nombre (str): Nombre del jugador.
        puntuacion (int): Nueva puntuación.
    '''
    if nombre not in jugadores:
        jugadores[nombre] = ()

    jugadores[nombre] += (puntuacion,)


def mejor_puntuacion(jugadores: dict, nombre: str):
    '''
    Obtiene la puntuación más alta de un jugador.

    Args:
        jugadores (dict): Diccionario de jugadores.
        nombre (str): Nombre del jugador.

    Returns:
        int | None: Mejor puntuación o None si no tiene puntuaciones.
    '''
    if nombre not in jugadores:
        return None

    if not jugadores[nombre]:
        return None

    return max(jugadores[nombre])


def mostrar_jugadores(jugadores: dict) -> None:
    '''
    Muestra los jugadores y sus puntuaciones.

    Args:
        jugadores (dict): Diccionario de jugadores.
    '''
    for nombre, puntuaciones in jugadores.items():

        print(f"\nJugador: {nombre}")
        print(f"Puntuaciones: {puntuaciones}")

        mejor = mejor_puntuacion(jugadores, nombre)

        if mejor is None:
            print("Todavía no tiene puntuaciones.")
        else:
            print(f"Mejor puntuación: {mejor}")


if __name__ == "__main__":
    jugadores = {}

    agregar_jugador(jugadores, "Jaime")
    agregar_jugador(jugadores, "Ana")

    agregar_puntuacion(jugadores, "Jaime", 1200)
    agregar_puntuacion(jugadores, "Jaime", 1850)
    agregar_puntuacion(jugadores, "Jaime", 1600)

    agregar_puntuacion(jugadores, "Ana", 950)
    agregar_puntuacion(jugadores, "Ana", 2100)

    mostrar_jugadores(jugadores)