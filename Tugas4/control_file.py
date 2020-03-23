import base64
import shelve
import uuid
import socket
import os

class Direct:
    def __init__(self):
        if not os.path.exists('files'):
            os.makedirs('files')
    
    def upload_file(self, name=None, file=None):
        data_file = file
        # print(base64.decodestring(data_file))
        f = open('files/'+ name, 'wb')
        f.write(data_file)
        return True

    def download_file(self, name=None):
        # arr = []
        f = open('files/'+ name, 'rb')
        res = f.read()
        f.close()
        res = str(res,'utf-8')
        return res

    def list_file(self):
        file_list = os.listdir('files')
        return file_list

if __name__=='__main__':
    d = Direct()
    # input = 'Message.txt'
    print(d.list_file())