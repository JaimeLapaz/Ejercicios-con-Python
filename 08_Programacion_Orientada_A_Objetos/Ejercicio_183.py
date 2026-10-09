"""
Enunciado:

183. Clase Restaurante: Diseña una clase Restaurante con atributos
como nombre y menú, y métodos para agregar platos y mostrar el menú.

Solución:
"""

from math import isfinite


class Restaurante:
    """Gestiona los platos y precios de un restaurante."""

    def __init__(self, nombre: str, menu: dict[str, float] | None = None) -> None:
        if not nombre.strip():
            raise ValueError("El restaurante debe tener un nombre.")
        self.nombre = nombre
        self._menu: dict[str, float] = {}
        for plato, precio in (menu or {}).items():
            self.agregar_plato(plato, precio)

    def agregar_plato(self, plato: str, precio: float) -> None:
        """Añade un plato nuevo con un precio positivo."""
        if not plato.strip():
            raise ValueError("El plato debe tener un nombre.")
        if not isfinite(precio) or precio <= 0:
            raise ValueError("El precio debe ser un número positivo y finito.")
        if plato in self._menu:
            raise ValueError("El plato ya existe en el menú.")
        self._menu[plato] = precio

    def mostrar_menu(self) -> dict[str, float]:
        """Devuelve una copia del menú para evitar cambios externos."""
        return self._menu.copy()


if __name__ == "__main__":
    restaurante = Restaurante("La Plaza", {"Ensalada": 7.5})
    restaurante.agregar_plato("Sopa", 5.0)
    menu = restaurante.mostrar_menu()
    print(f"Menú de {restaurante.nombre}:", menu)
    assert menu == {"Ensalada": 7.5, "Sopa": 5.0}

    menu["Sopa"] = 100.0
    assert restaurante.mostrar_menu()["Sopa"] == 5.0

    try:
        restaurante.agregar_plato("Postre", -2.0)
    except ValueError as error:
        print("Precio inválido:", error)
    else:
        raise AssertionError("Se debe rechazar un precio negativo.")
