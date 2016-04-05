import socket

target_host = "127.0.0.1"
target_port = 9999
ADDR = (target_host, target_port)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("Hello", (target_host, target_port))
data = client.recv(4096)
print data
