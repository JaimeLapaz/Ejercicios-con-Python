"""
Enunciado:

179. Clase Coche: Desarrolla una clase Coche con atributos como marca,
modelo y año, y métodos para acelerar y frenar.

Solución:
"""

from math import isfinite


class Coche:
    """Modela un coche con velocidad no negativa en km/h."""

    def __init__(self, marca: str, modelo: str, anio: int) -> None:
        if anio <= 0:
            raise ValueError("El año debe ser positivo.")
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad = 0.0

    def acelerar(self, incremento: float) -> float:
        """Aumenta la velocidad y devuelve el valor actualizado."""
        self._validar_cambio(incremento)
        nueva_velocidad = self.velocidad + incremento
        if not isfinite(nueva_velocidad):
            raise ValueError("La velocidad resultante no es finita.")
        self.velocidad = nueva_velocidad
        return self.velocidad

    def frenar(self, decremento: float) -> float:
        """Reduce la velocidad sin permitir valores negativos."""
        self._validar_cambio(decremento)
        self.velocidad = max(0.0, self.velocidad - decremento)
        return self.velocidad

    @staticmethod
    def _validar_cambio(cantidad: float) -> None:
        if not isfinite(cantidad) or cantidad <= 0:
            raise ValueError("El cambio de velocidad debe ser positivo y finito.")


if __name__ == "__main__":
    coche = Coche("Seat", "Ibiza", 2022)
    assert coche.velocidad == 0.0
    assert coche.acelerar(50) == 50.0
    assert coche.frenar(20) == 30.0
    assert coche.frenar(100) == 0.0
    print(f"{coche.marca} {coche.modelo}: {coche.velocidad} km/h")

    try:
        coche.acelerar(-10)
    except ValueError as error:
        print("Aceleración rechazada:", error)
    else:
        raise AssertionError("No se debe aceptar una aceleración negativa.")
