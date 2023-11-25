class Boleto:
    def __init__(self, db, codigoBoleto=None, numeroIngresos=None, codigoSector=None, codigoEvento=None, codigoPago=None, CIUsuario=None):
        self.codigoBoleto = codigoBoleto
        self.numeroIngresos = numeroIngresos
        self.codigoSector = codigoSector
        self.codigoEvento = codigoEvento
        self.codigoPago = codigoPago
        self.codigoUsuario = CIUsuario

        self.collection = db["boleto"]

    def generar_codigo_boleto(self):
        ultimo_boleto = self.collection.find_one(sort=[("codigoBoleto", -1)])

        if ultimo_boleto is not None and "codigoBoleto" in ultimo_boleto:
            ultimo_codigo = ultimo_boleto["codigoBoleto"]
            # Extraer el número del código de usuario y sumar 1
            numero_codigo = int(ultimo_codigo[1:])
            nuevo_numero_codigo = numero_codigo + 1

            # Generar el nuevo código de usuario con el formato deseado
            nuevo_codigo_usuario = f"B{nuevo_numero_codigo:02d}"
            return nuevo_codigo_usuario
        else:
            # Si no hay usuarios en la base de datos, generar un código predeterminado
            return "B01"
