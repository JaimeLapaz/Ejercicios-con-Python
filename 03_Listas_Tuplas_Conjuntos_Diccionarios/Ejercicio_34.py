'''
Enunciado:

34. Registro de Compras: Desarrolla un programa para registrar compras
en una tienda en línea.

Utiliza un diccionario para rastrear las compras de los clientes donde
cada cliente tiene un identificador único y una lista de productos
comprados (almacenados como tuplas de nombre del producto y cantidad).

Solución:
'''


def agregar_cliente(
        compras: dict,
        cliente_id: int
        ) -> bool:
    '''
    Añade un cliente al registro.

    Args:
        compras (dict): Diccionario de compras.
        cliente_id (int): Identificador único del cliente.

    Returns:
        bool: True si se agregó y False si ya existía.
    '''
    if cliente_id in compras:
        return False

    compras[cliente_id] = []

    return True


def registrar_compra(
        compras: dict,
        cliente_id: int,
        producto: str,
        cantidad: int
        ) -> bool:
    '''
    Registra una compra para un cliente.

    Args:
        compras (dict): Diccionario con las compras.
        cliente_id (int): Identificador del cliente.
        producto (str): Producto comprado.
        cantidad (int): Cantidad comprada.

    Returns:
        bool: True si se registró correctamente.
    '''
    if cliente_id not in compras:
        return False

    compras[cliente_id].append(
        (producto, cantidad)
    )

    return True


def total_productos_cliente(
        compras: dict,
        cliente_id: int
        ) -> int:
    '''
    Calcula la cantidad total de productos comprados.

    Args:
        compras (dict): Diccionario de compras.
        cliente_id (int): Identificador del cliente.

    Returns:
        int: Número total de unidades compradas.
    '''
    if cliente_id not in compras:
        return 0

    total = 0

    for _, cantidad in compras[cliente_id]:
        total += cantidad

    return total


def mostrar_compras(compras: dict) -> None:
    '''
    Muestra todas las compras registradas.
    '''
    for cliente_id, productos in compras.items():

        print(f"\nCliente {cliente_id}")

        if not productos:
            print("No tiene compras.")
            continue

        for producto, cantidad in productos:
            print(
                f"- {producto}: {cantidad} unidades"
            )

        print(
            "Total de unidades:",
            total_productos_cliente(
                compras,
                cliente_id
            )
        )


if __name__ == "__main__":
    compras = {}

    agregar_cliente(compras, 1001)
    agregar_cliente(compras, 1002)

    registrar_compra(
        compras,
        1001,
        "Teclado",
        1
    )

    registrar_compra(
        compras,
        1001,
        "Ratón",
        2
    )

    registrar_compra(
        compras,
        1002,
        "Monitor",
        1
    )

    mostrar_compras(compras)