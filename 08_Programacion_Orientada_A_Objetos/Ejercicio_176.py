"""
Enunciado:

176. Clase Contacto: Crea una clase Contacto con nombre y dos datos de
comunicacion, con metodos para mostrar y modificar su informacion.

Solucion:
"""


class Contacto:
    """Representa la informacion editable de un contacto."""

    def __init__(self, nombre: str, correo: str, telefono: str) -> None:
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def mostrar_informacion(self) -> tuple[str, str, str]:
        """Devuelve una copia inmutable de los datos actuales."""
        return self.nombre, self.correo, self.telefono

    def modificar_informacion(
        self,
        nombre: str | None = None,
        correo: str | None = None,
        telefono: str | None = None,
    ) -> None:
        """Actualiza solo los campos indicados."""
        if nombre is not None:
            self.nombre = nombre
        if correo is not None:
            self.correo = correo
        if telefono is not None:
            self.telefono = telefono


if __name__ == "__main__":
    contacto = Contacto("Ejemplo", "correo-1", "telefono-1")
    assert contacto.mostrar_informacion() == (
        "Ejemplo", "correo-1", "telefono-1"
    )
    contacto.modificar_informacion(telefono="telefono-2")
    print(contacto.mostrar_informacion())
    assert contacto.telefono == "telefono-2"
