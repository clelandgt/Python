import socket

import os
import struct
from ctypes import *

BUFSIZE = 65565
host = "192.168.1.103"

# IP Class definition
class IP(Structure):
    _fields_ = [
        ("ihl",         c_ubyte, 4),
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


class ICMP(Structure):
    _fields_ = [
        ("type",        c_ubyte),
        ("code",        c_ubyte),
        ("checksum",    c_ushort),
        ("unused",      c_short),
        ("next_hop_mtu",c_ushort)
    ]

    def __new__(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer):
        pass

if __name__ == "__main__":
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

            # Handle, if ICMP
            if ip_header.protocol == "ICMP":
                # Calculate start position of ICMP package
                offset = ip_header.ihl * 4
                buf = raw_buffer[offset:offset + sizeof(ICMP)]

                # Decode ICMP
                icmp_header = ICMP(buf)

                print "ICMP ->Type: %d Code: %d" % (icmp_header.type, icmp_header.code)

    # Handle CTRL-C
    except KeyboardInterrupt:

        if os.name == "nt":
            sniffer.ioctl(socket.SIO_RCVALL, socket.SIP_RCALL_OFF)