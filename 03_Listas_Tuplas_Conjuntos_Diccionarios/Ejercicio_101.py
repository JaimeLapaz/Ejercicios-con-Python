"""
Enunciado:

101. Desarrolla un programa que administre un diccionario de
ciudades y sus temperaturas máximas diarias, almacenadas como
una lista de tuplas con fechas y temperaturas.

Solución:
"""


def agregar_temperatura(
    ciudades: dict,
    ciudad: str,
    fecha: str,
    temperatura: float,
) -> None:
    """
    Registra una temperatura máxima diaria para una ciudad.

    Args:
        ciudades (dict): Diccionario con los registros.
        ciudad (str): Nombre de la ciudad.
        fecha (str): Fecha del registro.
        temperatura (float): Temperatura máxima del día.
    """
    if ciudad not in ciudades:
        ciudades[ciudad] = []

    ciudades[ciudad].append((fecha, temperatura))


def obtener_temperatura_maxima(ciudades: dict, ciudad: str):
    """
    Obtiene el registro con mayor temperatura de una ciudad.

    Returns:
        tuple | None: Tupla (fecha, temperatura) o None si no hay datos.
    """
    registros = ciudades.get(ciudad, [])

    if not registros:
        return None

    registro_maximo = registros[0]

    for registro in registros[1:]:
        if registro[1] > registro_maximo[1]:
            registro_maximo = registro

    return registro_maximo


def mostrar_temperaturas(ciudades: dict, ciudad: str) -> None:
    """Muestra las temperaturas registradas para una ciudad."""
    registros = ciudades.get(ciudad)

    if not registros:
        print(f"No hay temperaturas registradas para {ciudad}.")
        return

    print(f"Temperaturas máximas de {ciudad}:")

    for fecha, temperatura in registros:
        print(f"- {fecha}: {temperatura:.1f} °C")

    fecha, temperatura = obtener_temperatura_maxima(ciudades, ciudad)
    print(f"Máxima registrada: {temperatura:.1f} °C ({fecha})")


if __name__ == "__main__":
    ciudades = {}

    agregar_temperatura(ciudades, "Granada", "2026-07-01", 35.4)
    agregar_temperatura(ciudades, "Granada", "2026-07-02", 37.1)
    agregar_temperatura(ciudades, "Granada", "2026-07-03", 36.2)
    agregar_temperatura(ciudades, "Málaga", "2026-07-01", 31.8)

    mostrar_temperaturas(ciudades, "Granada")
    print()
    mostrar_temperaturas(ciudades, "Sevilla")
