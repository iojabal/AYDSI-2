import jwt
import datetime
import bcrypt

from flask import jsonify, request, abort

secret_key = "T3st1ng456"


def crearJWT(response, datos):

    duracion_validez_token = datetime.timedelta(hours=1)
    fecha_expiracion = datetime.datetime.utcnow() + duracion_validez_token

    token_payload = {"codUsuario": datos['codigoUsuario'], "carnet": datos['carnet'],
                     'usuario': datos['usuario'], 'exp': fecha_expiracion}

    token = jwt.encode(token_payload, secret_key, algorithm='HS256')

    response_json = response.get_json()
    response_json.update({'token': token})

    response.set_data(jsonify(response_json).data)
    response.set_cookie("session", token)
    return response


def encrpytPassword(password):
    salt = bcrypt.gensalt()
    contrasena_encriptada = bcrypt.hashpw(
        password=password.encode('utf-8'), salt=salt)
    return contrasena_encriptada


def checkuserAuthenticationRol(rol_requerido):
    jwt_token = request.cookies.get('session')
    if jwt_token is not None:
        try:
            decoded_token = jwt.decode(
                jwt_token, secret_key, algorithms='HS256')

            if 'rol' in decoded_token and decoded_token['rol'] == rol_requerido:
                return True

        except jwt.ExpiredSignatureError:
            abort(403, description="Acceso denegado. El rol requerido no coincide.")
        except jwt.InvalidTokenError:
            abort(403, description="Acceso denegado. El rol requerido no coincide.")

    abort(403, description="Acceso denegado. El rol requerido no coincide.")
