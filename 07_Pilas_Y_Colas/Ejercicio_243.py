"""
Enunciado:

243. Pila de Tareas Recursivas: Crea una pila para gestionar llamadas
     recursivas en un programa y evitar desbordamiento de la pila de llamadas.

Solución:
Un intérprete iterativo de tareas simula la recursión con marcos explícitos.
Se ilustra con Fibonacci: los marcos pendientes se guardan en una lista,
sin depender de la profundidad de llamadas de Python.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Marco:
    """Llamada pendiente a Fibonacci y fase de ejecución."""
    n: int
    fase: int = 0
    izquierdo: int = 0


def fibonacci_con_pila(n: int) -> int:
    """Calcula Fibonacci(n) mediante una pila explícita de marcos.

    El espacio máximo de la pila es O(n), sin recursión de Python.
    """
    if type(n) is not int or n < 0:
        raise ValueError("n debe ser un entero no negativo")
    pila = [Marco(n)]
    resultado = 0
    while pila:
        marco = pila[-1]
        if marco.n < 2:
            resultado = marco.n
            pila.pop()
        elif marco.fase == 0:
            marco.fase = 1
            pila.append(Marco(marco.n - 1))
            continue
        elif marco.fase == 1:
            marco.izquierdo = resultado
            marco.fase = 2
            pila.append(Marco(marco.n - 2))
            continue
        else:
            resultado = marco.izquierdo + resultado
            pila.pop()
    return resultado


def factorial_con_pila(n: int) -> int:
    """Ejemplo adicional: producto de marcos pendientes, sin recursión."""
    if type(n) is not int or n < 0:
        raise ValueError("n debe ser un entero no negativo")
    pila = list(range(2, n + 1))
    resultado = 1
    while pila:
        resultado *= pila.pop()
    return resultado


if __name__ == "__main__":
    assert [fibonacci_con_pila(n) for n in range(11)] == [
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
    ]
    assert fibonacci_con_pila(25) == 75025
    assert factorial_con_pila(0) == 1
    assert factorial_con_pila(6) == 720
    assert len(str(factorial_con_pila(1000))) > 2000
    for funcion in (fibonacci_con_pila, factorial_con_pila):
        try:
            funcion(-1)
        except ValueError:
            pass
        else:
            raise AssertionError("Se esperaba ValueError")
    print("Ejercicio 243: pruebas superadas")
