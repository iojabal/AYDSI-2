class Boleto:
    def __init__(self, precio, clase_boleto, Numero_asiento, palco, evento):
        self.precio = precio
        self.clase_boleto = clase_boleto
        self.Numero_asiento = Numero_asiento
        self.palco = palco
        self.evento = evento

    def obtener_precio(self):
        return self.precio

    def cambiarClaseBoleto(self, nueva_clase):
        self.clase_boleto = nueva_clase

    def cambiarNroAsiento(self, nuevo_numero):
        self.Numero_asiento = nuevo_numero

    def pagarBoleto(self):
        pass
