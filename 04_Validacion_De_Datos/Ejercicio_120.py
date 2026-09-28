"""
Enunciado:

120. Potencia de un número: Escribe una función que calcule la potencia de un número
después de validar que tanto la base como el exponente sean números reales.

Solución:
"""

def potencia(base: float, exponente: float) -> float:
    """Valida dos números reales y devuelve base elevada al exponente."""
    if isinstance(base, bool) or not isinstance(base, (int, float)):
        raise TypeError("La base debe ser un número real.")
    if isinstance(exponente, bool) or not isinstance(exponente, (int, float)):
        raise TypeError("El exponente debe ser un número real.")

    return base ** exponente


if __name__ == "__main__":
    ejemplos = [(2, 3), (9, 0.5), (5, -2)]
    for base, exponente in ejemplos:
        print(f"{base} ** {exponente} = {potencia(base, exponente)}")
