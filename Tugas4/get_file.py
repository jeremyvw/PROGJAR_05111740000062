import socket
import sys
import base64
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('127.0.0.1', 7777)
print(sys.stderr, 'Connecting to %s port %s' % server_addr)

sock.connect(server_addr)

try:
    filename = 'file.txt'
    msg = 'get '+filename
    print('Requesting file to server')
    sock.send(msg.encode())

    data = sock.recv(4096)
    tmp = open(filename,'wb')
    tmp.write(data)
    tmp.close()

    print('File has been received')
finally:
    print('Closing connection')
    sock.close()