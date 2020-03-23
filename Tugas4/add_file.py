import socket
import sys
import base64
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('127.0.0.1', 7777)
print(sys.stderr, 'Connecting to %s port %s' % server_addr)

sock.connect(server_addr)

try:
    # filename = 'file2.txt'
    this_folder = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(this_folder, 'file2.txt')
    # filename='F:/Jeremy/Kuliah/Smt.6/Progjar/PROGJAR_05111740000062/Tugas4/file2.txt'
    tmp = open(filename, 'rb')
    file = tmp.read(2048)
    tmp.close()
    file = file.decode()
    msg = 'add '+filename+' '+file
    print('Adding file')
    sock.send(msg.encode())

    data = sock.recv(2048).decode()
    print(data)
finally:
    print('Closing connection...')
    sock.close()