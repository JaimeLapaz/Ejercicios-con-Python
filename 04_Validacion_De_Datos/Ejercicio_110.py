"""
Enunciado:

110. Calificación de un examen: Crea una función que tome una calificación
como entrada y valide que esté en el rango de 0 a 100.

Solución:
"""


def validar_calificacion(calificacion) -> float:
    """Valida que una calificación sea numérica y esté entre 0 y 100."""
    if isinstance(calificacion, bool) or not isinstance(
        calificacion, (int, float)
    ):
        raise TypeError("La calificación debe ser un número.")

    if calificacion < 0 or calificacion > 100:
        raise ValueError("La calificación debe estar entre 0 y 100.")

    return float(calificacion)


if __name__ == "__main__":
    print(f"Calificación válida: {validar_calificacion(87.5)}")

    for valor in (-5, 120):
        try:
            validar_calificacion(valor)
        except ValueError as error:
            print(f"Error con {valor}: {error}")
