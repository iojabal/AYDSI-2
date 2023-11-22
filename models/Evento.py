class Evento:
    def __init__(self, db, cod_evento=None, tipoEvento=None, nombreEvento=None, fechaEvento=None, descripcionEvento=None, cod_admin=None, imgURL=None):
        self.cod_evento = cod_evento
        self.tipoEvento = tipoEvento
        self.nombreEvento = nombreEvento
        self.fechaEvento = fechaEvento
        self.descripcionEvento = descripcionEvento
        self.cod_admin = cod_admin
        self.imgUrl = imgURL
        self.collection = db["Evento"]

    def crearEvento(self):
        if self.verificarExistencia(self.cod_evento):
            return ("El Evento ya Existe", -1)
        else:
            evento = {
                "cod_evento": self.cod_evento,
                "tipoEvento": self.tipoEvento,
                "nombreEvento": self.nombreEvento,
                "fechaEvento": self.fechaEvento,
                "descripcionEvento": self.descripcionEvento,
                "cod_admin": self.cod_admin,
                "imgURL": self.imgUrl
            }
            result = self.collection.insert_one(evento)
            return ("Creado Existosamente", result.inserted_id)
        # pass

    def editarEvento(self, cod_evento, nuevos_valores):
        result = self.collection.update_one(
            {"cod_evento": cod_evento},
            {"$set": nuevos_valores}
        )
        return result.modified_count

    def borrarEvento(self, cod_evento):
        result = self.collection.delete_one({"cod_evento": cod_evento})
        return result.deleted_count

    def mostrarEventoS(self, cod_evento):
        evento_encontrado = self.collection.find_one(
            {"cod_evento": cod_evento}, {"_id": 0})
        return evento_encontrado

    def mostrarEvento(self):
        eventos = self.collection.find({}, {"_id": 0})  # Excluye el campo _id
        return list(eventos)

    def verificarExistencia(self, cod_evento):
        evento_encontrado = self.collection.find_one(
            {"cod_evento": cod_evento})
        return evento_encontrado is not None
