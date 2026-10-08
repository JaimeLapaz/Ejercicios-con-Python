"""
Enunciado:

178. Clase Empleado: Diseña una clase Empleado con atributos como nombre,
salario y departamento, y métodos para calcular el aumento de salario.

Solución:
"""

from math import isfinite


class Empleado:
    """Representa a un empleado y permite calcular y aplicar aumentos."""

    def __init__(self, nombre: str, salario: float, departamento: str) -> None:
        if not isfinite(salario) or salario < 0:
            raise ValueError("El salario debe ser un número finito no negativo.")
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def calcular_aumento(self, porcentaje: float) -> float:
        """Devuelve el importe de un aumento porcentual sin cambiar el salario."""
        if not isfinite(porcentaje) or porcentaje < 0:
            raise ValueError("El porcentaje debe ser finito y no negativo.")
        return self.salario * porcentaje / 100

    def aplicar_aumento(self, porcentaje: float) -> float:
        """Actualiza el salario y devuelve su nuevo valor."""
        nuevo_salario = self.salario + self.calcular_aumento(porcentaje)
        if not isfinite(nuevo_salario):
            raise ValueError("El salario resultante no es finito.")
        self.salario = nuevo_salario
        return self.salario


if __name__ == "__main__":
    empleado = Empleado("Ana", 2000.0, "Informática")
    print("Aumento del 10 %:", empleado.calcular_aumento(10))
    assert empleado.calcular_aumento(10) == 200.0
    assert empleado.salario == 2000.0
    assert empleado.aplicar_aumento(10) == 2200.0
    assert empleado.salario == 2200.0

    try:
        empleado.aplicar_aumento(-5)
    except ValueError as error:
        print("Aumento rechazado:", error)
    else:
        raise AssertionError("Un porcentaje negativo debe rechazarse.")
