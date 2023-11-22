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
    from app import handler_cliente
except:
    print("error")


class TestGestionarEvento(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.add_url_rule('/api/cliente', 'handler_cliente',
                              handler_cliente, methods=["GET", "POST", "DELETE", "PUT"])
        self.client = self.app.test_client()

    @patch("app.mongo_connection.connect")
    @patch("app.mongo_connection.disconnect")
    def test_get_eventos(self, mock_connect, mock_disconnect):
        response = self.client.get("/api/cliente")
        self.assertEqual(response.status_code, 200)

    @patch("app.mongo_connection.connect")
    @patch("app.mongo_connection.disconnect")
    def test_post_eventos(self, mock_connect, mock_disconnect):
        data = {
            "ci": 1234,
            "nombre": "Mario Hugo",
            "apellidos": "Martinez fernandez",
            "metodoPago": "Tarjeta",
            "usuario": "MHugo",
            "password": "12345A@",
            "email": "test@test.com"
        }
        headers = {"Content-Type": "application/json"}
        response = self.client.post('/api/cliente', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)

    @patch("app.mongo_connection.connect")
    @patch("app.mongo_connection.disconnect")
    def test_delete_evento(self, mock_connect, mock_disconnect):
        data = {"ci": 1234}
        headers = {"Content-Type": "application/json"}

        response = self.client.delete(
            '/api/cliente', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)

    @patch("app.mongo_connection.connect")
    @patch("app.mongo_connection.disconnect")
    def test_put_evento(self, mock_connect, mock_disconnect):
        data = {
            "ci": 1234,
            "nuevos_valores": {
                "usuario": "MHugo2",
                "password": "12345A@"
            }
        }
        headers = {"Content-Type": "application/json"}

        response = self.client.put("/api/cliente", json=data, headers=headers)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
