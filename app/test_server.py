import socket
import struct
import unittest

from model.Server import Server, ServerBuilder
from model.Protocol import Protocol
from Builders.ProtocolBuilder import ProtocolBuilder


class TestServer(unittest.TestCase):

    def test_create_server(self):

        Listener : socket.socket = None
        
        server = Server( host="localhost", port=6000 )
        builder = ServerBuilder(server)
        with builder.create_server() as Listener:
            address = Listener.getsockname()[0]
            port = Listener.getsockname()[1]

            self.assertIsInstance(Listener, socket.socket)
            self.assertEqual(address, "127.0.0.1")
            self.assertEqual(port, 6000)

    def test_connect_with_client(self):

        # Listener : socket.socket = None
        # server = Server( host="localhost", port=5000 )
        # builder = ServerBuilder(server)

        # with builder.create_server() as Listener:
        #     Listener 
        ...

    def test_send_message(self):
        ...

    def test_receive_message(self):
        ...

    def test_is_listening(self):
        ...

    def test_have_clients(self):
        ...

    def test_build_protocol(self):
        # bytes = b"\x02\x01\x01\x00\x00\x03"
        bytes = struct.pack("<bib", 2, 257, 3)
        protocolBuilder = ProtocolBuilder(bytes)
        
        is_protocol = protocolBuilder.Validate()

        self.assertTrue(is_protocol) 

        protocol = protocolBuilder.build()

        self.assertIsInstance(protocol, Protocol)
        print(protocol.data)
        
        ...

    