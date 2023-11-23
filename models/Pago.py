class Pago:
    def __init__(self, codigo_pago, Precio, fecha_pago):
        self.codigoPago = codigo_pago
        self.monto = Precio
        self.fecha = fecha_pago
        self.metodoPago = ""

    def AlmacenarPago(self):
        pass

    def ObtenerPrecio(self):
        return self.Precio
