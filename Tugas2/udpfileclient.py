import socket
import os

TARGET_IP = "192.168.1.12"
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

namafile="d:/TC ITS/Smt. 6/Progjar/PROGJAR_05111740000062/Tugas2/bart.png"
ukuran = os.stat(namafile).st_size


fp = open(namafile,'rb')
k = fp.read()
terkirim=0
# sock.sendto(k, (TARGET_IP, TARGET_PORT))
# for x in k:
#    sock.sendto(str(x).encode(), (TARGET_IP, TARGET_PORT))
#    terkirim = terkirim + 1
#    print(f"terkirim {terkirim} of {ukuran} ")
for x in k:
   k_bytes=bytes([x])
   sock.sendto(k_bytes, (TARGET_IP, TARGET_PORT))
   k = fp.read()
   terkirim = terkirim + 1
   print(k_bytes,f"terkirim {terkirim} of {ukuran} ")
fp.close()
sock.close()