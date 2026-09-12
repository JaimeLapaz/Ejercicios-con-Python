'''
Enunciado:

33. Directorio Telefónico: Crea un directorio telefónico que almacene
contactos como un diccionario donde las claves son nombres y los valores
son tuplas con números de teléfono y direcciones de correo electrónico.

Solución:
'''


def agregar_contacto(
        directorio: dict,
        nombre: str,
        telefono: str,
        email: str
        ) -> bool:
    '''
    Agrega un nuevo contacto al directorio.

    Args:
        directorio (dict): Diccionario de contactos.
        nombre (str): Nombre del contacto.
        telefono (str): Número de teléfono.
        email (str): Correo electrónico.

    Returns:
        bool: True si se añadió y False si ya existía.
    '''
    if nombre in directorio:
        return False

    directorio[nombre] = (telefono, email)

    return True


def buscar_contacto(
        directorio: dict,
        nombre: str
        ):
    '''
    Busca un contacto por nombre.

    Args:
        directorio (dict): Diccionario de contactos.
        nombre (str): Nombre del contacto.

    Returns:
        tuple | None: Teléfono y email del contacto.
    '''
    return directorio.get(nombre)


def mostrar_contactos(directorio: dict) -> None:
    '''
    Muestra todos los contactos del directorio.
    '''
    for nombre, datos in directorio.items():
        telefono, email = datos

        print(f"\nNombre: {nombre}")
        print(f"Teléfono: {telefono}")
        print(f"Email: {email}")


if __name__ == "__main__":
    directorio = {}

    agregar_contacto(
        directorio,
        "Ana",
        "612345678",
        "ana@email.com"
    )

    agregar_contacto(
        directorio,
        "Carlos",
        "623456789",
        "carlos@email.com"
    )

    mostrar_contactos(directorio)

    contacto = buscar_contacto(
        directorio,
        "Ana"
    )

    if contacto:
        telefono, email = contacto
        print(
            f"\nAna -> {telefono} | {email}"
        )