class Usuario:
    def __init__(self, db, CI=None, nombres=None, apellidos=None, metodoPago=None, usuario=None, password=None, email=None, rol=None):
        self.CI = CI
        self.nombres = nombres
        self.apellidos = apellidos
        self.metodoPago = metodoPago
        self.usuario = usuario
        self.password = password
        self.email = email
        self.rol = rol
        self.collection = db["Usuario"]
