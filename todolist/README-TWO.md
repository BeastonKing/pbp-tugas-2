# Penjelasan Tugas 6

Aplikasi yang sudah di-deploy dapat diakses melalui tautan berikut:
http://beaston-tugas-2.herokuapp.com/todolist/ (butuh login terlebih dahulu)
Login dapat diakses melalui link: http://beaston-tugas-2.herokuapp.com/todolist/login/

Akun yang dibuat adalah:
1. username: penggunasatu | password: apakabar123
2. username: penggunadua | password: apakabar123

### Synchronous Programming vs Asynchronous Programming

##### Synchronous Programming
Synchronous Programming adalah suatu cara pemrograman di mana operation tasks dilakukan satu persatu. Task yang selanjutnya akan dieksekusi tidak akan mulai berjalan sampai task yang sedang dieksekusi selesai berjalan. Sehingga, kita harus menunggu suatu task untuk selesai dieksekusi untuk mulai bisa mengeksekusi task-task selanjutnya.

##### Asynchronous Programming
Asynchronous Programming adalah pemrograman di mana kita tidak harus menunggu suatu proses selesai untuk bisa menjalankan proses selanjutnya. Dengan kata lain, dalam operasi asinkronus, ketika suatu proses sedang berjalan, kita bisa pindah ke proses lain sebelum proses pertama tersebut selesai dieksekusi. Pemrograman ini memungkinkan kita bisa melakukan handling beberapa request sekaligus, yang akan mampu menyelesaikan lebih banyak proses dengan waktu yang lebih cepat.

### Event-Driven Programming pada Tugas
Paradigma Event-Driven Programming adalah suatu paradigma pemrograman di mana alur dari suatu program ditentukan oleh event-event. Event dalam kasus ini adalah bisa berupa input dari user, sensor, message passing, dan sebagainya. Pada paradigma ini, terdapat fungsi yang selalu melakukan listening terhadap event dan jika event tersebut ditangkap, maka fungsi akan berjalan. Penerapan Event-Driven Programming pada tugas 6 ini adalah dalam penerapan AJAX POST dan GET menggunakan jQuery. 

### Penerapan Asynchronous Programming
Setelah melakukan penambahan Task, maka AJAX akan melakukan POST dan GET secara asinkronus, dalam artian bahwa halaman web akan mengalami perubahan jika dan hanya jika terjadi update baru dari pengguna. Proses listening terhadap perubahan ini juga berlangsung terus-menerus tanpa ada titik pasti kapan perubahan itu terjadi karena update bergantung pada pengguna, atau bisa disebut asinkronus. Perubahan ini juga tidak memerlukan pemuatan ulang halaman dengan menggunakan Refresh Page yang mampu menghemat sumber daya.

### Cara Implementasi Checklist
##### AJAX GET
Untuk proses GET digunakan jQuery. Sebelum itu, saya menambahkan path `json/` dan mengatur view-nya sehingga path tersebut mengembalikan data dari database dalam bentuk file JSON. Kemudian, akan dilakukan AJAX GET yang akan melakukan GET dari path `json/` tersebut yang kemudian akan melakukan passing array of objects tersebut. Setiap individual objek akan dilakukan iterate menggunakan method `forEach()` yang kemudian akan diakses atributnya, dan di-append ke dalam elemen HTML yang sesuai dengan class-nya yang sesuai pula.

##### AJAX POST
Mirip dengan AJAX GET, AJAX POST juga diterapkan dengan memanfaatkan jQuery. Sebelumnya, dibuat path `add/` yang diatur view-nya agar fungsi tersebut bisa menerima data yang dimasukkan oleh pengguna, menambahkannya ke dalam database, lalu akan mengembalikan response berbentuk JSON berdasarkan data yang dimasukkan tersebut. Untuk pemasukkan input itu sendiri, saya menggunakan Modal yang diimplementasikan menggunakan framework Bootstrap yang akan muncul jika pengguna menekan button Add Task pada navbar halaman utama. Modal ini akan meminta input dari pengguna dan akan di-submit dengan button Create. Setelah data berhasil di-input, maka Modal akan tertutup sendiri dan AJAX POST akan berjalan serta kemudian mengirim data tersebut ke path `add/` dengan view-nya sendiri yang sudah dibuat sebelumnya. Hasil return dari view tersebut yang berupa JSON akan dikembalikan kepada AJAX. Jika proses tersebut berhasil, maka fungsi success pada AJAX akan berjalan, dan jika gagal maka fungsi error yang akan berjalan. Fungsi success akan menerima hasil return tersebut sebagai response dan kemudian akan melakukan append elemen response tersebut ke dalam HTML dengan tags dan class-nya yang sesuai. Hal ini bertujuan agar halaman tidak perlu dilakukan refresh untuk meng-update data baru ini. 
