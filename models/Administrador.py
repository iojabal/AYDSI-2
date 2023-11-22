class Administrador:
    def __init__(self, db, nombres=None, apellidos=None, email=None, password=None, usuario=None):
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.password = password
        # agregado mio
        self.usuario = usuario
        self.collection = db["Administrador"]
