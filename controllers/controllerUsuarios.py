import os
import sys


try:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
    sys.path.insert(0, parent_dir)
    from models.Usuario import Usuario
    from middlewares.auth_middleware import encrpytPassword
except:
    print("error")


def crearUsuario(usuario, db):
    cl = Usuario(db=db)
    if verificarExistencia(usuario["carnet"], db=db):
        return ("El usuario ya existe", -1)
    usuario = {
        "codigoUsuario": cl.generar_codigo_usuario(),
        "carnet": usuario["carnet"],
        "nombre": usuario["nombre"],
        "apellido": usuario["apellido"],
        "usuario": usuario["usuario"],
        "password": encrpytPassword(usuario["password"]),
        "email": usuario["email"]
    }
    result = cl.collection.insert_one(usuario)
    return ("Creado Exitosamente", result.inserted_id)


def eliminarUsuario(ci_Usuario, db):
    cl = Usuario(db=db)
    result = cl.collection.delete_one({"carnet": ci_Usuario})
    return result.deleted_count


def editarDatosUsuario(ci_Usuario, datos_nuevos, db):
    cl = Usuario(db=db)
    result = cl.collection.update_one(
        {"carnet": ci_Usuario}, {"$set": datos_nuevos})
    return result.modified_count


def mostrarUsuario(cod_Usuario, db):
    cl = Usuario(db)
    usuario = cl.collection.find_one({"carnet": cod_Usuario}, {"_id": 0})
    usuario["password"] = str(usuario["password"])
    return usuario


def mostrarUsuarios(db):
    cl = Usuario(db)
    usuarios = cl.collection.find({}, {"_id": 0})
    return list(usuarios)


def verificarExistencia(ci, db):
    cl = Usuario(db=db)
    evento_encontrado = cl.collection.find_one(
        {"carnet": ci})
    return evento_encontrado is not None
