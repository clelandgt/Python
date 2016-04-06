import sys
import socket
import threading

BUFSIZE = 1024

# modify any requests destined for the remote host
def RequstHandle(buffer):

    return buffer

# modify any responses destined for the local host
def RespondHandle(buffer):

    return buffer


def ReveiveFrom(connection):

    buffer = ""

    # We set a 2 second time out depending on your target this may need to be adjusted.
    connection.settimeout(2)

    try:
        # Keeping read data into buffer until not data or time out.
        while True:
            data = connection.recv(BUFSIZE)
            if not data:
                break
            buffer + data

    except:
        pass

    return buffer


def HexDump(src, length=16):

    result = []
    digits = 4 if isinstance(src, unicode) else 2

    for i in xrange(0, len(src), length):
       s = src[i:i+length]
       hexa = b' '.join(["%0*X" % (digits, ord(x))  for x in s])
       text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.'  for x in s])
       result.append( b"%04X   %-*s   %s" % (i, length*(digits + 1), hexa, text) )

    print b'\n'.join(result)


def Proxy_Handle(clientSocket, remoteHost, remotePort, receiveFirst):

    # connect the remote
    remoteSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remoteSocket.connect((remoteHost, remotePort))

    # receive data from the remote if necessary
    if receiveFirst:
        remoteBuffer = ReveiveFrom(remoteSocket)
        HexDump(remoteBuffer)

        remoteBuffer = RequstHandle(remoteBuffer)

        # Send data to local, if data not empty
        if len(remoteBuffer):
            print "[<==] Sending % bytes to localhost." % len(remoteBuffer)
            clientSocket.send(remoteBuffer)

    # Now let's loop and reading from local, send to remote, send to local rinse wash repeat
    while True:

        # Read data from local
        localBuffer = ReveiveFrom(clientSocket)

        if len(localBuffer):
            print "[==>] Received $ bytes from localhost." % len(localBuffer)
            hex(localBuffer)

            localBuffer =RequstHandle(localBuffer)

            # Send data to the remote
            remoteSocket.send(localBuffer)
            print "[==>] Send to remote."

        # Receive response data
        remoteBuffer = ReveiveFrom(remoteSocket)

        if len(remoteBuffer):
            print "[<==] Received % bytes from remote." % len(remoteBuffer)
            HexDump(remoteBuffer)

            # Send to RespondHandle
            remoteBuffer = RespondHandle(remoteBuffer)

            # Send data to localhost
            clientSocket.send(remoteBuffer)
            print "[<==] Send to localhost"

        # Close connect, if not data in two side.
        if not len(localBuffer) or not len(remoteBuffer):
            clientSocket.close()
            remoteSocket.close()
            print "[*] No more data. Closing connections"
            break


def ServerLoop(localHost, localPort, remoteHost, remotePort, reveiveFirst):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((localHost, localPort))

    except:
        print "[!!] Failed to listen on %s:%d" % (localHost, localPort)
        print "[!!] Check for other listening sockets or correct permission"

    server.listen(5)

    while True:
        clientSocket, addr = server.accept()

        # print local connection message
        print "[==>] Received incoming connection from %s:%d" % (addr[0], addr[1])


        # Create a thread to connect with remote pc
        proxyThraed = threading.Thread(target=Proxy_Handle, args=(clientSocket, remoteHost, remotePort, reveiveFirst))
        proxyThraed.start()


def main():

    if len(sys.argv[1:]) != 5:
        print "Usage: ./proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]"
        print "Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True"
        sys.exit(0)

    localHost = sys.argv[1]
    localPort = int(sys.argv[2])
    remoteHost = sys.argv[3]
    remotePort = int(sys.argv[4])
    receiveFirst = sys.argv[5]

    if "True" in receiveFirst:
        receiveFirst = True
    else:
        receiveFirst = False

    ServerLoop(localHost,localPort, remoteHost, remotePort, receiveFirst)

if __name__ == "__main__":
    main()