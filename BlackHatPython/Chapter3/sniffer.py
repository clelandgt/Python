import socket
import os

BUFSIZE = 65565
host = "192.168.1.100"

if os.name == 'nt:':
    socket_protocol = socket.IPPROTO_IP

else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind((host, 0))

# Set contain IP Head in data package.
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# Read single data package
print sniffer.recvfrom(BUFSIZE)

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


