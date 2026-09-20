"""
Enunciado:

93. Crea un programa que gestione una lista de usuarios, donde
cada usuario es un diccionario con nombre, correo electrónico y
una lista de pedidos realizados (almacenados como diccionarios
con detalles de productos).

Solución:
"""


def agregar_usuario(usuarios: list, nombre: str, correo: str) -> bool:
    """
    Agrega un nuevo usuario.

    Args:
        usuarios (list): Lista de usuarios.
        nombre (str): Nombre del usuario.
        correo (str): Correo electrónico.

    Returns:
        bool: True si se agregó y False si el correo ya existe.
    """
    if buscar_usuario(usuarios, correo) is not None:
        return False

    usuario = {"nombre": nombre, "correo": correo, "pedidos": []}

    usuarios.append(usuario)

    return True


def buscar_usuario(usuarios: list, correo: str):
    """
    Busca un usuario mediante su correo electrónico.

    Args:
        usuarios (list): Lista de usuarios.
        correo (str): Correo que queremos buscar.

    Returns:
        dict | None: Usuario encontrado o None.
    """
    for usuario in usuarios:
        if usuario["correo"] == correo:
            return usuario

    return None


def agregar_pedido(
    usuarios: list, correo: str, producto: str, cantidad: int, precio_unitario: float
) -> bool:
    """
    Agrega un pedido al usuario indicado.

    Args:
        usuarios (list): Lista de usuarios.
        correo (str): Correo del usuario.
        producto (str): Producto comprado.
        cantidad (int): Cantidad comprada.
        precio_unitario (float): Precio de una unidad.

    Returns:
        bool: True si el pedido se agregó correctamente.
    """
    usuario = buscar_usuario(usuarios, correo)

    if usuario is None:
        return False

    if cantidad <= 0 or precio_unitario < 0:
        return False

    pedido = {
        "producto": producto,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
    }

    usuario["pedidos"].append(pedido)

    return True


def calcular_total_pedidos(usuario: dict) -> float:
    """
    Calcula el importe total de los pedidos de un usuario.

    Args:
        usuario (dict): Diccionario del usuario.

    Returns:
        float: Importe total de sus pedidos.
    """
    total = 0

    for pedido in usuario["pedidos"]:
        total += pedido["cantidad"] * pedido["precio_unitario"]

    return total


def mostrar_usuario(usuario: dict) -> None:
    """
    Muestra la información y pedidos de un usuario.

    Args:
        usuario (dict): Usuario que queremos mostrar.
    """
    print(f"\nNombre: {usuario['nombre']}")
    print(f"Correo: {usuario['correo']}")
    print("Pedidos:")

    if not usuario["pedidos"]:
        print("- No tiene pedidos.")
        return

    for pedido in usuario["pedidos"]:
        subtotal = pedido["cantidad"] * pedido["precio_unitario"]

        print(
            f"- {pedido['producto']}: "
            f"{pedido['cantidad']} x "
            f"{pedido['precio_unitario']:.2f} € "
            f"= {subtotal:.2f} €"
        )

    print("Total:", f"{calcular_total_pedidos(usuario):.2f} €")


def mostrar_usuarios(usuarios: list) -> None:
    """
    Muestra todos los usuarios registrados.

    Args:
        usuarios (list): Lista de usuarios.
    """
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    for usuario in usuarios:
        mostrar_usuario(usuario)


if __name__ == "__main__":
    usuarios = []

    agregar_usuario(usuarios, "Ana", "ana@email.com")

    agregar_usuario(usuarios, "Carlos", "carlos@email.com")

    agregar_pedido(usuarios, "ana@email.com", "Teclado", 1, 29.99)

    agregar_pedido(usuarios, "ana@email.com", "Ratón", 2, 15.50)

    agregar_pedido(usuarios, "carlos@email.com", "Monitor", 1, 199.99)

    mostrar_usuarios(usuarios)
