"""
Enunciado:

155. Número Palindrómico: Crea una función recursiva que verifique
si una cadena de texto es un palíndromo.

Solución:
"""


def es_palindromo(texto: str) -> bool:
    """Comprueba recursivamente si el texto se lee igual al revés."""
    normalizado = "".join(
        caracter.casefold() for caracter in texto if caracter.isalnum()
    )

    def comprobar(inicio: int, fin: int) -> bool:
        if inicio >= fin:
            return True
        if normalizado[inicio] != normalizado[fin]:
            return False
        return comprobar(inicio + 1, fin - 1)

    return comprobar(0, len(normalizado) - 1)


if __name__ == "__main__":
    ejemplos = [
        ("reconocer", True),
        ("Anita lava la tina", True),
        ("Python", False),
        ("", True),
    ]

    for texto, esperado in ejemplos:
        resultado = es_palindromo(texto)
        print(f"{texto!r}: {resultado}")
        assert resultado is esperado
