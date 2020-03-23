import socket
import sys
import base64
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('127.0.0.1', 7777)
print(sys.stderr, 'Connecting to %s port %s' % server_addr)
sock.connect(server_addr)

try:
    msg = 'list'
    sock.send(msg.encode())
    print('\nRequest has been sent')
    data = sock.recv(2048)
    print(data.decode())
finally:
    sock.close()