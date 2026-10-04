"""
Enunciado:

162. Cola de Tareas: Crea una cola de tareas pendientes y desarrolla
funciones para agregar nuevas tareas y completarlas.

Solución:
"""


def agregar_tarea(tareas: list[str], tarea: str) -> None:
    """Añade una tarea no vacía al final de la cola."""
    tarea = tarea.strip()
    if not tarea:
        raise ValueError("La tarea no puede estar vacía.")
    tareas.append(tarea)


def completar_tarea(tareas: list[str]) -> str:
    """Completa y devuelve la tarea más antigua."""
    if not tareas:
        raise IndexError("No hay tareas pendientes.")
    return tareas.pop(0)


if __name__ == "__main__":
    pendientes: list[str] = []
    agregar_tarea(pendientes, "Estudiar pilas")
    agregar_tarea(pendientes, "Practicar colas")
    agregar_tarea(pendientes, "Revisar ejercicios")

    completada = completar_tarea(pendientes)
    print("Completada:", completada)
    print("Pendientes:", pendientes)

    assert completada == "Estudiar pilas"
    assert pendientes == ["Practicar colas", "Revisar ejercicios"]
