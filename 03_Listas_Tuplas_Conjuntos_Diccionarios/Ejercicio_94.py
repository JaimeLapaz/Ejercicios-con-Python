"""
Enunciado:

94. Implementa una función que reciba una lista de empleados
(diccionarios) y calcule el salario promedio.

Solución:
"""


def calcular_salario_promedio(empleados: list) -> float:
    """
    Calcula el salario promedio de una lista de empleados.

    Args:
        empleados (list): Lista de diccionarios con empleados.

    Returns:
        float: Salario promedio. Devuelve 0 si la lista está vacía.
    """
    if not empleados:
        return 0

    total_salarios = 0

    for empleado in empleados:
        total_salarios += empleado["salario"]

    return total_salarios / len(empleados)


if __name__ == "__main__":
    empleados = [
        {"nombre": "Ana", "puesto": "Desarrolladora", "salario": 28000},
        {"nombre": "Carlos", "puesto": "Diseñador", "salario": 24000},
        {"nombre": "Laura", "puesto": "Analista", "salario": 32000},
    ]

    promedio = calcular_salario_promedio(empleados)

    print(f"Salario promedio: {promedio:.2f} €")
