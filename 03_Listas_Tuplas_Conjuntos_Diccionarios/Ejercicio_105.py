"""
Enunciado:

105. Crea un programa que administre una lista de invitados a un
evento, utilizando un diccionario para rastrear la asistencia
mediante un conjunto.

Solución:
"""


def crear_evento(eventos: dict, nombre: str) -> bool:
    """
    Crea un evento con un conjunto vacío de asistentes.

    Returns:
        bool: True si se creó y False si ya existía.
    """
    if nombre in eventos:
        return False

    eventos[nombre] = set()
    return True


def registrar_asistencia(eventos: dict, evento: str, invitado: str) -> bool:
    """
    Registra la asistencia de un invitado.

    Returns:
        bool: True si se registró y False si no fue posible.
    """
    if evento not in eventos:
        return False

    if invitado in eventos[evento]:
        return False

    eventos[evento].add(invitado)
    return True


def cancelar_asistencia(eventos: dict, evento: str, invitado: str) -> bool:
    """Elimina a un invitado del conjunto de asistentes."""
    if evento not in eventos or invitado not in eventos[evento]:
        return False

    eventos[evento].remove(invitado)
    return True


def mostrar_asistentes(eventos: dict, evento: str) -> None:
    """Muestra los asistentes confirmados de un evento."""
    if evento not in eventos:
        print("El evento no existe.")
        return

    asistentes = eventos[evento]

    print(f"Evento: {evento}")
    print(f"Asistentes confirmados: {len(asistentes)}")

    for invitado in sorted(asistentes):
        print(f"- {invitado}")


if __name__ == "__main__":
    eventos = {}

    crear_evento(eventos, "Encuentro Python")

    registrar_asistencia(eventos, "Encuentro Python", "Ana")
    registrar_asistencia(eventos, "Encuentro Python", "Carlos")
    registrar_asistencia(eventos, "Encuentro Python", "Laura")

    mostrar_asistentes(eventos, "Encuentro Python")

    print("\nCarlos cancela su asistencia:")
    cancelar_asistencia(eventos, "Encuentro Python", "Carlos")
    mostrar_asistentes(eventos, "Encuentro Python")
