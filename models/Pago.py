class Pago:
    def __init__(self, db, codigo_pago=None, Precio=None, fecha_pago=None, metodoPago=None):
        self.codigoPago = codigo_pago
        self.monto = Precio
        self.fecha = fecha_pago
        self.metodoPago = metodoPago

        self.collection = db["pago"]

    def generar_codigo_pago(self):
        ultimo_pago = self.collection.find_one(sort=[("codigoPago", -1)])

        if ultimo_pago is not None and "codigoPago" in ultimo_pago:
            ultimo_codigo = ultimo_pago["codigoPago"]
            # Extraer el número del código de usuario y sumar 1
            numero_codigo = int(ultimo_codigo[1:])
            nuevo_numero_codigo = numero_codigo + 1

            # Generar el nuevo código de usuario con el formato deseado
            nuevo_codigo_usuario = f"P{nuevo_numero_codigo:02d}"
            return nuevo_codigo_usuario
        else:
            # Si no hay usuarios en la base de datos, generar un código predeterminado
            return "P01"
