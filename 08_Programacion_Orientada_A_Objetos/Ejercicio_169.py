"""
Enunciado:

169. Clase Rectángulo: Implementa una clase Rectangulo con atributos para el
largo y ancho, y métodos para calcular el área y el perímetro.

Solución:
"""


class Rectangulo:
    """Representa un rectángulo y permite calcular sus medidas."""

    def __init__(self, largo: float, ancho: float) -> None:
        if largo <= 0 or ancho <= 0:
            raise ValueError("El largo y el ancho deben ser positivos.")
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self) -> float:
        """Calcula el área del rectángulo."""
        return self.largo * self.ancho

    def calcular_perimetro(self) -> float:
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.largo + self.ancho)


if __name__ == "__main__":
    rectangulo = Rectangulo(5, 3)
    print("Área:", rectangulo.calcular_area())
    print("Perímetro:", rectangulo.calcular_perimetro())
    assert rectangulo.calcular_area() == 15
    assert rectangulo.calcular_perimetro() == 16
