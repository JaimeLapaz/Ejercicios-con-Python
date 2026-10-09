"""
Enunciado:

184. Clase Computadora: Desarrolla una clase Computadora con atributos
como marca, modelo y capacidad de almacenamiento, y métodos para
instalar software.

Solución:
"""


class Computadora:
    """Instala programas respetando la capacidad de almacenamiento en GB."""

    def __init__(
        self, marca: str, modelo: str, capacidad_almacenamiento: int
    ) -> None:
        if not marca.strip() or not modelo.strip():
            raise ValueError("La marca y el modelo son obligatorios.")
        if capacidad_almacenamiento <= 0:
            raise ValueError("La capacidad debe ser positiva.")
        self.marca = marca
        self.modelo = modelo
        self.capacidad_almacenamiento = capacidad_almacenamiento
        self.software_instalado: dict[str, int] = {}

    def espacio_disponible(self) -> int:
        """Calcula los GB que quedan libres."""
        return self.capacidad_almacenamiento - sum(
            self.software_instalado.values()
        )

    def instalar_software(self, nombre: str, espacio_gb: int) -> None:
        """Instala un programa si hay espacio suficiente."""
        if not nombre.strip() or espacio_gb <= 0:
            raise ValueError("Indica un nombre y un tamaño positivo.")
        if nombre in self.software_instalado:
            raise ValueError("El programa ya está instalado.")
        if espacio_gb > self.espacio_disponible():
            raise ValueError("No hay espacio suficiente.")
        self.software_instalado[nombre] = espacio_gb


if __name__ == "__main__":
    computadora = Computadora("Lenovo", "ThinkPad", 256)
    computadora.instalar_software("Editor", 10)
    computadora.instalar_software("Python", 2)
    print("Programas:", computadora.software_instalado)
    print("Espacio disponible:", computadora.espacio_disponible(), "GB")
    assert computadora.espacio_disponible() == 244

    try:
        computadora.instalar_software("Juego", 250)
    except ValueError as error:
        print("Instalación rechazada:", error)
    else:
        raise AssertionError("No se debe superar la capacidad.")

    assert "Juego" not in computadora.software_instalado
