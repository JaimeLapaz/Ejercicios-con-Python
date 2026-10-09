"""
Enunciado:

187. Clase Juego de Cartas: Diseña una clase JuegoDeCartas para un
juego de cartas simple con métodos para barajar, repartir y jugar cartas.

Solución:
"""

from dataclasses import dataclass
from random import shuffle


@dataclass(frozen=True)
class Carta:
    """Representa una carta de la baraja francesa."""

    valor: str
    palo: str


class JuegoDeCartas:
    """Gestiona un mazo de 52 cartas, manos y descartes."""

    def __init__(self) -> None:
        valores = (
            "A", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "J", "Q", "K",
        )
        palos = ("corazones", "diamantes", "tréboles", "picas")
        self.mazo: list[Carta] = [
            Carta(valor, palo) for palo in palos for valor in valores
        ]
        self.manos: dict[str, list[Carta]] = {}
        self.descartes: list[Carta] = []

    def barajar(self) -> None:
        """Mezcla las cartas que aún están en el mazo."""
        shuffle(self.mazo)

    def repartir(self, jugador: str, cantidad: int) -> list[Carta]:
        """Reparte cartas a un jugador y devuelve una copia de su mano."""
        if not jugador.strip() or cantidad <= 0:
            raise ValueError("Indica un jugador y una cantidad positiva.")
        if cantidad > len(self.mazo):
            raise ValueError("No quedan suficientes cartas en el mazo.")
        mano = self.manos.setdefault(jugador, [])
        for _ in range(cantidad):
            mano.append(self.mazo.pop())
        return mano.copy()

    def jugar_carta(self, jugador: str) -> Carta:
        """Juega la última carta de la mano y la deja en descartes."""
        mano = self.manos.get(jugador)
        if not mano:
            raise ValueError("El jugador no tiene cartas para jugar.")
        carta = mano.pop()
        self.descartes.append(carta)
        return carta


if __name__ == "__main__":
    juego = JuegoDeCartas()
    assert len(juego.mazo) == 52
    juego.barajar()
    mano_ana = juego.repartir("Ana", 5)
    mano_luis = juego.repartir("Luis", 5)
    assert len(set(mano_ana + mano_luis)) == 10
    assert len(juego.mazo) == 42

    jugada = juego.jugar_carta("Ana")
    print("Ana juega:", jugada)
    assert jugada in mano_ana
    assert len(juego.manos["Ana"]) == 4
    assert juego.descartes == [jugada]

    try:
        juego.repartir("Ana", 43)
    except ValueError as error:
        print("Reparto rechazado:", error)
    else:
        raise AssertionError("No se pueden repartir más cartas que las disponibles.")
