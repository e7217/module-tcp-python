import socket

host = "127.0.0.1"
port = 5000

Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client.connect((host, port))

print("Connected to server")
Client.send("Hello Server".encode())

print("Send message to Server")
data = Client.recv(1024).decode()

print(f"Receive from server : {data}")
Client.close()