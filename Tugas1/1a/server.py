import sys
import socket
import os
# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 31000)
print("Starting up on ", server_address)
s.bind(server_address)
# Listen for incoming connections
s.listen(3)
while True:
    # Wait for a connection
    print("Waiting for a connection...")
    conn, client_address = s.accept()
    print("Connection from ", client_address)
    # Receive the data in small chunks and retransmit it
    while True:
        data = conn.recv(10000)
        print("Received ", data)
        f = open('d:/TC ITS/Smt. 6/Progjar/PROGJAR_05111740000062/Tugas1/1a/Newfile'+'.jpg','a+b')
        if not data:
            f.close()
            break
        f.write(data)
    # Clean up the connection
    conn.close() 