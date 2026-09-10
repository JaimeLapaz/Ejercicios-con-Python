'''
Enunciado:

29. Diccionario de Estudiantes: Crea un diccionario que almacene
información sobre estudiantes, donde cada estudiante tiene un nombre,
una lista de cursos en los que está inscrito y una tupla con sus
calificaciones para cada curso.

Solución:
'''


def agregar_estudiante(
        estudiantes: dict,
        identificador: int,
        nombre: str
        ) -> None:
    '''
    Añade un estudiante al diccionario.

    Args:
        estudiantes (dict): Diccionario de estudiantes.
        identificador (int): Identificador único del estudiante.
        nombre (str): Nombre del estudiante.
    '''
    estudiantes[identificador] = {
        "nombre": nombre,
        "cursos": [],
        "calificaciones": ()
    }


def agregar_curso(
        estudiantes: dict,
        identificador: int,
        curso: str,
        calificacion: float
        ) -> bool:
    '''
    Añade un curso y su calificación a un estudiante.

    Args:
        estudiantes (dict): Diccionario de estudiantes.
        identificador (int): Identificador del estudiante.
        curso (str): Nombre del curso.
        calificacion (float): Nota del curso.

    Returns:
        bool: True si se añadió correctamente.
    '''
    if identificador not in estudiantes:
        return False

    estudiantes[identificador]["cursos"].append(curso)

    estudiantes[identificador]["calificaciones"] += (
        calificacion,
    )

    return True


def calcular_promedio(
        estudiantes: dict,
        identificador: int
        ):
    '''
    Calcula el promedio de un estudiante.

    Args:
        estudiantes (dict): Diccionario de estudiantes.
        identificador (int): Identificador del estudiante.

    Returns:
        float | None: Promedio o None si no existen calificaciones.
    '''
    if identificador not in estudiantes:
        return None

    calificaciones = estudiantes[identificador]["calificaciones"]

    if not calificaciones:
        return None

    return sum(calificaciones) / len(calificaciones)


def mostrar_estudiante(
        estudiantes: dict,
        identificador: int
        ) -> None:
    '''
    Muestra toda la información de un estudiante.

    Args:
        estudiantes (dict): Diccionario de estudiantes.
        identificador (int): Identificador del estudiante.
    '''
    if identificador not in estudiantes:
        print("El estudiante no existe.")
        return

    estudiante = estudiantes[identificador]

    print(f"\nNombre: {estudiante['nombre']}")

    print("Cursos:")

    for curso, nota in zip(
            estudiante["cursos"],
            estudiante["calificaciones"]
            ):
        print(f"- {curso}: {nota}")

    promedio = calcular_promedio(
        estudiantes,
        identificador
    )

    if promedio is not None:
        print(f"Promedio: {promedio:.2f}")


if __name__ == "__main__":
    estudiantes = {}

    agregar_estudiante(
        estudiantes,
        1,
        "Jaime"
    )

    agregar_estudiante(
        estudiantes,
        2,
        "Laura"
    )

    agregar_curso(
        estudiantes,
        1,
        "Python",
        9
    )

    agregar_curso(
        estudiantes,
        1,
        "Bases de Datos",
        8
    )

    agregar_curso(
        estudiantes,
        1,
        "Git",
        10
    )

    agregar_curso(
        estudiantes,
        2,
        "Python",
        7.5
    )

    mostrar_estudiante(estudiantes, 1)
    mostrar_estudiante(estudiantes, 2)