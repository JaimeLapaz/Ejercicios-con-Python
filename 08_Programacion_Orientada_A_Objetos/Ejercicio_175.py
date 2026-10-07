"""
Enunciado:

175. Clase Película: Desarrolla una clase Pelicula con atributos como
título, director y año, y métodos para agregar y listar actores.

Solución:
"""


class Pelicula:
    """Representa una película y su reparto."""

    def __init__(self, titulo: str, director: str, anio: int) -> None:
        if anio <= 0:
            raise ValueError("El año debe ser un entero positivo.")
        self.titulo = titulo
        self.director = director
        self.anio = anio
        self._actores: list[str] = []

    def agregar_actor(self, actor: str) -> None:
        """Añade un actor al reparto si todavía no figura en él."""
        if actor not in self._actores:
            self._actores.append(actor)

    def listar_actores(self) -> list[str]:
        """Devuelve una copia de la lista de actores."""
        return self._actores.copy()


if __name__ == "__main__":
    pelicula = Pelicula("Origen", "Christopher Nolan", 2010)
    pelicula.agregar_actor("Leonardo DiCaprio")
    pelicula.agregar_actor("Joseph Gordon-Levitt")
    pelicula.agregar_actor("Leonardo DiCaprio")
    print(pelicula.listar_actores())
    assert pelicula.listar_actores() == [
        "Leonardo DiCaprio", "Joseph Gordon-Levitt"
    ]
