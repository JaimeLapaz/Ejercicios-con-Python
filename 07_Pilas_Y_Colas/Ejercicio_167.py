"""
Enunciado:

167. Simulación de Colas: Escribe una simulación simple de una cola
de autobuses que llegan y parten en intervalos de tiempo.

Solución:
"""

from collections import deque


def simular_autobuses(
    duracion: int, intervalo_llegada: int, intervalo_salida: int
) -> list[str]:
    """Simula llegadas y salidas y devuelve el registro de eventos."""
    if duracion < 0 or intervalo_llegada <= 0 or intervalo_salida <= 0:
        raise ValueError("La duración no puede ser negativa y los intervalos deben ser positivos.")

    cola: deque[str] = deque()
    eventos: list[str] = []
    numero_autobus = 1

    for minuto in range(duracion + 1):
        if minuto % intervalo_llegada == 0:
            autobus = f"Autobús {numero_autobus}"
            numero_autobus += 1
            cola.append(autobus)
            eventos.append(f"{minuto}: llega {autobus}")

        if minuto > 0 and minuto % intervalo_salida == 0 and cola:
            autobus = cola.popleft()
            eventos.append(f"{minuto}: parte {autobus}")

    return eventos


if __name__ == "__main__":
    eventos = simular_autobuses(12, intervalo_llegada=3, intervalo_salida=4)
    for evento in eventos:
        print(evento)

    assert eventos[0] == "0: llega Autobús 1"
    assert "4: parte Autobús 1" in eventos
    assert "12: llega Autobús 5" in eventos
    assert "12: parte Autobús 3" in eventos
