from dataclasses import dataclass, field
import socket
import time
from threading import Thread, active_count

from app.model.Client import ClientSocket

@dataclass
class Server:

    host :str = "localhost"
    port :int = 5000
    clients : list[ClientSocket] = field(default_factory=list)
    listener : socket.socket = None

class ServerBuilder:

    server : Server = None
    id : int = 0

    def __init__(self, server: Server) -> None:
        self.server = server
    
    def create_server(self) -> socket.socket:
        self.server.listener = socket.create_server((self.server.host, self.server.port))
        print("Address of Server is ", self.server.host)
        print("Server is listening on port", self.server.port)
        return self.server.listener
    
    def get_server(self) -> Server:
        return self.server

    def start(self) -> None:
        with self.server.listener as Listener:
            while True:
                conn, addr = Listener.accept()
                print(f"{addr} has connected to the server")

                print("conut of active thread", active_count())
                client = ClientSocket(self.id, conn, addr)
                client.start()
                print("conut of active thread", active_count())
                self.server.clients.append(client)

                self.id += 1


