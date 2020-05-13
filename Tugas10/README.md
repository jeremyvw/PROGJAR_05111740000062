# Tugas 10

#### Menjalankan Asynchronous Server pada Port 9002, 9003, 9004, 9005

![1](Screenshots/async_server_start.png)

#### Menjalankan Load Balancer pada port 44444

![2](Screenshots/load_balancer_start.png)

#### Membuka browser pada http://localhost:44444/page.html

![3](Screenshots/html.png)

#### Bisa dilihat pada log program, setiap request akan dilayani oleh backend yang bergantian

![4](Screenshots/async_server_backend.png)
![5](Screenshots/load_balancer_backend.png)

### Stress Benchmark Asynchronous Server + Load Balancer

![20](Screenshots/)

#### Concurrency 1

![6](Screenshots/async_server_load_balancer_c1_1.png)
![7](Screenshots/async_server_load_balancer_c1_2.png)

#### Concurrency 5

![8](Screenshots/async_server_load_balancer_c5_1.png)
![9](Screenshots/async_server_load_balancer_c5_2.png)

#### Concurrency 10

![10](Screenshots/async_server_load_balancer_c10_1.png)
![11](Screenshots/async_server_load_balancer_c10_2.png)

#### Concurrency 20

![12](Screenshots/async_server_load_balancer_c20_1.png)
![13](Screenshots/async_server_load_balancer_c20_2.png)

#### Concurrency 30

![14](Screenshots/async_server_load_balancer_c30_1.png)
![15](Screenshots/async_server_load_balancer_c30_2.png)

#### Concurrency 50

![16](Screenshots/async_server_load_balancer_c50_1.png)
![17](Screenshots/async_server_load_balancer_c50_2.png)

#### Concurrency 100

![18](Screenshots/async_server_load_balancer_c100_1.png)
![19](Screenshots/async_server_load_balancer_c100_2.png)