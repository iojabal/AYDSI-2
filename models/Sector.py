class Sector:
    def __init__(self, Codigo_sector, Nombre_sector, Cantidad_asientos):
        self.Codigo_sector = Codigo_sector
        self.Nombre_sector = Nombre_sector
        self.Cantidad_asientos = Cantidad_asientos
        self.precioSector = 0
        self.habilitado = False
        self.posicion = None
        self.CodigoEvento = None

    def marcarOcupado(self):
        pass

    def marcarDesocupado(self):

        pass
