# coding=utf-8

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)

sock.bind(server_address)

while True:
    data, address = sock.recvfrom(4096)

    print >> sys.stderr, 'Received %r' % data

    if data:
        sent = sock.sendto(data, address)
        print >> sys.stderr, 'send %r bytes back to %s' % (sent, address)
