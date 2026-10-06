"""
Enunciado:

168. Clase Perro: Crea una clase Perro con atributos como nombre, raza y edad,
y métodos para ladrar y mostrar información básica.

Solución:
"""


class Perro:
    """Representa un perro con sus datos básicos."""

    def __init__(self, nombre: str, raza: str, edad: int) -> None:
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def ladrar(self) -> str:
        """Devuelve el sonido característico del perro."""
        return "¡Guau!"

    def mostrar_informacion(self) -> str:
        """Devuelve una descripción básica del perro."""
        return f"{self.nombre} es un {self.raza} de {self.edad} años."


if __name__ == "__main__":
    perro = Perro("Luna", "Labrador", 4)
    print(perro.ladrar())
    print(perro.mostrar_informacion())
    assert perro.ladrar() == "¡Guau!"
    assert perro.mostrar_informacion() == "Luna es un Labrador de 4 años."
