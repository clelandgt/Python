import socket
import threading

HOST = "127.0.0.1"
PORT = 9999
BUFSIZE = 1024
ADDR = (HOST, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(5)
print "[*] Listening on %s:%d " % (HOST, PORT)

# This is client work thread
def Handle_Client(client_socket):

    # Print message from client
    request = client_socket.recv(BUFSIZE)
    print "[*] Recevied: %s" % request

    # return data package
    client_socket.send("ACK!")
    client_socket.close()

while True:
    client, addr = server.accept()
    print "[*] Accepted connection from: %s", addr

    # Hang up client threading, and handle data.
    client_handle = threading.Thread(target=Handle_Client, args=(client,))
    client_handle.start()




