"""
Enunciado:

172. Clase Estudiante: Crea una clase Estudiante con atributos como nombre,
edad y calificaciones, y métodos para calcular el promedio de calificaciones.

Solución:
"""


class Estudiante:
    """Representa un estudiante y sus calificaciones."""

    def __init__(
        self, nombre: str, edad: int, calificaciones: list[float]
    ) -> None:
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones.copy()

    def calcular_promedio(self) -> float:
        """Calcula el promedio; exige al menos una calificación."""
        if not self.calificaciones:
            raise ValueError("Se necesita al menos una calificación.")
        return sum(self.calificaciones) / len(self.calificaciones)


if __name__ == "__main__":
    estudiante = Estudiante("Ana", 20, [8.5, 9.0, 7.5, 10.0])
    promedio = estudiante.calcular_promedio()
    print(f"Promedio de {estudiante.nombre}: {promedio:.2f}")
    assert promedio == 8.75

    try:
        Estudiante("Luis", 19, []).calcular_promedio()
    except ValueError as error:
        print("Sin promedio:", error)
