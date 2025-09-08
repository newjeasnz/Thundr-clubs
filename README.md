# THUNDR clubs
_Bring the Energy of Lightning to your Match_

Check out here: [THUNDR clubs Web](https://jessica-tandra-thundrclubs.pbp.cs.ui.ac.id/)

Nama: Jessica Tandra
NPM: 2406355445
Kelas: PBP - B 

## TUGAS 2 - PBP 2025/2026
Berikut adalah jawaban dari pertanyaan yang terdapat pada Tugas 2:

### Langkah Implementasi
**1. Membuat sebuah proyek Django baru.**
- Langkah pertama yaitu membuat direktori baru dengan nama thundr-clubs, kemudian dalam direktori tersebut buka _command prompt_ dan buat virtual environment dengan perintah `python -m venv env`. Nyalakan virtual environment tersebut dengan `env\Scripts\activate`.
- Selanjutnya dalam direktori yang sama, buat file `requirements.txt`, tambahkan dependencies dan lakukan instalasi.
- Terakhir, buat proyek django dengan perintah `django-admin startproject thundr_clubs .`. Hal ini dilakukan untuk membuat fondasi utama dalam mengembangkan aplikasi lebih lanjut.

**2. Membuat aplikasi dengan nama main pada proyek tersebut.**
- Setelah membuat proyek, kita harus membuat aplikasi baru bernama `main` dengan menjalankan perintah `python manage.py startapp main`. Perintah ini akan menghasilkan sebuah folder main yang berisi struktur dasar aplikasi Django. Aplikasi inilah yang nantinya digunakan untuk mengatur logika utama, mulai dari model, views, hingga routing dan template yang akan membentuk fitur-fitur pada website.

**3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**
- Tambahkan route pada berkas `urls.py` dalam direktori proyek yang bertujuan untuk menghubungkan aplikasi `main` dengan proyek utama, sehingga setiap request yang masuk ke alamat tertentu akan diarahkan ke routing pada aplikasi `main`. 

**4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut**
- Pada tahap ini, kita membuat sebuah model bernama `Product` di dalam berkas `models.py` pada aplikasi `main`. Model Product berperan sebagai representasi dari data produk, dengan sejumlah atribut seperti `name`, `price`, `description`, `thumbnail`, `category`, dan `is_featured`. Masing-masing atribut memiliki tipe data tertentu yang digunakan untuk menyimpan informasi produk ke dalam database.

**5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**
- Pada tahap ini, dibuat fungsi di dalam `views.py` yang bertugas membuat data berupa nama aplikasi, nama, serta kelas. Data tersebut dimasukkan ke dalam dictionary berupa `context`. Fungsi ini kemudian akan merender berkas template HTML, sehingga variabel dalam `context` dapat ditampilkan pada halaman web yang sesuai dengan template yang sudah dibuat.

**6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**
- Selanjutnya, kita perlu menambahkan route pada `urls.py` yang ada dalam aplikasi `main`. Routing ini berfungsi untuk memetakan URL ke fungsi yang ada dalam `views.py`. Saat pengguna mengakses halaman yang telah dibuat melalui URL yang sesuai, Django akan mengeksekusi fungsi yang sesuai di`views.py` dan menampilkan hasilnya menggunakan template HTML.

**7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
- Setelah aplikasi selesai dibuat, selanjutnya yaitu melakukan deployment ke PWS dengan cara mengunggah proyek ke server PWS dengan menjalankan perintah `add`, `commit`, dan `git push pws master`. Dengan demikian, aplikasi yang sebelumnya hanya dapat dijalankan di komputer lokal, sekarang dapat diakses melalui internet dengan URL tertentu.

**8. Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.**
- Setelah aplikasi berhasil di-deploy ke PWS. Selanjutnya adalah membuat file README.md yang berisi tautan menuju aplikasi yang sudah di-deploy di PWS, langkah-langkah impplementasi dan beberapa pertanyaan terkait Django.

### Bagan Alur Django


### Peran `settings.py`
melakukan konfigurasi, setelah melakukan migrasi akan ada satu file database (db.sqlite). object relational mapping

### Cara Kerja Migrasi Database

### Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

### Feedback untuk Asisten Dosen Tutorial 1