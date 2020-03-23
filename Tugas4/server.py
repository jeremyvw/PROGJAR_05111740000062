import socket
import threading
import logging
import time
import sys
import base64

from file_machine import FileMachine

fm = FileMachine()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        while True:
            data = self.connection.recv(1024)
            if data:
                d = data.decode()
                res = fm.process(d)
                print(res)
                self.connection.sendall(res.encode())
            else:
                break
        self.connection.close()

class Server(threading.Thread):
    def __init__(self):
        self.clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 7777))
        self.my_socket.listen(1)

        while True:
            self.connection, self.client_addr = self.my_socket.accept()
            logging.warning(f'Connection from {self.client_addr}')
            clnt = ProcessTheClient(self.connection, self.client_addr)
            clnt.start()
            self.clients.append(clnt)

def main():
    print('Server is running...')
    srvr = Server()
    srvr.start()

if __name__ == '__main__':
    main()
