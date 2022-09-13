# Penjelasan Tugas 2

Link aplikasi yang sudah di-deploy pada Heroku dapat diakses di sini:
https://beaston-tugas-2.herokuapp.com/


## Alur Program

GAMBAR DISINI

Pertama, client yang mengakses akan diarahkan requestnya sesuai dengan yang tersedia pada routes (urls.py). Jika URL yang diminta tersedia maka fungsinya yang sesuai pada views.py akan dipanggil. Pemanggilan fungsi tersebut akan melakukan query yang membutuhkan data dari models.py. Data tersebut diambil dari database (dari file .json dalam kasus ini). Setelah query didapatkan dari models, maka akan diteruskan kembali ke views, yang kemudian akan direspons kembali ke client melalui pemetaan HTML berdasarkan hasil proses sebelumnya.


## Mengapa Virtual Environment? Bisakah Kita Membuat Aplikasi Berbasis Django Tanpa Virtual Environment?

Aplikasi tentulah bisa dibuat tanpa melalui Virtual Environment. Namun, hal tersebut tidak begitu direkomendasikan karena Virtual Environment digunakan agar projek Django yang kita buat tidak akan mempengaruhi semua pekerjaan kita yang lain. Instalasi Django tanpa melalui Virtual Environment akan membuatnya terinstall secara global. Virtual Environment berguna agar setiap projek yang kita buat bisa terisolasi satu sama lain dan setiap projek tidak akan saling mempengaruhi.


## Cara Implementasi

### Settings views.py dan models.py

Kita memiliki end goal untuk bisa menampilkan data-data pada file HTML. Oleh karena itu, kita akan melakukan respons terhadap request client dengan menampilkan file HTML. Kita bisa mulai dengan membuat fungsi yang akan melakukan hal demikian. views.py akan meminta semua daftar barang yang terdapat pada models, nama, dan student id sehingga kita perlu mengisi fungsi agar bisa memberikan data tersebut. 

Agar data dari models bisa didapat, kita harus mengatur pula models.py dengan membuat suatu class yang berisi wadah untuk menampung data dari database. Database dalam kasus ini adalah file JSON initial_catalog_data.json. Setelah melakukan loaddata, maka models siap memberikan data kepada views.py jika dibutuhkan.

Fungsi yang sudah kita buat dalam views.py lalu akan melakukan respons pada file HTML dengan data-data yang sudah kita dapatkan dan buat sebelumnya, seperti data dari models, nama, dan student id.

### Proses Routing

Ketika client melakukan request URL (pada tugas ini adalah `/katalog`), maka akan mencocokannya pada file urls.py pada direktori `/project-django`. Untuk itu kita perlu memasukkan path `/katalog` tersebut pada `/project-django` dengan meng-include file urls.py yang dimiliki oleh `/katalog`.

File urls.py pada `/katalog` akan melakukan routing dengan memanggil fungsi show_katalog (yang sudah kita buat sebelumnya) pada views.py.

### Pemetaan Data pada File HTML

Data yang didapat dari models masih berupa list of objects. Oleh karena itu, untuk menampilkan data, kita perlu mengambil atribut dari data tersebut yang akan menghasilkan sebuah value.

1. Pertama, kita perlu melakukan looping pada list tersebut menggunakan {% for barang in list_barang %}. Untuk menutup for loop digunakan {% endfor %}
2. Karena data yang diminta harus dalam format table, maka kita gunakan tag html <tr></tr> untuk membuat baris tabel, dengan elemennya menggunakan tag <th></th>
3. Kita mengisi elemen pada th dengan atribut objek yang sesuai. Sebagai contoh, untuk data yang pertama kita ambil atribut item_name dengan menggunakan sintaks {{barang.item_name}}. Lakukan terus untuk setiap atribut (item_name, item_price, item_stock, rating, description, item_url)

### Deploy ke Heroku

Untuk bisa melakukan deploy ke Heroku, semua file harus sudah di add, commit, dan push ke dalam repositori remote GitHub. Kemudian, buatlah app baru pada Heroku. Lalu kita akan meng-copy account API serta nama app pada Heroku ke dalam Secrets yang terdapat pada GitHub. Secrets bisa diakses melalui `Settings -> Secrets -> Actions`. Kita akan menambahkan secret bernama HEROKU_API_KEY dengan valuenya adalah account API Heroku, serta HEROKU_APP_NAME dengan valuenya adalah nama aplikasi milik kita di Heroku.

Setelah secrets berhasil dibuat, maka langkah selanjutnya adalah menjalankan kembali workflow yang gagal pada tab `Actions` di GitHub. Tunggu proses selesai (hingga terdapat centang hijau), lalu projek sudah bisa diakses.