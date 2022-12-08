import socket
import time
from threading import Thread, active_count

from model.Client import Client

class Server:

    host :str = ""
    port :int = 0
    clients : list[Client] = []
    listener : socket.socket = None

    def __init__(self, host: str = "localhost", port: int = 5000) -> None:
        self.host = host
        self.port = port

class ServerBuilder:

    server :Server
    id : int = 0

    def __init__(self, server: Server) -> None:
        self.server = server
    
    def create_server(self) -> socket.socket:
        self.server.listener = socket.create_server((self.server.host, self.server.port))
        print("Server is listening on port", self.server.port)
        return self.server.listener
    
    def get_server(self) -> Server:
        return self.server

    def start(self) -> None:
        while True:
            conn, addr = self.server.listener.accept()
            print(f"{addr} has connected to the server")

            print("conut of active thread", active_count())
            client = Client(self.id, conn, addr)
            client.start()
            print("conut of active thread", active_count())
            self.server.clients.append(client)

            self.id += 1


