"""
Enunciado:

116. Día de la semana: Escribe una función que solicite al usuario
un número del 1 al 7 y devuelva el nombre del día de la semana
correspondiente después de validar la entrada.

Solución:
"""


def obtener_dia(numero: int) -> str:
    """
    Devuelve el día de la semana asociado a un número del 1 al 7.
    """
    if isinstance(numero, bool) or not isinstance(numero, int):
        raise TypeError("El día debe indicarse con un número entero.")

    dias = (
        "lunes",
        "martes",
        "miércoles",
        "jueves",
        "viernes",
        "sábado",
        "domingo",
    )

    if numero < 1 or numero > len(dias):
        raise ValueError("El número debe estar entre 1 y 7.")

    return dias[numero - 1]


def solicitar_dia() -> int:
    """Solicita y valida un número de día introducido por teclado."""
    entrada = input("Introduce un número del 1 al 7: ")

    try:
        numero = int(entrada)
    except ValueError as error:
        raise ValueError("Debes introducir un número entero.") from error

    obtener_dia(numero)
    return numero


if __name__ == "__main__":
    try:
        numero = solicitar_dia()
        print(f"El día correspondiente es {obtener_dia(numero)}.")
    except (TypeError, ValueError) as error:
        print(f"Entrada no válida: {error}")
