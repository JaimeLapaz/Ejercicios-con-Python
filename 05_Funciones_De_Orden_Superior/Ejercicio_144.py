"""
Enunciado:

144. Validación de Datos: Desarrolla una función de orden superior
que tome una lista de datos y una función de validación, y devuelva
una lista de los datos válidos según esa función.

Solución:
"""

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def validar_datos(
    datos: list[T], es_valido: Callable[[T], bool]
) -> list[T]:
    """Conserva los datos válidos en su orden original."""
    return [dato for dato in datos if es_valido(dato)]


if __name__ == "__main__":
    edades = [17, 22, -3, 35, 0, 18]
    edades_validas = validar_datos(
        edades, lambda edad: 0 <= edad <= 120
    )
    mayores_de_edad = validar_datos(
        edades_validas, lambda edad: edad >= 18
    )

    correos = ["ana@ejemplo.com", "sin-arroba", "luis@ejemplo.es", ""]
    correos_validos = validar_datos(
        correos, lambda correo: correo.count("@") == 1
        and all(correo.split("@"))
    )

    print("Edades válidas:", edades_validas)
    print("Mayores de edad:", mayores_de_edad)
    print("Correos con formato básico:", correos_validos)
    assert edades_validas == [17, 22, 35, 0, 18]
    assert mayores_de_edad == [22, 35, 18]
    assert correos_validos == ["ana@ejemplo.com", "luis@ejemplo.es"]
    assert validar_datos([], lambda dato: True) == []
