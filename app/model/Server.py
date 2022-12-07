class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.listener = None
        self.clients = []
        self.is_listening = False

    def create_server(self):
        self.listener = socket.create_server((self.host, self.port))
        self.is_listening = True
        print("Server is listening on port", self.port)

    def connect_with_client(self):
        conn, addr = self.listener.accept()
        self.clients.append(conn)
        print(f"{addr}has connected to the server")

    def send_message(self, message):
        for client in self.clients:
            client.send(message.encode())

    def receive_message(self):
        for client in self.clients:
            data = client.recv(1024).decode()
            print(f"receive : {data}")

    def is_listening(self):
        return self.is_listening

    def have_clients(self):
        return len(self.clients) > 0

    def close(self):
        self.listener.close()
        self.is_listening = False
        print("Server is closed")
