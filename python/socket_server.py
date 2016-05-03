# -*- encoding: utf-8 -*-

import SocketServer
import socket
import threading


class EchoRequestHander(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        print 'Handle %s' % data
        self.request.send(data)
        return


if __name__ == '__main__':
    address = ('localhost', 0)
    server = SocketServer.TCPServer(address, EchoRequestHander)
    ip, port = server.server_address

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)
    t.start()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    message = 'Hello, world'
    len_sent = s.send(message)

    response = s.recv(len_sent)
    print 'Recv %s' % response

    server.shutdown()
    s.close()
    server.socket.close()
