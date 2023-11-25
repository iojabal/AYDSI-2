import os
import sys


try:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
    sys.path.insert(0, parent_dir)
    from models.Boleto import Boleto
except:
    print("error")


def crearBoleto(bol, db):
    pg = Boleto(db=db)

    boleto = {
        "codigoBoleto": pg.generar_codigo_pago(),
        "numeroIngresos": bol["numeroIngresos"],
        "codigoSector": bol["codigoSector"],
        "codigoEvento": bol["codigoEvento"],
        "codigoPago": bol["codigoPago"],
        "codigoUsuario": bol["codigoUsuario"]
    }

    result = pg.collection.insert_one(boleto)
    return ("Creado Existosamente", result.inserted_id)


def verificarExistencia(ci, db):
    cl = Boleto(db=db)
    evento_encontrado = cl.collection.find_one(
        {"codigoPago": ci})
    return evento_encontrado is not None
