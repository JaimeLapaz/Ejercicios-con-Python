"""
Enunciado:

118. Longitud de una cadena: Crea una función que calcule la longitud de una cadena
después de validar que sea una cadena de texto válida.

Solución:
"""

def longitud_cadena(texto: str) -> int:
    """Valida una cadena y devuelve su longitud."""
    if not isinstance(texto, str):
        raise TypeError("El valor debe ser una cadena de texto.")
    return len(texto)


if __name__ == "__main__":
    ejemplos = ["Python", "", "Validación de datos"]
    for ejemplo in ejemplos:
        print(f"{ejemplo!r} tiene {longitud_cadena(ejemplo)} caracteres.")
