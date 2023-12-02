class Sector:
    def __init__(self, db, Codigo_sector=None, Nombre_sector=None, Cantidad_asientos=None, cantidadOcupantes=None, precioSector=None, habilitado=None, posicionDefecto=None, codigoEvento=None):
        self.codigoSector = Codigo_sector
        self.Nombre = Nombre_sector
        self.capacidadMaxima = Cantidad_asientos
        self.cantidadOcupantes = cantidadOcupantes
        self.precioSector = precioSector
        self.comprasMaximas = 0
        self.codigoEvento = codigoEvento
        self.habilitado = habilitado
        self.posicionDefecto = posicionDefecto

        self.collection = db["Sector"]

    def marcarOcupado(self):
        pass

    def marcarDesocupado(self):
        pass
