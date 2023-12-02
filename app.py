from functools import wraps
from flask import Flask, jsonify, request
from config import MongoDBConnection
from models.Evento import Evento
from flask_cors import CORS
from controllers.controllerUsuarios import *
from controllers.controllerPago import *
from controllers.controllerSectores import *
from controllers.controllerBoleto import *
from middlewares.auth_middleware import *


app = Flask(__name__)
CORS(app, origins='*')
mongo_connection = MongoDBConnection(
    host="146.190.214.220",
    port=27017,
    username="adminStadium",
    password="adminPassword123",
    database="Stadium"
)
# db = mongo_connection.connect()


@app.route("/api/evento", methods=["GET", "POST", "DELETE", "PUT"])
@app.route("/api/evento/<ev>", methods=["GET"])
def gestionar_evento(ev=None):
    db = mongo_connection.connect()
    try:
        if request.method == 'GET':
            eventos = Evento(db=db)
            if ev is not None:
                eventos_en_db = eventos.mostrarEventoS(ev)
            else:
                eventos_en_db = eventos.mostrarEvento()
            return jsonify(eventos_en_db)

        elif request.method == 'POST':
            data = request.get_json()
            evento = Evento(
                db,
                cod_evento=data['codigoEvento'],
                tipoEvento=data['tipo'],
                nombreEvento=data['nombre'],
                fechaEvento=data['fecha'],
                descripcionEvento=data['descripcion'],
                cod_admin=data['codigoAdmin'],
                hora=data['hora'],
                imgURL=data['imgURL']
            )
            msg, insertedID = evento.crearEvento()
            return jsonify({"msg": msg, "id": str(insertedID)})

        elif request.method == 'DELETE':
            data = request.get_json()
            evento = Evento(db=db)
            deleted_count = evento.borrarEvento(data["codigoEvento"])
            return jsonify({"msg": f"{str(deleted_count)} Elementos Eliminados"})

        elif request.method == 'PUT':
            data = request.get_json()
            evento = Evento(db=db)
            edited_count = evento.editarEvento(
                codigoEvento=data["codigoEvento"], nuevos_valores=data["nuevos_datos"]
            )
            return jsonify({"msg": f"{str(edited_count)} Elementos Editados"})
    finally:
        mongo_connection.disconnect()


# @require_authentication_and_role(True)
@app.route("/api/usuario", methods=["POST", "PUT", "GET", "DELETE"])
@app.route("/api/usuario/<cliente_id>", methods=["GET"])
def handler_cliente(cliente_id=None):
    db = mongo_connection.connect()
    try:
        if request.method == "POST":
            data = request.get_json()
            msg, id = crearUsuario(data, db)
            return jsonify({"msg": msg, "id": str(id)})
            # return crearJWT(jsonify({"msg": msg, "id": str(id)}), datos=data)

        elif request.method == 'PUT':
            data = request.get_json()
            edited_count = editarDatosUsuario(
                data["carnet"], data["nuevos_valores"], db)
            return jsonify({"msg": f"{str(edited_count)} Elementos Editados"})

        elif request.method == 'GET':
            if cliente_id is not None:
                cliente_id = int(cliente_id)
                clientes = mostrarUsuario(cliente_id, db)
            else:
                clientes = mostrarUsuarios(db)
                for cliente in clientes:
                    cliente["password"] = str(cliente["password"])

            return jsonify(clientes)

        elif request.method == 'DELETE':
            data = request.get_json()
            deleted_count = eliminarUsuario(data['carnet'], db)
            return jsonify({"msg": f"{str(deleted_count)} Elementos Eliminados"})
    finally:
        mongo_connection.disconnect()


@app.route('/api/login', methods=["POST"])
def makeLogin():
    db = mongo_connection.connect()
    try:
        data = request.get_json()
        if 'usuario' in data and 'password' in data:
            usuariojson = data['usuario']
            password = data['password'].encode('utf-8')

            usuarios = mostrarUsuarios(db)
            usuario_encontrado = next(
                (usuario for usuario in usuarios if usuario["usuario"] == usuariojson), None)
            print(usuario_encontrado)
            if usuario_encontrado and bcrypt.checkpw(password, usuario_encontrado["password"]):
                # cambiar esto a la función que crea el JWT
                return crearJWT(jsonify({"cod": 1, "msg": "Inicio de sesion exitoso"}), datos=usuario_encontrado)
            else:
                return jsonify({"cod": -1, "mensaje": "Credenciales incorrectas"}), 401
        else:
            return jsonify({"cod": 0, "Error": "Faltan datos en la solicitud"}), 400
    except Exception as e:
        return jsonify({"Error": f"Error en la solicitud: {str(e)}"}), 500
    finally:
        mongo_connection.disconnect()


@app.route("/api/logout")
def logout():
    # Elimina la cookie de sesión
    response = jsonify({'mensaje': 'Cierre de sesión exitoso'})
    response.delete_cookie('session')

    return response


@app.route("/api/pago", methods=["POST"])
def handler_pago():
    db = mongo_connection.connect()
    try:
        if request.method == "POST":
            data = request.get_json()
            msg, id = crearPago(data, db)
            return jsonify({"msg": msg, "id": str(id)})
    finally:
        mongo_connection.disconnect()


@app.route("/api/boleto", methods=["POST"])
def handler_boleto():
    db = mongo_connection.connect()
    try:
        if request.method == "POST":
            data = request.get_json()
            msg, id = crearBoleto(data, db)
            return jsonify({"msg": msg, "id": str(id)})
    finally:
        mongo_connection.disconnect()


@app.route("/api/sector", methods=["POST", "GET", "PUT", "DELETE"])
def handler_sector():
    db = mongo_connection.connect()
    db = mongo_connection.connect()
    try:
        if request.method == "POST":
            data = request.get_json()
            msg, id = crearSector(data, db)
            return jsonify({"msg": msg, "id": str(id)})
            # return crearJWT(jsonify({"msg": msg, "id": str(id)}), datos=data)

        elif request.method == 'PUT':
            data = request.get_json()
            edited_count = editarDatosSector(
                data["codigoSector"], data["nuevos_valores"], db)
            return jsonify({"msg": f"{str(edited_count)} Elementos Editados"})

        elif request.method == 'GET':
            try:
                data = request.get_json()
                clientes = mostrarSectores(db, data)
            except:
                clientes = mostrarSectores(db)
            return jsonify(clientes)

        elif request.method == 'DELETE':
            data = request.get_json()
            deleted_count = eliminarSector(data['codigoSector'], db)
            return jsonify({"msg": f"{str(deleted_count)} Elementos Eliminados"})
    finally:
        mongo_connection.disconnect()


if __name__ == '__main__':
    app.run(debug=True)
