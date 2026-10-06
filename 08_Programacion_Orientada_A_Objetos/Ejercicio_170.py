"""
Enunciado:

170. Clase Libro: Diseña una clase Libro con atributos como título, autor y
género, y métodos para mostrar la información del libro.

Solución:
"""


class Libro:
    """Representa un libro mediante sus principales datos bibliográficos."""

    def __init__(self, titulo: str, autor: str, genero: str) -> None:
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    def mostrar_informacion(self) -> str:
        """Devuelve la información del libro en una sola línea."""
        return (
            f'"{self.titulo}", de {self.autor} '
            f"(género: {self.genero})."
        )


if __name__ == "__main__":
    libro = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela")
    informacion = libro.mostrar_informacion()
    print(informacion)
    assert "Cien años de soledad" in informacion
    assert "Gabriel García Márquez" in informacion
