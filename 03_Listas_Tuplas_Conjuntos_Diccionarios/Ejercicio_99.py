"""
Enunciado:

99. Diseña un programa que organice una lista de estudiantes
(diccionarios) en función de sus calificaciones, almacenadas
como una tupla.

Solución:
"""


def calcular_promedio(calificaciones: tuple) -> float:
    """
    Calcula el promedio de una tupla de calificaciones.

    Args:
        calificaciones (tuple): Calificaciones del estudiante.

    Returns:
        float: Promedio de las calificaciones.
    """
    if not calificaciones:
        return 0

    total = 0

    for calificacion in calificaciones:
        total += calificacion

    return total / len(calificaciones)


def ordenar_estudiantes(estudiantes: list) -> list:
    """
    Ordena los estudiantes de mayor a menor promedio.

    Args:
        estudiantes (list): Lista de estudiantes.

    Returns:
        list: Nueva lista ordenada por promedio.
    """
    resultado = estudiantes.copy()

    resultado.sort(
        key=lambda estudiante: calcular_promedio(estudiante["calificaciones"]),
        reverse=True,
    )

    return resultado


def mostrar_estudiantes(estudiantes: list) -> None:
    """
    Muestra los estudiantes y sus promedios.
    """
    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["calificaciones"])

        print(f"{estudiante['nombre']}: {promedio:.2f}")


if __name__ == "__main__":
    estudiantes = [
        {"nombre": "Ana", "calificaciones": (8.5, 9.0, 7.5)},
        {"nombre": "Carlos", "calificaciones": (6.0, 7.0, 6.5)},
        {"nombre": "Laura", "calificaciones": (9.5, 9.0, 10.0)},
        {"nombre": "Miguel", "calificaciones": (7.5, 8.0, 8.5)},
    ]

    ordenados = ordenar_estudiantes(estudiantes)

    print("Estudiantes ordenados por calificación:")

    mostrar_estudiantes(ordenados)
