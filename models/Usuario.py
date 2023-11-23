class Usuario:
    def __init__(self, db, codigoUsuario=None, CI=None, nombres=None, apellidos=None, metodoPago=None, usuario=None, password=None, email=None, rol=None):
        self.codigoUsuario = codigoUsuario
        self.CI = CI
        self.nombres = nombres
        self.apellidos = apellidos
        self.usuario = usuario
        self.password = password
        self.email = email

        self.collection = db["Usuario"]

    def generar_codigo_usuario(self):
        ultimo_usuario = self.collection.find_one(sort=[("codigoUsuario", -1)])

        if ultimo_usuario is not None and "codigoUsuario" in ultimo_usuario:
            ultimo_codigo = ultimo_usuario["codigoUsuario"]
            # Extraer el número del código de usuario y sumar 1
            numero_codigo = int(ultimo_codigo[1:])
            nuevo_numero_codigo = numero_codigo + 1

            # Generar el nuevo código de usuario con el formato deseado
            nuevo_codigo_usuario = f"U{nuevo_numero_codigo:02d}"
            return nuevo_codigo_usuario
        else:
            # Si no hay usuarios en la base de datos, generar un código predeterminado
            return "U01"
