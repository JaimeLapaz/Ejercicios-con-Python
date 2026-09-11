'''
Enunciado:

30. Inventario de Tienda: Desarrolla un programa que administre el
inventario de una tienda.

Utiliza un diccionario para almacenar los productos como claves y
sus detalles (precio, cantidad en stock, etc.) como valores.

Permite agregar nuevos productos y actualizar la información existente.

Solución:
'''


def agregar_producto(
        inventario: dict,
        nombre: str,
        precio: float,
        stock: int
        ) -> bool:
    '''
    Agrega un nuevo producto al inventario.

    Args:
        inventario (dict): Diccionario con los productos.
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        stock (int): Cantidad disponible.

    Returns:
        bool: True si se agregó y False si ya existía.
    '''
    if nombre in inventario:
        return False

    inventario[nombre] = {
        "precio": precio,
        "stock": stock
    }

    return True


def actualizar_producto(
        inventario: dict,
        nombre: str,
        precio: float = None,
        stock: int = None
        ) -> bool:
    '''
    Actualiza los datos de un producto existente.

    Args:
        inventario (dict): Diccionario con los productos.
        nombre (str): Producto a modificar.
        precio (float): Nuevo precio.
        stock (int): Nuevo stock.

    Returns:
        bool: True si se actualizó y False si no existe.
    '''
    if nombre not in inventario:
        return False

    if precio is not None:
        inventario[nombre]["precio"] = precio

    if stock is not None:
        inventario[nombre]["stock"] = stock

    return True


def mostrar_inventario(inventario: dict) -> None:
    '''
    Muestra todos los productos del inventario.
    '''
    for nombre, datos in inventario.items():
        print(f"\nProducto: {nombre}")
        print(f"Precio: {datos['precio']:.2f} €")
        print(f"Stock: {datos['stock']}")


if __name__ == "__main__":
    inventario = {}

    agregar_producto(
        inventario,
        "Teclado",
        29.99,
        10
    )

    agregar_producto(
        inventario,
        "Ratón",
        15.50,
        25
    )

    agregar_producto(
        inventario,
        "Monitor",
        199.99,
        5
    )

    actualizar_producto(
        inventario,
        "Teclado",
        precio=27.99,
        stock=12
    )

    mostrar_inventario(inventario)