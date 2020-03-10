# Tugas 1
### Menyiapkan ketiga server port 31000, 31001, 31002

## Pada PC yang sama
#### Kondisi Awal Server dan Client
![Kondisi Awal](SS/server_init.jpg)

#### Client mengirimkan pesan ke server port 31000

![31000](SS/server_31000.jpg)
![31000](SS/client_31000.jpg)

#### Client mengirimkan pesan ke server port 31001

![31001](SS/server_31001.jpg)
![31001](SS/client_31001.jpg)

#### Client mengirimkan pesan ke server port 31002

![31002](SS/server_31002.jpg)
![31002](SS/client_31002.jpg)

## Pada PC yang berbeda
### Jalankan program server.py di 3 port yang berbeda di 2 komputer yang berbeda

![Server home](SS/server_home_init.jpg)
#### Server dijalankan pada 192.168.0.15
![Server laptop](SS/server_laptop_init.jpg)
#### Server dijalankan pada 192.168.0.12

### Jalankan program client.py untuk konek ke server pada poin sebelumnya, kirimkan string yang sama

#### Client dari 192.168.0.15 connect ke 192.0.168.12 
![Client 31000 to Laptop](SS/client_31000_connect_to_laptop.jpg)
![Client 31001 to Laptop](SS/client_31001_connect_to_laptop.jpg)
![Client 31002 to Laptop](SS/client_31002_connect_to_laptop.jpg)

#### Server dari 192.168.0.12 menerima koneksi dari 192.168.0.15
![Server 31000 from Home](SS/server_31000_connect_from_home.jpg)
![Server 31001 from Home](SS/server_31001_connect_from_home.jpg)
![Server 31002 from Home](SS/server_31002_connect_from_home.jpg)
![Server Laptop](SS/server_connect_from_home.jpg)

#### Client dari 192.168.0.12 connect ke 192.0.168.15 
![Client 31000 to Home](SS/client_31000_connect_to_home.jpg)
![Client 31001 to Home](SS/client_31001_connect_to_home.jpg)
![Client 31002 to Home](SS/client_31002_connect_to_home.jpg)

#### Server dari 192.168.0.15 menerima koneksi dari 192.168.0.12
![Server 31000 from Laptop](SS/server_31000_connect_from_laptop.jpg)
![Server 31001 from Laptop](SS/server_31001_connect_from_laptop.jpg)
![Server 31002 from Laptop](SS/server_31002_connect_from_laptop.jpg)
![Server Home](SS/server_connect_from_laptop.jpg)
