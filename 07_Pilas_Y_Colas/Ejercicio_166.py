"""
Enunciado:

166. Pila de Expresiones: Desarrolla un programa que evalúe una
expresión matemática en notación polaca inversa (postfija)
utilizando una pila.

Solución:
"""

from collections.abc import Callable

Operacion = Callable[[float, float], float]

OPERACIONES: dict[str, Operacion] = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def evaluar_postfija(expresion: str) -> float:
    """Evalúa una expresión postfija cuyos elementos están separados."""
    pila: list[float] = []

    for token in expresion.split():
        if token not in OPERACIONES:
            try:
                pila.append(float(token))
            except ValueError as error:
                raise ValueError(f"Token no válido: {token}") from error
            continue

        if len(pila) < 2:
            raise ValueError("La expresión postfija no es válida.")
        segundo = pila.pop()
        primero = pila.pop()
        pila.append(OPERACIONES[token](primero, segundo))

    if len(pila) != 1:
        raise ValueError("La expresión postfija no es válida.")
    return pila[0]


if __name__ == "__main__":
    resultado = evaluar_postfija("5 1 2 + 4 * + 3 -")
    print("Resultado:", resultado)
    assert resultado == 14.0
    assert evaluar_postfija("8 2 / 3 +") == 7.0

    try:
        evaluar_postfija("2 +")
    except ValueError as error:
        print("Expresión incorrecta:", error)
