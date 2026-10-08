"""
Enunciado:

180. Clase Banco con Transferencias: Extiende la clase Banco para
permitir transferencias entre cuentas bancarias.

Solución:
"""

from math import isfinite

from Ejercicio_173 import Banco, Cuenta


class BancoConTransferencias(Banco):
    """Amplía Banco con transferencias entre cuentas registradas."""

    def transferir(self, origen: Cuenta, destino: Cuenta, cantidad: float) -> None:
        """Mueve fondos tras validar cuentas, importe y saldo disponible."""
        if not isfinite(cantidad) or cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva y finita.")
        if origen is destino:
            raise ValueError("Las cuentas de origen y destino deben ser distintas.")
        if not any(cuenta is origen for cuenta in self.cuentas):
            raise ValueError("La cuenta de origen no pertenece al banco.")
        if not any(cuenta is destino for cuenta in self.cuentas):
            raise ValueError("La cuenta de destino no pertenece al banco.")
        if not isfinite(origen.saldo) or not isfinite(destino.saldo):
            raise ValueError("Los saldos deben ser finitos.")
        if origen.saldo < cantidad:
            raise ValueError("Saldo insuficiente para la transferencia.")
        saldo_destino = destino.saldo + cantidad
        if not isfinite(saldo_destino):
            raise ValueError("El saldo de destino resultante no es finito.")

        origen.saldo -= cantidad
        destino.saldo = saldo_destino


if __name__ == "__main__":
    banco = BancoConTransferencias()
    cuenta_ana = Cuenta("Ana", 100.0)
    cuenta_luis = Cuenta("Luis", 25.0)
    banco.agregar_cuenta(cuenta_ana)
    banco.agregar_cuenta(cuenta_luis)

    banco.transferir(cuenta_ana, cuenta_luis, 40.0)
    print("Saldos:", cuenta_ana.saldo, cuenta_luis.saldo)
    assert cuenta_ana.saldo == 60.0
    assert cuenta_luis.saldo == 65.0
    assert banco.calcular_saldo_total() == 125.0

    try:
        banco.transferir(cuenta_ana, cuenta_luis, 100.0)
    except ValueError as error:
        print("Transferencia rechazada:", error)
    else:
        raise AssertionError("No se debe permitir un saldo insuficiente.")
    assert (cuenta_ana.saldo, cuenta_luis.saldo) == (60.0, 65.0)

    for origen, destino, cantidad in [
        (cuenta_ana, cuenta_ana, 10.0),
        (cuenta_ana, Cuenta("Desconocida"), 10.0),
        (cuenta_ana, cuenta_luis, -1.0),
    ]:
        try:
            banco.transferir(origen, destino, cantidad)
        except ValueError:
            pass
        else:
            raise AssertionError("La transferencia inválida debe rechazarse.")
    assert (cuenta_ana.saldo, cuenta_luis.saldo) == (60.0, 65.0)
