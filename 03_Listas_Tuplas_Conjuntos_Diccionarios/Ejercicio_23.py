'''
Enunciado:

23. Diccionario de Contactos: Crea un diccionario de contactos
con nombres y números de teléfono.

Solución:
'''


def agregar_contacto(contactos: dict, nombre: str, telefono: str) -> None:
    '''
    Agrega o actualiza un contacto.

    Args:
        contactos (dict): Diccionario de contactos.
        nombre (str): Nombre del contacto.
        telefono (str): Número de teléfono.
    '''
    contactos[nombre] = telefono


def buscar_contacto(contactos: dict, nombre: str) -> str:
    '''
    Busca el teléfono de un contacto.

    Args:
        contactos (dict): Diccionario de contactos.
        nombre (str): Nombre que queremos buscar.

    Returns:
        str: Número de teléfono o mensaje de error.
    '''
    if nombre in contactos:
        return contactos[nombre]

    return f"No existe ningún contacto llamado '{nombre}'."


if __name__ == "__main__":
    contactos = {
        "Ana": "612345678",
        "Luis": "623456789",
        "Marta": "634567890"
    }

    agregar_contacto(contactos, "Carlos", "645678901")

    print(contactos)

    print("Teléfono de Ana:", buscar_contacto(contactos, "Ana"))
    print(buscar_contacto(contactos, "Pedro"))