# Penjelasan Tugas 4

Aplikasi yang sudah di-deploy dapat diakses melalui tautan berikut:
http://beaston-tugas-2.herokuapp.com/todolist/ (butuh login terlebih dahulu)

Akun yang dibuat adalah:
1. username: penggunasatu | password: apakabar123
2. username: penggunadua | password: apakabar123

## Apa kegunaan {% csrf_token %} pada elemen `<form>`

`{% csrf_token %}` adalah sintaks yang disediakan oleh Django untuk menyediakan token yang berfungsi agar bisa terhindar dari serangan CSRF atau Cross Site Request Forgery. Tipe serangan ini terjadi ketika suatu website yang jahat mengandung link, button form, atau sebuah script JavaScript yang dibuat agar browser pengguna meminta request ke server yang bisa membuat perubahan pada server tersebut. Server akan beranggapan bahwa karena request diminta dengan cookies pengguna, maka pengguna tersebut benar-benar melakukan request, padahal kenyataannya tidak. Tanpa adanya tag tersebut, dengan mendapatkan cookie yang sama dengan pengguna, maka aktor jahat bisa berpura-pura seperti pengguna. (Sumber: https://docs.djangoproject.com/en/4.1/ref/csrf/ dan https://www.squarefree.com/securitytips/web-developers.html#CSRF)

## Apakah elemen `<form>` dapat dibuat secara manual?
Bisa. Sintaks `{{ form.as_table }}` adalah sintaks yang disediakan oleh django untuk menampilkan form sebagai table, dengan syarat bahwa sintaks tersebut terletak dalam tags `<table></table>`. Apabila kita ingin menampilkan form secara manual, maka kita harus membuat semua kolom input, label, dan button submit dengan name, type, value, dan labelnya masing-masing yang sesuai. 

## Proses alur data
Pengguna akan diminta untuk memasukkan data ke kolom form yang sesuai dan melakukan submit atas data tersebut. Setelah submisi dilakukan, maka server akan mengecek token CSRF. Proses submisi selanjutnya akan melalui proses pengecekan data terhadap atribut yang terdapat pada models. Lalu apabila sudah sesuai maka program akan melakukan proses migrasi data ke database. Berdasarkan models, data yang dimasukkan ke dalam database tidak hanya title dan description, melainkan juga user yang saat itu terlogged-in, dan date saat data di-submit. Setelah data sudah disimpan, maka `views.py` akan mengambil data-data yang terdapat di database dan di-filter berdasarkan user yang meng-submit-nya saja, lalu akan dilakukan render ke dalam template. Template lalu akan melakukan looping terhadap data ini, dan menampilkannya satu per satu yang sudah dimasukkan ke dalam format HTML agar bisa tampil dengan rapih kepada pengguna.

# Cara implementasi
1. Membuat aplikasi baru bernama todolist dengan startapp pada Command Prompt.
2. Menambahkan aplikasi tersebut pada `INSTALLED_APPS` di `settings.py` project_django.
2. Menambahkan path `todolist` ke dalam `urls.py` di project_django, dengan meng-include urls pada todolist.
3. Membuat field atribut yang sesuai pada `models.py`.
4. Membuat `views.py` untuk setiap fungsionalitas yang akan dilakukan program, seperti register, login, logout, halaman utama, dan halaman add task. Fungsi akan me-render response ke dalam template HTML masing-masing. Fungsionalitas Form dibuat dengan menyusun `forms.py` yang field-nya disesuaikan dengan `models.py`.
5. Membuat routing pada `urls.py` agar setiap path bisa diakses oleh pengguna.
6. Melakukan deploy aplikasi pada heroku.
7. Membuat 2 akun dan masing-masing akun menambahkan 3 dummy data pada aplikasi yang sudah di-deploy pada heroku.
