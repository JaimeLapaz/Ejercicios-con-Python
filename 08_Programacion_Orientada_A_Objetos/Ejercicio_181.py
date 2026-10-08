"""
Enunciado:

181. Clase Alumno: Crea una clase Alumno con atributos como nombre,
edad y calificaciones, y métodos para calcular la calificación final.

Solución:
"""

from math import isfinite


class Alumno:
    """Almacena calificaciones de 0 a 10 y calcula su media aritmética."""

    def __init__(self, nombre: str, edad: int, calificaciones: list[float]) -> None:
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.nombre = nombre
        self.edad = edad
        self.calificaciones: list[float] = []
        for calificacion in calificaciones:
            self.agregar_calificacion(calificacion)

    def agregar_calificacion(self, calificacion: float) -> None:
        """Añade una nota si está comprendida entre 0 y 10."""
        if not isfinite(calificacion) or not 0 <= calificacion <= 10:
            raise ValueError("La calificación debe estar entre 0 y 10.")
        self.calificaciones.append(calificacion)

    def calcular_calificacion_final(self) -> float:
        """Devuelve la media de las notas; requiere al menos una."""
        if not self.calificaciones:
            raise ValueError("No hay calificaciones para calcular la nota final.")
        return sum(self.calificaciones) / len(self.calificaciones)


if __name__ == "__main__":
    alumno = Alumno("María", 18, [8.0, 7.0, 9.0])
    print("Calificación final:", alumno.calcular_calificacion_final())
    assert alumno.calcular_calificacion_final() == 8.0
    alumno.agregar_calificacion(10.0)
    assert alumno.calcular_calificacion_final() == 8.5

    try:
        Alumno("Luis", 17, []).calcular_calificacion_final()
    except ValueError as error:
        print("Sin calificaciones:", error)
    else:
        raise AssertionError("La lista vacía debe rechazarse.")
