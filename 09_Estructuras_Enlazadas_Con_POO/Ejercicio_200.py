"""
Enunciado:

200. Evaluación de Expresiones: Crea una clase EvaluadorExpresiones que
utilice una pila para evaluar expresiones matemáticas en notación postfija.

Solución:
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Nodo:
    valor: float
    siguiente: Nodo | None = None


class Pila:
    """Pila LIFO implementada mediante nodos enlazados."""

    def __init__(self) -> None:
        self._cima: Nodo | None = None

    def apilar(self, valor: float) -> None:
        self._cima = Nodo(valor, self._cima)

    def desapilar(self) -> float:
        if self._cima is None:
            raise ValueError("Faltan operandos")
        valor = self._cima.valor
        self._cima = self._cima.siguiente
        return valor

    def vacia(self) -> bool:
        return self._cima is None


class EvaluadorExpresiones:
    """Evalúa expresiones postfijas separadas por espacios."""

    def evaluar(self, expresion: str) -> float:
        pila = Pila()
        if not expresion.strip():
            raise ValueError("La expresión está vacía")
        operaciones = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        for token in expresion.split():
            if token in operaciones:
                segundo = pila.desapilar()
                primero = pila.desapilar()
                pila.apilar(operaciones[token](primero, segundo))
            else:
                try:
                    pila.apilar(float(token))
                except ValueError as exc:
                    raise ValueError(f"Token inválido: {token}") from exc
        resultado = pila.desapilar()
        if not pila.vacia():
            raise ValueError("Sobran operandos")
        return resultado


if __name__ == "__main__":
    evaluador = EvaluadorExpresiones()
    assert evaluador.evaluar("3 4 + 2 *") == 14
    assert evaluador.evaluar("10 2 / 3 -") == 2
    try:
        evaluador.evaluar("1 2")
    except ValueError:
        pass
    else:
        raise AssertionError("Debe rechazar operandos sobrantes")
    print("Pruebas superadas")
