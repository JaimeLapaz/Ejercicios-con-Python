"""
Enunciado:

174. Clase Tienda: Diseña una clase Tienda con una lista de productos
y métodos para agregar productos y calcular el precio total de la compra.

Solución:
"""


class Producto:
    """Representa un producto disponible en la tienda."""

    def __init__(self, nombre: str, precio: float) -> None:
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.nombre = nombre
        self.precio = precio


class Tienda:
    """Gestiona los productos incluidos en una compra."""

    def __init__(self) -> None:
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        """Añade un producto a la compra."""
        self.productos.append(producto)

    def calcular_precio_total(self) -> float:
        """Calcula el precio total de los productos."""
        return sum(producto.precio for producto in self.productos)


if __name__ == "__main__":
    tienda = Tienda()
    tienda.agregar_producto(Producto("Cuaderno", 3.50))
    tienda.agregar_producto(Producto("Bolígrafo", 1.25))
    print("Total:", tienda.calcular_precio_total())
    assert tienda.calcular_precio_total() == 4.75
