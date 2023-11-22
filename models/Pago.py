class Pago:
    def __init__(self, codigo_pago, Precio, fecha_pago):
        self.codigo_pago = codigo_pago
        self.Precio = Precio
        self.fecha_pago = fecha_pago

    def AlmacenarPago(self):

        pass

    def ObtenerPrecio(self):
        return self.Precio
