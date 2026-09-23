"""
Enunciado:

100. Crea una función que tome una lista de direcciones de correo
electrónico y divida las válidas de las inválidas en dos listas
separadas.

Solución:
"""


def es_correo_valido(correo: str) -> bool:
    """
    Comprueba de forma sencilla si una dirección de correo es válida.

    Args:
        correo (str): Dirección que queremos comprobar.

    Returns:
        bool: True si cumple las reglas básicas y False en caso contrario.
    """
    if correo.count("@") != 1:
        return False

    usuario, dominio = correo.split("@")

    if not usuario or not dominio:
        return False

    if "." not in dominio:
        return False

    if dominio.startswith(".") or dominio.endswith("."):
        return False

    return True


def separar_correos(correos: list) -> tuple:
    """
    Separa una lista de correos en válidos e inválidos.

    Args:
        correos (list): Lista de direcciones de correo electrónico.

    Returns:
        tuple: Dos listas: correos válidos y correos inválidos.
    """
    validos = []
    invalidos = []

    for correo in correos:
        if es_correo_valido(correo):
            validos.append(correo)
        else:
            invalidos.append(correo)

    return validos, invalidos


if __name__ == "__main__":
    correos = [
        "ana@email.com",
        "correo-invalido",
        "carlos@empresa.es",
        "@dominio.com",
        "laura@dominio",
        "miguel@mail.org",
    ]

    validos, invalidos = separar_correos(correos)

    print("Correos válidos:")
    print(validos)

    print("\nCorreos inválidos:")
    print(invalidos)
