# coding=utf-8
import socket
import sys

server_address = './uds_socket'

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

try:
    sock.connection(server_address)
except socket.error, msg:
    print >> sys.stderr, msg
    sys.exit(1)

try:
    message = 'This is the message'
    print >> sys.stderr, 'sending %r' % message
    sock.sendall(message)

    data = sock.recv(100)

    print >> sys.stderr, 'received %r' % data
finally:
    print >> sys.stderr, 'closing socket'
    sock.close()