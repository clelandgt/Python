import socket

HOST = "127.0.0.1"
PORT = 9999
BUFSIZE = 1024
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

client.send("hello")
data = client.recv(BUFSIZE)
if data:
    print data

client.close()