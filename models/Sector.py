class Sector:
    def __init__(self, Codigo_sector, Nombre_sector, Cantidad_asientos, cantidadOcupantes, precioSector, habilitado, posicionDefecto, codigoEvento):
        self.codigoSector = Codigo_sector
        self.Nombre = Nombre_sector
        self.capacidadMaxima = Cantidad_asientos
        self.cantidadOcupantes = cantidadOcupantes
        self.precioSector = precioSector
        self.comprasMaximas = 0
        self.codigoEvento = codigoEvento
        self.habilitado = habilitado
        self.posicionDefecto = posicionDefecto

    def marcarOcupado(self):
        pass

    def marcarDesocupado(self):
        pass
