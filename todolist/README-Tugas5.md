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
elemen (p, h1, body) = Memilih elemen berdasarkan tag
.class (.nama-class) = Memilih elemen yang memiliki nama class "nama-class"
.class1.class2 = Memilih elemen yang memiliki kedua class1 dan class2.
.class1 .class2 = Memilih elemen yang memiliki class2 nya merupakan keturunan class1 (tidak hanya langsung, bisa berupa kakek) (berlaku juga untuk tag)
elemen1 > elemen2 = Memilih elemen2 yang merupakan turunan langsung (hubungan anak terhadap orangtua) dari elemen1
#id = Memilih elemen dengan id tertentu
`*` = Memilih semua elemen

### Cara implementasi
Proses styling CSS pada tugas 5 ini menggunakan framework CSS Bootstrap, serta juga memanfaatkan styling External dan Inline CSS. Login, Register, Todolist dan Add Task memanfaatkan flexbox yang akan meng-align elemen sesuai keinginan kita tanpa harus pusing memikirkan margin. Elemen akan dibagi menjadi beberapa bagian menggunakan `<div></div>` agar bisa disusun menggunakan flexbox. Cards diimplementasikan dengan memanfaatkan syntax dari Bootstrap yang kemudian sedikit dimodifikasi dengan CSS vanilla. Padding, Margin, dan Gap juga diimplementasikan agar elemen tidak saling berhimpitan dan bertabrakan. Sebagai bonus, saya juga mengimplementasikan selector hover dengan menggunakan transisi agar tampil layaknya animasi.