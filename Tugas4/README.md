# Tugas 4

String terbagi menjadi 2 bagian, dipisahkan oleh spasi 

*COMMAND* [spasi] *PARAMETER* [spasi] *PARAMETER* ...

1. Meletakkan file

* Request/Command: 'add'<br/>
* Parameter: _namafile_ [spasi] _isifile_ 
* Response:
    * Berhasil = 'Success'<br/>
    * Gagal = 'ERROR'

2. Mengambil file
* Request/Command: 'get'<br/>
* Parameter: _namafile_ [spasi] _isifile_
* Response:
    Retrrieving _namafile_<br/>_isifile_

3. Melihat list file pada direktori
* Request/Command: 'list'<br/>
* Parameter: Tidak ada
* Response:
    Daftar nama file pada direktori files dalam format **JSON** 

4. Jika Command tidak dikenali maka akan menampilkan pesan 'ERRCMD'

## Langkah-langkah 

1. Menambahkan/meletakkan file
- Jalankan file server.py dan kemudian jalankan file add_file.py

![1](screenshots/server_add_files.jpg)
- Keadaan direktori sebelum file add_file.py di eksekusi

![1](screenshots/before_add_files.jpg) 
- Keadaan direktori sesudah file add_file.py di eksekusi

![1](screenshots/after_add_files.jpg)

2. Mengambil file
- Jalankan file server.py dan kemudian jalankan file get_file.py

![2](screenshots/server_get_files.jpg)
- Keadaan direktori sebelum file add_file.py di eksekusi

![2](screenshots/before_get_files.jpg) 
- Keadaan direktori sesudah file add_file.py di eksekusi

![2](screenshots/after_get_files.jpg)

3. Melihat file-file pada direktori
- Keadaan pada direktori _files_ yang ingin dilihat

![3](screenshots/list_dir.jpg)
- Jalankan file server.py dan kemudian jalankan file list_file.py
![3](screenshots/server_list_files.png)




    