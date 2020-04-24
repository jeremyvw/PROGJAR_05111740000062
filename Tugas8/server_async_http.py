import socket
import time
import sys
import asyncore
from  http import HttpServer

httpserver = HttpServer()

class ProcessTheClient(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(1024)
        if data:
            self.sendall("{}" . format(httpserver.proses(data)))
        self.close()

class Server(asyncore.dispatcher):
        def __init__(self):
            asyncore.dispatcher.__init__(self)

        def handle_accept(self):
            pair = self.accept()
            if pair is not None:
                sock, addr = pair
                print >> sys.stderr, 'Connection from', repr(addr)
                handler = ProcessTheClient(sock)

def main():
	svr = Server()
	asyncore.loop()

if __name__=="__main__":
	main()