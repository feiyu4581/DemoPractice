# coding=utf-8
import socket
import sys
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = './uds_socketer'

try:
    os.unlink(server_address)
except:
    if os.path.exists(server_address):
        raise

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_aserver_addresimport socket
import os

parent, child = socket.socketpair()

pid = os.fork()

if pid:
    print 'in parent, sending message'
    child.close()
    parent.sendall('ping')
    response = parent.recv(1024)
    print 'response from child:', response
    parent.close()

else:
    print 'in child, waiting for message'
    parent.close()
    message = child.recv(1024)
    print 'message from parent:', message
    child.sendall('pong')
    child.close()s')ddress = sock.accept()
    try:
        print >> sys.stderr, 'connection from', client_address

        while True:
            data = connection.recv(16)
            print >> sys.stderr, 'received "%s"' % data
            if data:
                print >> sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >> sys.stderr, 'no data from', client_address
                break
    finally:
        connection.close()



import socket
import os

parent, child = socket.socketpair()

pid = os.fork()

if pid:
    print 'in parent, sending message'
    child.close()
    parent.sendall('ping')
    response = parent.recv(1024)
    print 'response from child:', response
    parent.close()

else:
    print 'in child, waiting for message'
    parent.close()
    message = child.recv(1024)
    print 'message from parent:', message
    child.sendall('pong')
    child.close()