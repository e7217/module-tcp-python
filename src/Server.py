import socket

def create_server(host = "127.0.0.1", port = 5000):

    Server = socket.create_server((host, port))
    print("Server is listening on port", port)

    return Server

if __name__ ==  "__main__":
    Listener = create_server()

    print(Listener.getsockname())

    conn, addr = Listener.accept()

    print(f"{addr}has connected to the server")

    data = conn.recv(1024).decode()
    print(f"receive : {data}")

    conn.send("Hello Client".encode())
    print(f"send to client : {data}")

    Listener.close()


