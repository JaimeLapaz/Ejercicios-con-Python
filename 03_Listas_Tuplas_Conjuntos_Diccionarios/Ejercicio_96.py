"""
Enunciado:

96. Desarrolla una función que encuentre el empleado con el
salario más alto en una lista de empleados (diccionarios)
y muestre su información.

Solución:
"""


def empleado_mayor_salario(empleados: list):
    """
    Encuentra el empleado con el salario más alto.

    Args:
        empleados (list): Lista de empleados.

    Returns:
        dict | None: Empleado con mayor salario o None
        si la lista está vacía.
    """
    if not empleados:
        return None

    empleado_mayor = empleados[0]

    for empleado in empleados[1:]:
        if empleado["salario"] > empleado_mayor["salario"]:
            empleado_mayor = empleado

    return empleado_mayor


def mostrar_empleado(empleado: dict) -> None:
    """
    Muestra la información de un empleado.

    Args:
        empleado (dict): Diccionario del empleado.
    """
    print(f"Nombre: {empleado['nombre']}")

    print(f"Puesto: {empleado['puesto']}")

    print(f"Salario: {empleado['salario']:.2f} €")


if __name__ == "__main__":
    empleados = [
        {"nombre": "Ana", "puesto": "Desarrolladora", "salario": 28000},
        {"nombre": "Carlos", "puesto": "Diseñador", "salario": 24000},
        {"nombre": "Laura", "puesto": "Analista", "salario": 32000},
        {"nombre": "Miguel", "puesto": "Administrador", "salario": 30000},
    ]

    resultado = empleado_mayor_salario(empleados)

    if resultado is not None:
        print("Empleado con mayor salario:")
        mostrar_empleado(resultado)
    else:
        print("No hay empleados registrados.")
