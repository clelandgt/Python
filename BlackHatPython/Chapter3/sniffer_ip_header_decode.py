import socket

import os
import struct
from ctypes import *

BUFSIZE = 65565
host = "192.168.1.103"

# IP Class definition
class IP(Structure):
    _fields_ = [
        ("ih1",         c_ubyte, 4),
        ("version",     c_ubyte, 4),
        ("tos",         c_ubyte),
        ("len",         c_ushort),
        ("id",          c_ushort),
        ("offset",      c_ushort),
        ("ttl",         c_ubyte),
        ("protocol_num",c_ubyte),
        ("sum",         c_ushort),
        ("src",         c_uint32),
        ("dst",         c_uint32)
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        #  Protocol Field map the Name
        self.protocol_map = {1:"ICMP", 6:"TCP", 17:"UDP"}

        # More readable IP address.
        self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))

        # Type of Protocol
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)

if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP

else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW, socket_protocol)

sniffer.bind((host,0))
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.SIP_RCALL_ON)

try:
    while True:
        # Read data package
        raw_buffer = sniffer.recvfrom(BUFSIZE)[0]

        # 20 data before parsing
        ip_header = IP(raw_buffer[0:20])

         # Output protocol and ip addresses
        print "Protocol: %s %s -> %s" % (ip_header.protocol, ip_header.src_address, ip_header.dst_address)

# Handle CTRL-C
except KeyboardInterrupt:

    if os.name == "nt":
        sniffer.ioctl(socket.SIO_RCVALL, socket.SIP_RCALL_OFF)




