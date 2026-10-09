"""
Enunciado:

185. Clase Inventario: Crea una clase Inventario para gestionar un
inventario de productos con métodos para agregar, vender y mostrar
productos.

Solución:
"""

from dataclasses import dataclass
from math import isfinite


@dataclass
class Producto:
    """Datos de un producto almacenado en el inventario."""

    precio: float
    cantidad: int


class Inventario:
    """Controla el stock de productos identificados por su nombre."""

    def __init__(self) -> None:
        self._productos: dict[str, Producto] = {}

    def agregar_producto(
        self, nombre: str, precio: float, cantidad: int
    ) -> None:
        """Añade un producto o aumenta su stock si conserva el precio."""
        if not nombre.strip():
            raise ValueError("El producto debe tener un nombre.")
        if not isfinite(precio) or precio < 0 or cantidad <= 0:
            raise ValueError("El precio y la cantidad deben ser válidos.")

        if nombre in self._productos:
            producto = self._productos[nombre]
            if producto.precio != precio:
                raise ValueError("El producto existente tiene otro precio.")
            producto.cantidad += cantidad
        else:
            self._productos[nombre] = Producto(precio, cantidad)

    def vender_producto(self, nombre: str, cantidad: int) -> float:
        """Descuenta unidades y devuelve el importe de la venta."""
        if cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser positiva.")
        if nombre not in self._productos:
            raise KeyError(f"Producto desconocido: {nombre}")
        producto = self._productos[nombre]
        if cantidad > producto.cantidad:
            raise ValueError("No hay existencias suficientes.")
        producto.cantidad -= cantidad
        return producto.precio * cantidad

    def mostrar_productos(self) -> dict[str, tuple[float, int]]:
        """Devuelve una vista independiente de precios y cantidades."""
        return {
            nombre: (producto.precio, producto.cantidad)
            for nombre, producto in self._productos.items()
        }


if __name__ == "__main__":
    inventario = Inventario()
    inventario.agregar_producto("Lápiz", 0.5, 10)
    inventario.agregar_producto("Cuaderno", 3.0, 4)
    assert inventario.vender_producto("Lápiz", 2) == 1.0
    print("Inventario:", inventario.mostrar_productos())
    assert inventario.mostrar_productos() == {
        "Lápiz": (0.5, 8),
        "Cuaderno": (3.0, 4),
    }

    try:
        inventario.vender_producto("Cuaderno", 5)
    except ValueError as error:
        print("Venta rechazada:", error)
    else:
        raise AssertionError("No se puede vender más stock del disponible.")

    assert inventario.mostrar_productos()["Cuaderno"][1] == 4
