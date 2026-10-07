"""
Enunciado:

177. Clase Agenda: Implementa una clase Agenda que almacene contactos
y permita buscarlos por nombre.

Solucion:
"""


class Contacto:
    """Representa un contacto identificado por su nombre."""

    def __init__(self, nombre: str, dato: str) -> None:
        self.nombre = nombre
        self.dato = dato


class Agenda:
    """Almacena contactos y permite consultarlos por nombre."""

    def __init__(self) -> None:
        self.contactos: list[Contacto] = []

    def agregar_contacto(self, contacto: Contacto) -> None:
        """Agrega un contacto a la agenda."""
        self.contactos.append(contacto)

    def buscar_por_nombre(self, nombre: str) -> list[Contacto]:
        """Busca coincidencias exactas sin distinguir mayusculas."""
        buscado = nombre.casefold()
        return [
            contacto
            for contacto in self.contactos
            if contacto.nombre.casefold() == buscado
        ]


if __name__ == "__main__":
    agenda = Agenda()
    agenda.agregar_contacto(Contacto("Ana", "dato-a"))
    agenda.agregar_contacto(Contacto("Luis", "dato-b"))
    encontrados = agenda.buscar_por_nombre("ana")
    print([contacto.nombre for contacto in encontrados])
    assert len(encontrados) == 1
    assert encontrados[0].dato == "dato-a"
    assert agenda.buscar_por_nombre("Marta") == []
