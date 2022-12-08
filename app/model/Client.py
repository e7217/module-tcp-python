from dataclasses import dataclass
import socket
import time
from threading import Thread


@dataclass
class ClientSocket:

    id : int = 0
    sock : socket.socket = None
    addr : tuple = None

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