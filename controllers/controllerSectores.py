import os
import sys


try:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
    sys.path.insert(0, parent_dir)
    from models.Sector import Sector
except:
    print("error")


def crearSector(sc, db):
    sc = Sector(db=db)

    sector = {
        "codigoSector": sc["codigoSector"],
        "Nombre": sc["Nombre"],
        "capacidadMaxima": sc["capacidadMaxima"],
        "cantidadOcupantes": sc["cantidadOcupantes"],
        "precioSector": sc["precioSector"],
        "comprasMaximas": sc["comprasMaximas"],
        "codigoEvento": sc["codigoEvento"],
        "habilitado": sc["habilitado"],
        "posicionDefecto": sc["posicionDefecto"]
    }
    result = sc.collection.insert_one(sector)
    return ("Creado Exitosamente", result.inserted_id)


def eliminarSector(codSec, db):
    sc = Sector(db=db)
    result = sc.collection.delete_one({"codigoSector": codSec})
    return result.deleted_count


def editarDatosSector(csec, datos_nuevos, db):
    sc = Sector(db=db)
    result = sc.collection.update_one(
        {"codigoSector": csec}, {"$set": datos_nuevos})
    return result.modified_count


def mostrarSectores(db, filtro=None):
    query = {}

    if filtro and isinstance(filtro, dict):
        if "codigoSector" in filtro:
            query["codigoSector"] = filtro["codigoSector"]

        if "Nombre" in filtro:
            query["Nombre"] = filtro["Nombre"]

        if "codigoEvento" in filtro:
            query["codigoEvento"] = filtro["codigoEvento"]

    sc = Sector(db)
    sectores = sc.collection.find(query, {"_id": 0})
    return list(sectores)


def verificarExistencia(ci, db):
    cl = Sector(db=db)
    evento_encontrado = cl.collection.find_one(
        {"codigoSector": ci})
    return evento_encontrado is not None
