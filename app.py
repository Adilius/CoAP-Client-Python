import socket

HOST = "coap://coap.me/"
PORT = 5682

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)

print(repr(data))