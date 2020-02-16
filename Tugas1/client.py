import sys
import socket
import os
# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
port = input("Input the port address: ")
server_address = ('localhost', int(port))
print("Connecting to ", server_address)
s.connect(server_address)

try:
    # Send data
    message = 'PEMROGRAMAN JARINGAN TEKNIK INFORMATIKA'
    print("Sending ", message)
    s.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = s.recv(64)
        amount_received += len(data)
        print(data)
finally:
    print("Closing")
    s.close()