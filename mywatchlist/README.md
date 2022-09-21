# Penjelasan Tugas 3

Link aplikasi yang sudah di-deploy pada Heroku dapat diakses di sini:
https://beaston-tugas-2.herokuapp.com/

## Perbedaan JSON, XML, dan HTML
JSON atau JavaScript Object Notation adalah suatu format pertukaran data yang berbasis bahasa pemrograman JavaScript. Meskipun basis JSON adalah JavaScript namun JSON independen dari semua bahasa pemrograman. JSON merepresentasikan data dengan dua cara, yakni object dan array. Object adalah koleksi yang terdiri dari pasangan key dan value. Array adalah koleksi terurut yang berisi value. Array dapat berisi object, dan sebaliknya. Contoh kode JSON:
```
[{"FilmID":"catmanbegins", "Image":"https://m.media-amazon.com/images/catmanbegins.jpg"},
  {"FilmID":"cabdriver", "Image":"https://m.media-amazon.com/images/cabdriver.jpg"},
  {"FilmID":"pulpnonfiction", "Image":"https://m.media-amazon.com/images/pulpnonfiction.jpg"},
  {"FilmID":"doctornormal", "Image":"https://m.media-amazon.com/images/doctornormal.jpg"},
  {"FilmID":"backtothepresent", "Image":"https://m.media-amazon.com/images/backtothepresent.jpg"}];
```

XML atau Extensible Markup Language adalah format berbasis teks untuk merepresentasikan informasi terstruktur seperti dokumen, data, konfigurasi, transaksi, dan lainnya. Mirip seperti HTML, XML terdiri dari tags (opening dan closing) untuk menggambarkan susunan data. Contoh kode XML:
```
<employees>
  <employee>
    <firstName>John</firstName> <lastName>Doe</lastName>
  </employee>
  <employee>
    <firstName>Anna</firstName> <lastName>Smith</lastName>
  </employee>
  <employee>
    <firstName>Peter</firstName> <lastName>Jones</lastName>
  </employee>
</employees>
```

JSON dan XML dapat digunakan untuk mengambil data dari suatu web server. Keduanya mudah untuk dibaca manusia, memiliki hirarki, dan dapat di-parse dan digunakan oleh banyak bahasa pemrograman lain. Perbedaan keduanya adalah JSON tidak menggunakan end tag, lebih pendek, lebih cepat untuk dibaca dan ditulis, dan JSON dapat menggunakan array.

HTML atau Hypertext Markup Language adalah suatu bahasa markup yang digunakan untuk membangun sebuah struktur dari halaman web. Sebuah file HTML dapat dibuat sedemikian rupa agar bisa ditampilkan pada sebuah browser. HTML tersusun atas tags (opening dan closing), dapat dipercantik dengan bantuan CSS (Cascading Style Sheets), dan dapat diberikan logika dengan JavaScript. Dalam HTML, pengguna dapat menuliskan kode untuk membuat berbagai elemen pada halaman web, seperti paragraf, list, heading, button, image, dan masih banyak lagi. Berikut adalah contoh kode HTML:
```
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```

## Mengapa Data Delivery Dibutuhkan dalam Pengimplementasian Platform?
Kita membutuhkan data delivery agar kita bisa mengirimkan data ke suatu tempat. Sebagai contoh, apabila seorang pengguna melakukan request pada front-end, maka front-end akan meminta back-end untuk mengirimkan (response) data yang diminta oleh pengguna. Setelah request diproses di back-end maka dihasilkanlah data. Untuk sampai ke pengguna, data harus melalui proses data delivery. Data delivery ini akan mengirimkan data dari back-end yang sudah diolah, kembali kepada pengguna.

## Cara Pengimplementasian Checklist
Aplikasi baru dapat dibuat menggunakan command `python manage.py startapp mywatchlist`. Aplikasi lalu ditambahkan pada settings project_django pada bagian installed_apps. Path `/mywatchlist` kemudian ditambahkan pada file urls.py project_django agar pengguna bisa mengakses path tersebut. Pada folder aplikasi lalu ditambahkan class MyWatchList dalam models.py dengan atribut watched (textfield), title (charfield), rating (integerfield), release_date (textfield), review (textfield). Setelah itu dilakukan migrasi dengan command `python manage.py makemigrations` dan `python manage.py migrate`.

Setelah proses migrasi, maka dibuat file JSON yang berisi array of objects. Setiap objek adalah film yang memiliki atribut models, pk, dan fields (berisi atribut sesuai dengan models.py). Terdapat 11 objek film pada file JSON. Lalu data di-load menggunakan command `python manage.py loaddata initial_mywatchlist_data.json`.

Pada views.py dibuat fungsi-fungsi yang akan menampilkan data sesuai dengan hasil return yakni HTML, JSON, dan XML. Path `/html` akan me-return file html yang akan ditampilkan kepada pengguna. Sedangkan XML dan JSON akan dilakukan serialisasi dengan parameter yang sesuai (XML atau JSON) agar data bisa tampil ke pengguna. Menu bonus juga diimplementasikan pada views.py yang akan ditampilkan pada path `/bonus`. Setelah semua fungsi dibuat, ditambahkan path pada urls.py dengan fungsi-fungsinya yang sesuai.

Setelah itu akan dilakukan deploy pada heroku dengan cukup hanya melakukan push dan re-run failed actions pada github karena sudah di-setup sebelumnya pada tugas 2. 

Akan juga dilakukan testing pada postman dan tests.py. Keduanya akan mengecek apakah pengaksesan semua path akan mereturn status code 200. Pada postman bisa dilakukan dengan melakukan GET pada path yang dituju. Sedangkan pada tests.py akan ditambahkan fungsi yang akan melakukan hal demikian. Fungsi akan memanfaatkan method self.client.get() dan membandingkan hasil dengan 200 melalui assertEqual(). Jika return status code adalah 200 maka semua test akan berhasil (passed).

## Screenshot Hasil GET di Postman
Screenshot Postman dalam mengakses /mywatchlist/html/
![Postman HTML](/images/postman-html.png)

Screenshot Postman dalam mengakses /mywatchlist/json/
![Postman JSON](/images/postman-json.png)

Screenshot Postman dalam mengakses /mywatchlist/xml/
![Postman XML](/images/postman-xml.png)