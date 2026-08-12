class SaldoInsuficienteError(Exception):
    """Se lanza cuando se intenta retirar más dinero del disponible."""

    def __init__(self, saldo, cantidad):
        self.saldo = saldo
        self.cantidad = cantidad
        self.deficit = cantidad - saldo

        mensaje = (
            f"No hay suficiente saldo. "
            f"Saldo: {saldo}, Cantidad solicitada: {cantidad}"
        )

        super().__init__(mensaje)


class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo


def retirar(cuenta, cantidad):
    if cantidad > cuenta.saldo:
        raise SaldoInsuficienteError(cuenta.saldo, cantidad)

    cuenta.saldo -= cantidad
    return cuenta.saldo


cuenta = Cuenta(100000)

try:
    saldo_actual = retirar(cuenta, 150000)
    print(f"Saldo restante: {saldo_actual}")

except SaldoInsuficienteError as error:
    print(f"Error: {error}")