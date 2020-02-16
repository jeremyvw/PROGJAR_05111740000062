import sys
import socket
import os
# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
# port = input("Input the port address: ")
# filename = input("Input the filename you want to send: ")
server_address = ('localhost', 31000)
print("Connecting to ", server_address)
s.connect(server_address)

try:
    # Send data
    filename = "Logo.jpg"
    f = open(filename,'rb')
    l = f.read()
    s.sendall(l)
    print('Sent ', repr(l))
    f.close()
finally:
    print("Closing")
    s.close()