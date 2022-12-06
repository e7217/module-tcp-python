import socket

host = "127.0.0.1"
port = 5000


# Listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Listener.bind((host, port))
# Listener.listen(1)

Listener = socket.create_server((host, port))

print("Server is listening on port", port)

conn, addr = Listener.accept()

print(f"{addr}has connected to the server")

data = conn.recv(1024).decode()
print(f"receive : {data}")

conn.send("Hello Client".encode())
print(f"send to client : {data}")

Listener.close()
