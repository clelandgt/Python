# !/usr/bin/env python

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

try:

    while True:
        print 'waiting for connection...'
        tcpCliSock, addr = tcpSerSock.accept()
        print '...connected from:', addr

        while True:
            data = tcpCliSock.recv(BUFSIZE)
            if not data:
                tcpCliSock.close()
                break
            data = tcpCliSock.send('[%s] %s' % (ctime(), data))

    tcpSerSock.close()
except Exception, e:
    print e


