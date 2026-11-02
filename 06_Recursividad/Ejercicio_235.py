"""
Enunciado:

235. Fractal: Desarrolla una función recursiva para dibujar un fractal,
    como el conjunto de Mandelbrot.

Solución:
"""

from __future__ import annotations


def triangulo_sierpinski(nivel: int, caracter: str = "*") -> str:
    """Dibuja recursivamente el triángulo fractal de Sierpinski en texto.

    El caso base es un único carácter. Cada nivel coloca una copia del
    triángulo anterior arriba y dos copias debajo, separadas por un
    espacio. Así se generan huecos triangulares a todas las escalas.

    Se admite nivel entre 0 y 9 para evitar salidas demasiado grandes:
    el dibujo tiene 2**nivel filas y 2**(nivel + 1) - 1 columnas.
    Tiempo y memoria O(4**nivel), proporcionales al tamaño del dibujo.
    """
    if not isinstance(nivel, int) or isinstance(nivel, bool):
        raise TypeError("El nivel debe ser un entero")
    if not 0 <= nivel <= 9:
        raise ValueError("El nivel debe estar entre 0 y 9")
    if not isinstance(caracter, str) or len(caracter) != 1 or caracter.isspace():
        raise ValueError("El carácter debe ser un símbolo visible de longitud 1")

    def construir(profundidad: int) -> list[str]:
        if profundidad == 0:
            return [caracter]
        anterior = construir(profundidad - 1)
        margen = " " * (len(anterior[0]) // 2 + 1)
        parte_superior = [margen + fila + margen for fila in anterior]
        parte_inferior = [fila + " " + fila for fila in anterior]
        return parte_superior + parte_inferior

    return "\n".join(construir(nivel))


if __name__ == "__main__":
    assert triangulo_sierpinski(0) == "*"
    assert triangulo_sierpinski(1) == " * \n* *"
    assert triangulo_sierpinski(2) == (
        "   *   \n"
        "  * *  \n"
        " *   * \n"
        "* * * *"
    )
    assert triangulo_sierpinski(1, "#") == " # \n# #"

    for nivel in range(7):
        filas = triangulo_sierpinski(nivel).splitlines()
        assert len(filas) == 2**nivel
        assert all(len(fila) == 2 ** (nivel + 1) - 1 for fila in filas)
        assert sum(fila.count("*") for fila in filas) == 3**nivel

    for invalido in (True, 1.5, "2"):
        try:
            triangulo_sierpinski(invalido)
        except TypeError:
            pass
        else:
            raise AssertionError("Se esperaba TypeError")
    for invalido in (-1, 10):
        try:
            triangulo_sierpinski(invalido)
        except ValueError:
            pass
        else:
            raise AssertionError("Se esperaba ValueError")
    for invalido in ("", "ab", " ", "\n"):
        try:
            triangulo_sierpinski(2, invalido)
        except ValueError:
            pass
        else:
            raise AssertionError("Se esperaba ValueError")

    print("Ejercicio 235: pruebas superadas")
    print(triangulo_sierpinski(3))
