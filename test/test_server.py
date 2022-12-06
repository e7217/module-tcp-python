import socket
import unittest
from src import Server

class TestServer(unittest.TestCase):

    def test_create_server(self):
        with Server.create_server() as Listener:
            address = Listener.getsockname()[0]
            port = Listener.getsockname()[1]

            self.assertIsInstance(Listener, socket.socket)
            self.assertEqual(address, "127.0.0.1")
            self.assertEqual(port, 5000)

