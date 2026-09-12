'''
Enunciado:

35. Registro de Viajes: Diseña una aplicación para registrar viajes.

Utiliza un diccionario que almacene información sobre viajes, donde
cada viaje tiene un destino, una lista de lugares visitados
(almacenados como tuplas de nombre y fecha) y una descripción.

Solución:
'''


def agregar_viaje(
        viajes: dict,
        viaje_id: int,
        destino: str,
        descripcion: str
        ) -> bool:
    '''
    Añade un viaje al registro.

    Args:
        viajes (dict): Diccionario de viajes.
        viaje_id (int): Identificador del viaje.
        destino (str): Destino principal.
        descripcion (str): Descripción del viaje.

    Returns:
        bool: True si se añadió y False si ya existía.
    '''
    if viaje_id in viajes:
        return False

    viajes[viaje_id] = {
        "destino": destino,
        "lugares_visitados": [],
        "descripcion": descripcion
    }

    return True


def agregar_lugar_visitado(
        viajes: dict,
        viaje_id: int,
        lugar: str,
        fecha: str
        ) -> bool:
    '''
    Añade un lugar visitado a un viaje.

    Args:
        viajes (dict): Diccionario de viajes.
        viaje_id (int): Identificador del viaje.
        lugar (str): Lugar visitado.
        fecha (str): Fecha de la visita.

    Returns:
        bool: True si se añadió correctamente.
    '''
    if viaje_id not in viajes:
        return False

    viajes[viaje_id][
        "lugares_visitados"
    ].append(
        (lugar, fecha)
    )

    return True


def mostrar_viaje(
        viajes: dict,
        viaje_id: int
        ) -> None:
    '''
    Muestra toda la información de un viaje.
    '''
    if viaje_id not in viajes:
        print("El viaje no existe.")
        return

    viaje = viajes[viaje_id]

    print(f"\nDestino: {viaje['destino']}")
    print(
        f"Descripción: {viaje['descripcion']}"
    )

    print("Lugares visitados:")

    if not viaje["lugares_visitados"]:
        print("- Ninguno")
        return

    for lugar, fecha in viaje["lugares_visitados"]:
        print(f"- {lugar} ({fecha})")


if __name__ == "__main__":
    viajes = {}

    agregar_viaje(
        viajes,
        1,
        "Japón",
        "Viaje de dos semanas por Japón."
    )

    agregar_lugar_visitado(
        viajes,
        1,
        "Tokio",
        "01/09/2026"
    )

    agregar_lugar_visitado(
        viajes,
        1,
        "Kioto",
        "05/09/2026"
    )

    agregar_lugar_visitado(
        viajes,
        1,
        "Osaka",
        "08/09/2026"
    )

    mostrar_viaje(
        viajes,
        1
    )