# Penjelasan Tugas 4

Aplikasi yang sudah di-deploy dapat diakses melalui tautan berikut:
http://beaston-tugas-2.herokuapp.com/todolist/ (butuh login terlebih dahulu)

Akun yang dibuat adalah:
1. username: penggunasatu | password: apakabar123
2. username: penggunadua | password: apakabar123

### Apa kegunaan {% csrf_token %} pada elemen `<form>`

`{% csrf_token %}` adalah sintaks yang disediakan oleh Django untuk menyediakan token yang berfungsi agar bisa terhindar dari serangan CSRF atau Cross Site Request Forgery. Tipe serangan ini terjadi ketika suatu website yang jahat mengandung link, button form, atau sebuah script JavaScript yang dibuat agar browser pengguna meminta request ke server yang bisa membuat perubahan pada server tersebut. Server akan beranggapan bahwa karena request diminta dengan cookies pengguna, maka pengguna tersebut benar-benar melakukan request, padahal kenyataannya tidak. Tanpa adanya tag tersebut, dengan mendapatkan cookie yang sama dengan pengguna, maka aktor jahat bisa berpura-pura seperti pengguna. (Sumber: https://docs.djangoproject.com/en/4.1/ref/csrf/ dan https://www.squarefree.com/securitytips/web-developers.html#CSRF)

### Apakah elemen `<form>` dapat dibuat secara manual?
Bisa. Sintaks `{{ form.as_table }}` adalah sintaks yang disediakan oleh django untuk menampilkan form sebagai table, dengan syarat bahwa sintaks tersebut terletak dalam tags `<table></table>`. Apabila kita ingin menampilkan form secara manual, maka kita harus membuat semua kolom input, label, dan button submit dengan name, type, value, dan labelnya masing-masing yang sesuai. 

### Proses alur data
Pengguna akan diminta untuk memasukkan data ke kolom form yang sesuai dan melakukan submit atas data tersebut. Setelah submisi dilakukan, maka server akan mengecek token CSRF. Proses submisi selanjutnya akan melalui proses pengecekan data terhadap atribut yang terdapat pada models. Lalu apabila sudah sesuai maka program akan melakukan proses migrasi data ke database. Berdasarkan models, data yang dimasukkan ke dalam database tidak hanya title dan description, melainkan juga user yang saat itu terlogged-in, dan date saat data di-submit. Setelah data sudah disimpan, maka `views.py` akan mengambil data-data yang terdapat di database dan di-filter berdasarkan user yang meng-submit-nya saja, lalu akan dilakukan render ke dalam template. Template lalu akan melakukan looping terhadap data ini, dan menampilkannya satu per satu yang sudah dimasukkan ke dalam format HTML agar bisa tampil dengan rapih kepada pengguna.

### Cara implementasi
1. Membuat aplikasi baru bernama todolist dengan startapp pada Command Prompt.
2. Menambahkan aplikasi tersebut pada `INSTALLED_APPS` di `settings.py` project_django.
2. Menambahkan path `todolist` ke dalam `urls.py` di project_django, dengan meng-include urls pada todolist.
3. Membuat field atribut yang sesuai pada `models.py`.
4. Membuat `views.py` untuk setiap fungsionalitas yang akan dilakukan program, seperti register, login, logout, halaman utama, dan halaman add task. Fungsi akan me-render response ke dalam template HTML masing-masing. Fungsionalitas Form dibuat dengan menyusun `forms.py` yang field-nya disesuaikan dengan `models.py`.
5. Membuat routing pada `urls.py` agar setiap path bisa diakses oleh pengguna.
6. Melakukan deploy aplikasi pada heroku.
7. Membuat 2 akun dan masing-masing akun menambahkan 3 dummy data pada aplikasi yang sudah di-deploy pada heroku.

# Penjelasan Tugas 5

Aplikasi yang sudah di-deploy dapat diakses melalui tautan berikut:
http://beaston-tugas-2.herokuapp.com/todolist/ (butuh login terlebih dahulu)

Akun yang dibuat adalah:
1. username: penggunasatu | password: apakabar123
2. username: penggunadua | password: apakabar123

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Inline digunakan untuk melakukan styling CSS pada satu elemen HTML spesifik saja. Cara penerapannya adalah dengan memberikan atribut style tanpa menggunakan selector pada setiap tag HTML yang ingin kita lakukan styling. Kelebihan dari Inline CSS adalah prioritas stylingnya lebih tinggi dibandingkan dengan internal dan eksternal. Kekurangannya adalah jika kita ingin melakukan styling ke beberapa elemen, kita harus melakukannya satu per satu.

Internal CSS adalah styling CSS yang dilakukan dengan membuat tag `<style></style>` pada `<head>` file HTML. Kelebihan dari Internal CSS adalah bisa menggunakan selector dalam memilih elemen, dan Internal CSS memiliki prioritas lebih tinggi dibandingkan External CSS. Namun, kekurangannya adalah penambahan styling dengan Internal CSS yang banyak bisa membuat ukuran file HTML menjadi lebih besar dan memperlambat waktu loading page.

External CSS adalah styling CSS dengan membuat file eksternal berekstensi .css yang kemudian di-link pada `<head>` HTML. Kelebihan dari styling dengan External CSS adalah separasi antara struktur dan styling dalam membuat webpage, file HTML menjadi lebih bersih dan ringan, serta file .css yang sama bisa digunakan untuk file HTML berbeda. Kekurangannya adalah prioritasnya yang paling rendah dibandingkan Internal dan Inline CSS, page tidak akan ditampilkan dengan baik sebelum file CSS berhasil di-load, serta proses upload dan linking file CSS yang banyak bisa menurunkan waktu download website.

### Jelaskan tag HTML5 yang kamu ketahui
Terdapat sekumpulan tag HTML5 dengan kegunaannya masing-masing. Beberapa tag tersebut yang saya ketahui yaitu adalah `<head></head>` untuk head HTML, `<body></body>` untuk body HTML, `<p></p>` untuk paragraf, `<button></button>` untuk membuat button, `<a></a>` sebagai anchor link, `<h1></h1>` sampai `<h6></h6>` untuk header, `<img>` untuk menyisipkan gambar, `<span></span>` untuk span elemen, `<strong></strong>` dan `<em></em>` sebagai penegasan untuk aksesibilitas pengguna, `<style></style>` untuk styling CSS, `<table></table>`, `<td></td>`, `<tr></tr>`, `<th></th>` untuk membuat table dan elemen-elemennya, `<ul></ul>` untuk unordered list,` <ol></ol>` untuk ordered list, dan `<div></div>` untuk membuat divisi bagian elemen.

### Jelaskan tipe-tipe CSS selector yang kamu ketahui
1. elemen (p, h1, body) = Memilih elemen berdasarkan tag
2. .class (.nama-class) = Memilih elemen yang memiliki nama class "nama-class"
3. .class1.class2 = Memilih elemen yang memiliki kedua class1 dan class2.
4. .class1 .class2 = Memilih elemen yang memiliki class2 nya merupakan keturunan class1 (tidak hanya langsung, bisa berupa kakek) (berlaku juga untuk tag)
5. elemen1 > elemen2 = Memilih elemen2 yang merupakan turunan langsung (hubungan anak terhadap orangtua) dari elemen1
6. #id = Memilih elemen dengan id tertentu
7. `*` = Memilih semua elemen

### Cara implementasi
Proses styling CSS pada tugas 5 ini menggunakan framework CSS Bootstrap, serta juga memanfaatkan styling External dan Inline CSS. Login, Register, Todolist dan Add Task memanfaatkan flexbox yang akan meng-align elemen sesuai keinginan kita tanpa harus pusing memikirkan margin. Elemen akan dibagi menjadi beberapa bagian menggunakan `<div></div>` agar bisa disusun menggunakan flexbox. Cards diimplementasikan dengan memanfaatkan syntax dari Bootstrap yang kemudian sedikit dimodifikasi dengan CSS vanilla. Padding, Margin, dan Gap juga diimplementasikan agar elemen tidak saling berhimpitan dan bertabrakan. Sebagai bonus, saya juga mengimplementasikan selector hover dengan menggunakan transisi agar tampil layaknya animasi.