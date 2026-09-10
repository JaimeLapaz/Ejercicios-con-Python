'''
Enunciado:

27. Registro de Ventas: Crea un programa que registre las ventas
diarias de una tienda utilizando un diccionario. El diccionario debe
contener las fechas como claves y las ventas totales como valores.

Utiliza una lista para almacenar los detalles de cada venta, que
incluyen el producto vendido, la cantidad y el precio unitario.

Solución:
'''


def registrar_venta(
        ventas: dict,
        fecha: str,
        producto: str,
        cantidad: int,
        precio_unitario: float
        ) -> None:
    '''
    Registra una venta en una fecha determinada.

    Args:
        ventas (dict): Diccionario donde se almacenan las ventas.
        fecha (str): Fecha de la venta.
        producto (str): Nombre del producto.
        cantidad (int): Cantidad vendida.
        precio_unitario (float): Precio de una unidad.
    '''
    venta = {
        "producto": producto,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario
    }

    if fecha not in ventas:
        ventas[fecha] = []

    ventas[fecha].append(venta)


def calcular_total_dia(ventas: dict, fecha: str) -> float:
    '''
    Calcula el dinero total vendido en una fecha.

    Args:
        ventas (dict): Diccionario con todas las ventas.
        fecha (str): Fecha que se quiere consultar.

    Returns:
        float: Importe total vendido ese día.
    '''
    if fecha not in ventas:
        return 0.0

    total = 0

    for venta in ventas[fecha]:
        total += venta["cantidad"] * venta["precio_unitario"]

    return total


def mostrar_ventas(ventas: dict) -> None:
    '''
    Muestra todas las ventas agrupadas por fecha.

    Args:
        ventas (dict): Diccionario de ventas.
    '''
    for fecha, lista_ventas in ventas.items():
        print(f"\nFecha: {fecha}")

        for venta in lista_ventas:
            importe = venta["cantidad"] * venta["precio_unitario"]

            print(
                f"- {venta['producto']}: "
                f"{venta['cantidad']} unidades x "
                f"{venta['precio_unitario']:.2f} € "
                f"= {importe:.2f} €"
            )

        print(
            f"Total del día: "
            f"{calcular_total_dia(ventas, fecha):.2f} €"
        )


if __name__ == "__main__":
    ventas = {}

    registrar_venta(
        ventas,
        "10/09/2026",
        "Teclado",
        2,
        29.99
    )

    registrar_venta(
        ventas,
        "10/09/2026",
        "Ratón",
        3,
        15.50
    )

    registrar_venta(
        ventas,
        "11/09/2026",
        "Monitor",
        1,
        199.99
    )

    mostrar_ventas(ventas)