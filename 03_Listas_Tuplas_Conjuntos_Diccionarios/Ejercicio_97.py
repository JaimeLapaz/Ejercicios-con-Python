"""
Enunciado:

97. Escribe un programa que gestione un diccionario de productos,
donde cada producto tiene un nombre y una lista de revisiones de
usuarios, almacenadas como diccionarios con comentarios y
calificaciones.

Solución:
"""


def agregar_producto(productos: dict, identificador: str, nombre: str) -> bool:
    """
    Agrega un producto al diccionario.

    Args:
        productos (dict): Diccionario de productos.
        identificador (str): Identificador único del producto.
        nombre (str): Nombre del producto.

    Returns:
        bool: True si se agregó y False si ya existía.
    """
    if identificador in productos:
        return False

    productos[identificador] = {"nombre": nombre, "revisiones": []}

    return True


def agregar_revision(
    productos: dict, identificador: str, comentario: str, calificacion: int
) -> bool:
    """
    Agrega una revisión a un producto.

    Args:
        productos (dict): Diccionario de productos.
        identificador (str): Identificador del producto.
        comentario (str): Comentario del usuario.
        calificacion (int): Calificación entre 1 y 5.

    Returns:
        bool: True si la revisión se agregó correctamente.
    """
    if identificador not in productos:
        return False

    if calificacion < 1 or calificacion > 5:
        return False

    revision = {"comentario": comentario, "calificacion": calificacion}

    productos[identificador]["revisiones"].append(revision)

    return True


def calcular_calificacion_media(producto: dict) -> float:
    """
    Calcula la calificación media de un producto.

    Args:
        producto (dict): Diccionario del producto.

    Returns:
        float: Calificación media o 0 si no hay revisiones.
    """
    revisiones = producto["revisiones"]

    if not revisiones:
        return 0

    total = 0

    for revision in revisiones:
        total += revision["calificacion"]

    return total / len(revisiones)


def mostrar_producto(productos: dict, identificador: str) -> None:
    """
    Muestra un producto y todas sus revisiones.
    """
    if identificador not in productos:
        print("El producto no existe.")
        return

    producto = productos[identificador]

    print(f"\nProducto: {producto['nombre']}")

    if not producto["revisiones"]:
        print("No tiene revisiones.")
        return

    print("Revisiones:")

    for revision in producto["revisiones"]:
        print(f"- {revision['calificacion']}/5: {revision['comentario']}")

    promedio = calcular_calificacion_media(producto)

    print(f"Calificación media: {promedio:.2f}/5")


if __name__ == "__main__":
    productos = {}

    agregar_producto(productos, "P001", "Teclado mecánico")

    agregar_revision(productos, "P001", "Muy cómodo para programar.", 5)

    agregar_revision(productos, "P001", "Buen teclado, aunque algo ruidoso.", 4)

    mostrar_producto(productos, "P001")
