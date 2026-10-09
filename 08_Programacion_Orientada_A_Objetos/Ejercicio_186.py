"""
Enunciado:

186. Clase Hotel: Implementa una clase Hotel con atributos como
nombre y habitaciones, y métodos para reservar y desocupar habitaciones.

Solución:
"""


class Hotel:
    """Controla qué habitaciones están disponibles."""

    def __init__(self, nombre: str, habitaciones: list[int]) -> None:
        if not nombre.strip():
            raise ValueError("Se necesita un nombre.")
        if not habitaciones or len(set(habitaciones)) != len(habitaciones):
            raise ValueError("Indica habitaciones diferentes.")
        if any(numero <= 0 for numero in habitaciones):
            raise ValueError("Los números de habitación deben ser positivos.")
        self.nombre = nombre
        self.habitaciones = {numero: False for numero in habitaciones}

    def reservar(self, numero: int) -> None:
        """Marca una habitación como ocupada."""
        if numero not in self.habitaciones:
            raise KeyError(numero)
        if self.habitaciones[numero]:
            raise ValueError("Habitación ocupada.")
        self.habitaciones[numero] = True

    def desocupar(self, numero: int) -> None:
        """Marca una habitación como libre."""
        if numero not in self.habitaciones:
            raise KeyError(numero)
        if not self.habitaciones[numero]:
            raise ValueError("Habitación libre.")
        self.habitaciones[numero] = False

    def mostrar_habitaciones(self) -> dict[int, bool]:
        """Devuelve una copia del estado de las habitaciones."""
        return self.habitaciones.copy()


if __name__ == "__main__":
    hotel = Hotel("Mar Azul", [101, 102, 201])
    hotel.reservar(101)
    print(hotel.mostrar_habitaciones())
    assert hotel.mostrar_habitaciones()[101] is True
    try:
        hotel.reservar(101)
    except ValueError:
        print("No se puede reservar dos veces.")
    else:
        raise AssertionError("La habitación ya estaba ocupada.")
    hotel.desocupar(101)
    assert hotel.mostrar_habitaciones()[101] is False
