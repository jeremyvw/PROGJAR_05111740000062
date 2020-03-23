from control_file import Direct
import base64
import json
import logging

'''
        PROTOCOL FORMAT
string terbagi menjadi 2 bagian yang dipisahkan oleh spasi
Format : command *spasi* parameter *spasi* parameter
        FITUR
a. Meletakkan File
   Untuk meletakkan file ke dalam folder "drive"
   Request : add
   Parameter : namafile *spasi* isi dari file
   Response : jika berhasil -> "File Added
              jika gagal -> "ERROR"
b. List File
   Untuk melihat list file di dalam folder 'drive'
   Request : list
   Parameter: -
   Response: list file yang ada dalam folder 'drive'
c. Mengambil File
   Untuk mengambil file berdasarkan nama file dari folder 'drive'
   Request : get
   Parameter : namafile yang ingin diambil
   Response: file ter download pada folder tempat script berada
d. Jika command tidak dikenali akan merespon dengan ERRCMD
'''

d = Direct()

class FileMachine:
    def process(self, string_to_be_processed):
        string = string_to_be_processed
        split_string = string.split(' ')
        try:
            cmd = split_string[0].strip()
            if (cmd == 'add'):
                logging.warning('Adding')
                name = split_string[1].strip()
                file = split_string[2].strip()
                d.upload_file(name, file.encode())
                return "Success"
            
            elif (cmd == 'list'):
                logging.warning('List')
                data = {}
                data['files'] = []
                result = d.list_file()
                for filename in result:
                    data['files'].append({'Filename':filename})
                return json.dumps(data, indent=4)

            elif (cmd == 'get'):
                logging.warning('Getting')
                filename = split_string[1].strip()
                print('Retrieving',filename)
                res = d.download_file(filename)
                return res

            else:
                return 'ERRCMD'

        except:
            return 'ERROR'

if __name__=='__main__':
    mchn = FileMachine()
