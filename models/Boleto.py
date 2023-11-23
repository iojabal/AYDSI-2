class Boleto:
    def __init__(self, codigoBoleto, numeroIngresos, codigoSector, codigoEvento, codigoPago, CIUsuario):
        self.codigoBoleto = codigoBoleto
        self.numeroIngresos = numeroIngresos
        self.codigoSector = codigoSector
        self.codigoEvento = codigoEvento
        self.codigoPago = codigoPago
        self.CIUsuario = CIUsuario

    def obtener_precio(self):
        return self.precio

    def cambiarClaseBoleto(self, nueva_clase):
        self.clase_boleto = nueva_clase

    def cambiarNroAsiento(self, nuevo_numero):
        self.Numero_asiento = nuevo_numero

    def pagarBoleto(self):
        pass
