"""
Enunciado:

161. Pila de Palabras: Escribe un programa que verifique si una
palabra es un palíndromo utilizando una pila para comparar
caracteres.

Solución:
"""


def es_palindromo(palabra: str) -> bool:
    """Comprueba un palíndromo desapilando sus caracteres."""
    normalizada = palabra.casefold()
    pila = list(normalizada)
    invertida = "".join(pila.pop() for _ in range(len(pila)))
    return normalizada == invertida


if __name__ == "__main__":
    ejemplos = ["reconocer", "Radar", "python"]

    for palabra in ejemplos:
        print(f"{palabra}: {es_palindromo(palabra)}")

    assert es_palindromo("reconocer")
    assert es_palindromo("Radar")
    assert not es_palindromo("python")
