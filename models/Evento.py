class Evento:
    def __init__(self, db, cod_evento=None, tipoEvento=None, nombreEvento=None, fechaEvento=None, descripcionEvento=None, cod_admin=None, imgURL=None, hora=None):
        self.codigoEvento = cod_evento
        self.tipo = tipoEvento
        self.nombre = nombreEvento
        self.fecha = fechaEvento
        self.hora = hora
        self.descripcion = descripcionEvento
        self.imgUrl = imgURL
        self.cod_admin = cod_admin
        self.collection = db["Evento"]

    def crearEvento(self):
        if self.verificarExistencia(self.cod_evento):
            return ("El Evento ya Existe", -1)
        else:
            evento = {
                "codigoEvento": self.codigoEvento,
                "tipo": self.tipo,
                "nombre": self.nombre,
                "fecha": self.fecha,
                "descripcion": self.descripcion,
                "codigoAdministrador": self.cod_admin,
                "hora": self.hora,
                "imgURL": self.imgUrl
            }
            result = self.collection.insert_one(evento)
            return ("Creado Existosamente", result.inserted_id)
        # pass

    def editarEvento(self, codigoEvento, nuevos_valores):
        result = self.collection.update_one(
            {"codigoEvento": codigoEvento},
            {"$set": nuevos_valores}
        )
        return result.modified_count

    def borrarEvento(self, cod_evento):
        result = self.collection.delete_one({"codigoEvento": cod_evento})
        return result.deleted_count

    def mostrarEventoS(self, codigoEvento):
        evento_encontrado = self.collection.find_one(
            {"codigoEvento": codigoEvento}, {"_id": 0})
        return evento_encontrado

    def mostrarEvento(self):
        eventos = self.collection.find({}, {"_id": 0})  # Excluye el campo _id
        return list(eventos)

    def verificarExistencia(self, cod_evento):
        evento_encontrado = self.collection.find_one(
            {"codigoEvento": cod_evento})
        return evento_encontrado is not None
