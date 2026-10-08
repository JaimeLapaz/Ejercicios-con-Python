"""
Enunciado:

182. Clase Música: Implementa una clase Musica con atributos como título,
artista y género, y métodos para reproducir y pausar la música.

Solución:
"""


class Musica:
    """Representa una canción y su estado de reproducción."""

    def __init__(self, titulo: str, artista: str, genero: str) -> None:
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.esta_reproduciendo = False

    def reproducir(self) -> None:
        """Marca la canción como en reproducción."""
        self.esta_reproduciendo = True

    def pausar(self) -> None:
        """Pausa la canción, si se estaba reproduciendo."""
        self.esta_reproduciendo = False


if __name__ == "__main__":
    cancion = Musica("Imagine", "John Lennon", "Rock")
    assert not cancion.esta_reproduciendo
    cancion.reproducir()
    print(f"Reproduciendo: {cancion.titulo} - {cancion.artista}")
    assert cancion.esta_reproduciendo
    cancion.pausar()
    assert not cancion.esta_reproduciendo
    cancion.pausar()  # Pausar dos veces no causa errores.
    assert not cancion.esta_reproduciendo
    cancion.reproducir()
    assert cancion.esta_reproduciendo
