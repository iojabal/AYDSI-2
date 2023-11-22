
import unittest
import os
import sys
from flask import Flask
from flask.testing import FlaskClient
from unittest.mock import patch

try:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
    sys.path.insert(0, parent_dir)
    from app import gestionar_evento
except:
    print("error")


class TestGestionarEvento(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/api/evento', 'gestionar_evento',
                              gestionar_evento,  methods=["GET", "POST", "DELETE", "PUT"])
        self.client = self.app.test_client()

    @patch("app.mongo_connection.connect")
    @patch("app.mongo_connection.disconnect")
    def test_get_eventos(self, mock_connect, mock_disconnect):

        response = self.client.get("/api/evento")
        self.assertEqual(response.status_code, 200)

    @patch("app.mongo_connection.connect")
    @patch("app.mongo_connection.disconnect")
    def test_post_eventos(self, mock_connect, mock_disconenct):
        data = {
            "cod_evento": "Ev03",
            "tipoEvento": "tstr3",
            "nombreEvento": "234",
            "fechaEvento": "2023-1g4-05",
            "descripcionEvento": "tgdast",
            "imgURL": "https://google.com/",
            "cod_admin": "01"
        }
        headers = {"Content-Type": "Application/json"}
        response = self.client.post('/api/evento', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)

    @patch("app.mongo_connection.connect")
    @patch("app.mongo_connection.disconnect")
    def test_delete_evento(self, mock_connect, mock_disconnect):
        data = {"cod_evento": "Ev03"}
        headers = {"Content-Type": "Application/json"}

        response = self.client.delete(
            '/api/evento', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)

    @patch("app.mongo_connection.connect")
    @patch("app.mongo_connection.disconnect")
    def test_put_evento(self, mock_connect, mock_disconnect):
        data = {
            "cod_evento": "Ev02",
            "nuevos_datos": {
                "nombreEvento": "test2",
                "fechaEvento": "2021-05-01",
                "imgURL": "https:?//eadfdasfdasfafdasf"
            }
        }
        headers = {"Content-Type": "Application/json"}

        response = self.client.put("/api/evento", json=data, headers=headers)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':

    unittest.main()
