"""
Enunciado:

171. Clase Vehículo: Desarrolla una clase Vehiculo con atributos como marca,
modelo y año, y métodos para encender y apagar el motor.

Solución:
"""


class Vehiculo:
    """Representa un vehículo y el estado de su motor."""

    def __init__(self, marca: str, modelo: str, anio: int) -> None:
        if anio <= 0:
            raise ValueError("El año debe ser positivo.")
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.motor_encendido = False

    def encender(self) -> str:
        """Enciende el motor si estaba apagado."""
        if self.motor_encendido:
            return "El motor ya está encendido."
        self.motor_encendido = True
        return "Motor encendido."

    def apagar(self) -> str:
        """Apaga el motor si estaba encendido."""
        if not self.motor_encendido:
            return "El motor ya está apagado."
        self.motor_encendido = False
        return "Motor apagado."


if __name__ == "__main__":
    vehiculo = Vehiculo("Toyota", "Corolla", 2022)
    assert vehiculo.encender() == "Motor encendido."
    assert vehiculo.motor_encendido
    print(vehiculo.encender())
    assert vehiculo.apagar() == "Motor apagado."
    assert not vehiculo.motor_encendido
