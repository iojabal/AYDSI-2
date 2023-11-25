import os
import sys


try:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
    sys.path.insert(0, parent_dir)
    from models.Pago import Pago
except:
    print("error")


def crearPago(pago, db):
    pg = Pago(db=db)

    pagoJson = {
        "codigoPago": pg.generar_codigo_pago(),
        "monto": pago["monto"],
        "fecha": pago["fecha"],
        "metodoPago": pago["metodoPago"]
    }

    result = pg.collection.insert_one(pagoJson)
    return ("Creado Existosamente", result.inserted_id)


def verificarExistencia(ci, db):
    cl = Pago(db=db)
    evento_encontrado = cl.collection.find_one(
        {"codigoPago": ci})
    return evento_encontrado is not None
