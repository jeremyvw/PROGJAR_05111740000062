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
    filename = input("Input file that want to be requested from server: ")
    s.sendall(filename.encode())
    print('Sent ', filename)
    while True:
        data = s.recv(100000)
        newfile = open("new_"+filename,"a+b")
        if not data:
            newfile.close()
            break
        newfile.write(data)
finally:
    print("Closing")
    s.close()