"""
Enunciado:

173. Clase Banco: Implementa una clase Banco con una lista de cuentas y
metodos para agregar elementos y calcular la suma de sus saldos.

Solucion:
"""


class Cuenta:
    """Guarda un nombre descriptivo y un saldo numerico."""

    def __init__(self, nombre: str, saldo: float = 0.0) -> None:
        self.nombre = nombre
        self.saldo = saldo


class Banco:
    """Agrupa cuentas y permite consultar el saldo total."""

    def __init__(self) -> None:
        self.cuentas: list[Cuenta] = []

    def agregar_cuenta(self, cuenta: Cuenta) -> None:
        """Agrega una cuenta a la coleccion."""
        self.cuentas.append(cuenta)

    def calcular_saldo_total(self) -> float:
        """Suma los saldos de todas las cuentas."""
        return sum(cuenta.saldo for cuenta in self.cuentas)


if __name__ == "__main__":
    banco = Banco()
    banco.agregar_cuenta(Cuenta("A", 10.0))
    banco.agregar_cuenta(Cuenta("B", 15.0))
    print("Saldo total:", banco.calcular_saldo_total())
    assert banco.calcular_saldo_total() == 25.0
