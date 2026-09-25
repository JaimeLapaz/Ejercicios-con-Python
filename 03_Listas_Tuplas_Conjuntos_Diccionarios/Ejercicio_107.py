"""
Enunciado:

107. Escribe un programa que gestione un diccionario de productos en stock,
donde las claves son los productos y los valores son conjuntos de
ubicaciones donde se almacenan.

Solución:
"""


def agregar_producto(inventario: dict, producto: str) -> bool:
    """Añade un producto con un conjunto vacío de ubicaciones."""
    if producto in inventario:
        return False

    inventario[producto] = set()
    return True


def agregar_ubicacion(inventario: dict, producto: str, ubicacion: str) -> bool:
    """Registra una nueva ubicación para un producto existente."""
    if producto not in inventario or ubicacion in inventario[producto]:
        return False

    inventario[producto].add(ubicacion)
    return True


def eliminar_ubicacion(inventario: dict, producto: str, ubicacion: str) -> bool:
    """Elimina una ubicación asociada a un producto."""
    if producto not in inventario or ubicacion not in inventario[producto]:
        return False

    inventario[producto].remove(ubicacion)
    return True


def buscar_productos_por_ubicacion(inventario: dict, ubicacion: str) -> list:
    """Devuelve los productos almacenados en una ubicación."""
    productos = []

    for producto, ubicaciones in inventario.items():
        if ubicacion in ubicaciones:
            productos.append(producto)

    return productos


def mostrar_inventario(inventario: dict) -> None:
    """Muestra los productos y sus ubicaciones."""
    for producto, ubicaciones in inventario.items():
        print(f"{producto}:")

        if not ubicaciones:
            print("  - Sin ubicación asignada")
            continue

        for ubicacion in sorted(ubicaciones):
            print(f"  - {ubicacion}")


if __name__ == "__main__":
    inventario = {}

    agregar_producto(inventario, "Portátil")
    agregar_producto(inventario, "Teclado")
    agregar_producto(inventario, "Monitor")

    agregar_ubicacion(inventario, "Portátil", "Almacén A")
    agregar_ubicacion(inventario, "Portátil", "Almacén B")
    agregar_ubicacion(inventario, "Teclado", "Almacén A")
    agregar_ubicacion(inventario, "Monitor", "Almacén C")

    mostrar_inventario(inventario)

    print("\nProductos en Almacén A:")
    print(buscar_productos_por_ubicacion(inventario, "Almacén A"))

    print("\nDespués de retirar Portátil de Almacén B:")
    eliminar_ubicacion(inventario, "Portátil", "Almacén B")
    mostrar_inventario(inventario)
