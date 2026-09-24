"""
Enunciado:

103. Diseña un programa que gestione una lista de tareas pendientes
de múltiples usuarios, utilizando un diccionario donde las claves
son los usuarios y los valores son conjuntos de tareas.

Solución:
"""


def agregar_tarea(tareas: dict, usuario: str, tarea: str) -> bool:
    """
    Agrega una tarea pendiente a un usuario.

    Args:
        tareas (dict): Diccionario de usuarios y tareas.
        usuario (str): Nombre del usuario.
        tarea (str): Tarea que se quiere agregar.

    Returns:
        bool: True si se agregó la tarea y False si ya existía.
    """
    if usuario not in tareas:
        tareas[usuario] = set()

    if tarea in tareas[usuario]:
        return False

    tareas[usuario].add(tarea)
    return True


def completar_tarea(tareas: dict, usuario: str, tarea: str) -> bool:
    """
    Elimina una tarea al marcarla como completada.

    Returns:
        bool: True si la tarea existía y se eliminó.
    """
    if usuario not in tareas or tarea not in tareas[usuario]:
        return False

    tareas[usuario].remove(tarea)
    return True


def mostrar_tareas(tareas: dict, usuario: str) -> None:
    """Muestra las tareas pendientes de un usuario."""
    if usuario not in tareas:
        print(f"El usuario {usuario} no está registrado.")
        return

    if not tareas[usuario]:
        print(f"{usuario} no tiene tareas pendientes.")
        return

    print(f"Tareas pendientes de {usuario}:")

    for tarea in sorted(tareas[usuario]):
        print(f"- {tarea}")


if __name__ == "__main__":
    tareas = {}

    agregar_tarea(tareas, "Ana", "Estudiar Python")
    agregar_tarea(tareas, "Ana", "Hacer ejercicio")
    agregar_tarea(tareas, "Carlos", "Comprar alimentos")

    mostrar_tareas(tareas, "Ana")

    print("\nCompletando una tarea...")
    completar_tarea(tareas, "Ana", "Hacer ejercicio")
    mostrar_tareas(tareas, "Ana")
