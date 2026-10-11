"""
Enunciado:

193. Validación de Paréntesis: Desarrolla un método en la clase Pila
    para validar si una cadena de texto tiene paréntesis balanceados.

Solución:
"""

from __future__ import annotations

from typing import TypeVar

from Ejercicio_192 import Pila as PilaBase

T = TypeVar("T")


class Pila(PilaBase[T]):
    """Amplía la pila enlazada con validación de paréntesis."""

    @staticmethod
    def validar_parentesis(texto: str) -> bool:
        """Comprueba el balance de '(' y ')'; ignora otros caracteres.

        Tiempo O(n) y espacio O(n) en el peor caso.
        """
        pendientes = PilaBase[str]()
        for caracter in texto:
            if caracter == "(":
                pendientes.apilar(caracter)
            elif caracter == ")":
                if pendientes.esta_vacia():
                    return False
                pendientes.desapilar()
        return pendientes.esta_vacia()


if __name__ == "__main__":
    casos = {
        "": True,
        "sin paréntesis": True,
        "(a + b) * (c - d)": True,
        "((1 + 2) * (3 + 4))": True,
        "(())()": True,
        "(a + b": False,
        "a + b)": False,
        ") (": False,
        "(()))": False,
    }
    for expresion, esperado in casos.items():
        resultado = Pila.validar_parentesis(expresion)
        assert resultado is esperado, expresion
        print(f"{expresion!r}: {resultado}")

    pila = Pila[int]()
    pila.apilar(5)
    assert pila.validar_parentesis("(x)")
    assert pila.desapilar() == 5  # La validación no modifica la pila receptora.
