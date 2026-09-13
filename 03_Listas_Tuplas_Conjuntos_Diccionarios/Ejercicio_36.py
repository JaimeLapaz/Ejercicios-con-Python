'''
Enunciado:

36. Registro de Pedidos: Crea un sistema de registro de pedidos
para un restaurante.

Utiliza un diccionario que almacene detalles de pedidos donde cada
pedido tiene un número de pedido único, una lista de elementos del
pedido (almacenados como tuplas de nombre del plato y cantidad),
y un estado (pendiente, entregado, etc.).

Solución:
'''


def crear_pedido(
        pedidos: dict,
        numero_pedido: int
        ) -> bool:
    '''
    Crea un nuevo pedido.

    Args:
        pedidos (dict): Diccionario donde se guardan los pedidos.
        numero_pedido (int): Número único del pedido.

    Returns:
        bool: True si se creó, False si ya existía.
    '''
    if numero_pedido in pedidos:
        return False

    pedidos[numero_pedido] = {
        "elementos": [],
        "estado": "pendiente"
    }

    return True


def agregar_elemento(
        pedidos: dict,
        numero_pedido: int,
        plato: str,
        cantidad: int
        ) -> bool:
    '''
    Añade un plato a un pedido.

    Args:
        pedidos (dict): Diccionario de pedidos.
        numero_pedido (int): Número del pedido.
        plato (str): Nombre del plato.
        cantidad (int): Cantidad solicitada.

    Returns:
        bool: True si se añadió correctamente.
    '''
    if numero_pedido not in pedidos:
        return False

    if cantidad <= 0:
        return False

    pedidos[numero_pedido]["elementos"].append(
        (plato, cantidad)
    )

    return True


def cambiar_estado(
        pedidos: dict,
        numero_pedido: int,
        nuevo_estado: str
        ) -> bool:
    '''
    Cambia el estado de un pedido.

    Args:
        pedidos (dict): Diccionario de pedidos.
        numero_pedido (int): Número del pedido.
        nuevo_estado (str): Nuevo estado.

    Returns:
        bool: True si el cambio fue correcto.
    '''
    estados_validos = {
        "pendiente",
        "preparando",
        "listo",
        "entregado"
    }

    if numero_pedido not in pedidos:
        return False

    if nuevo_estado not in estados_validos:
        return False

    pedidos[numero_pedido]["estado"] = nuevo_estado

    return True


def mostrar_pedido(
        pedidos: dict,
        numero_pedido: int
        ) -> None:
    '''
    Muestra toda la información de un pedido.
    '''
    if numero_pedido not in pedidos:
        print("El pedido no existe.")
        return

    pedido = pedidos[numero_pedido]

    print(f"\nPedido nº {numero_pedido}")
    print(f"Estado: {pedido['estado']}")
    print("Elementos:")

    if not pedido["elementos"]:
        print("- El pedido está vacío.")
        return

    for plato, cantidad in pedido["elementos"]:
        print(f"- {plato}: {cantidad}")


if __name__ == "__main__":
    pedidos = {}

    crear_pedido(pedidos, 101)

    agregar_elemento(
        pedidos,
        101,
        "Hamburguesa",
        2
    )

    agregar_elemento(
        pedidos,
        101,
        "Patatas fritas",
        1
    )

    agregar_elemento(
        pedidos,
        101,
        "Agua",
        2
    )

    cambiar_estado(
        pedidos,
        101,
        "preparando"
    )

    mostrar_pedido(
        pedidos,
        101
    )