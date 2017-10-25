# coding=utf-8

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = 'This is the message.'

try:
    sent = sock.sendto(message, server_address)

    data, server = sock.recvfrom(4096)

    print >> sys.stderr, 'received %r' % data

finally:
    sock.close()