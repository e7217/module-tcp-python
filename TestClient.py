import socket
import struct
import time


class TestClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.socket.setblocking(False)

    def send(self, data):
        try:
            self.socket.send(data)
        except socket.error:
            pass

    def receive(self):
        try:
            data = self.socket.recv(1024)
            return data
        except socket.error:
            pass

    def close(self):
        self.socket.close()

packet = b"\x02\x01\x01\x00\x00\x03"

client = TestClient(host="127.0.0.1", port=5000)

for i in range(0, 1):
    client.send(packet)
    time.sleep(1)
    
client.close()