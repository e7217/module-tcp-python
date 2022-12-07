import socket
import time
from threading import Thread, active_count

class Client:

    id : int = 0
    sock : socket.socket = None
    addr : tuple = None

    def __init__(self, id: int, sock: socket.socket, addr: tuple) -> None:
        self.id = id
        self.sock = sock
        self.addr = addr

    def start(self) -> None:
        t1 = Thread(target=self.recv_handler)
        t2 = Thread(target=self.send_handler)
        t1.start()
        t2.start()

    def recv_handler(self) -> None:
        try:
            while True:
                message = self.sock.recv(1024).decode()
                if message:
                    print(f"receive from client{self.id}: {message}")
        except ConnectionAbortedError as e:
            print(f"Client{self.id} has disconnected")
            self.sock.close()

    def send_handler(self) -> None:
        try:
            while True:
                time.sleep(1) 
                self.sock.send(f"Hello Client{self.id}".encode())
        except OSError as e:
            print(f"Client{self.id} has disconnected")
            self.sock.close()

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

if __name__ ==  "__main__":

    server = Server()
    builder = ServerBuilder(server)
    builder.create_server()
    builder.start()

