# THUNDR clubs
_Bring the Energy of Lightning to your Match_

Check out here: [THUNDR clubs Web](https://jessica-tandra-thundrclubs.pbp.cs.ui.ac.id/)

Nama      : Jessica Tandra  
NPM       : 2406355445  
Kelas     : PBP B  

---

## TUGAS 2 - PBP 2025/2026
Berikut adalah jawaban dari pertanyaan yang terdapat pada Tugas 2:

### 🔍 Langkah Implementasi
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


### 📊 Bagan Alur Django
![Django Flows](https://github.com/user-attachments/assets/0f1ae51b-d71e-4ac3-a9bb-35b9f0b476a2)

Bagan alur request pada aplikasi web Django dimulai dari pengguna mengakses URL tertentu melalui browser, kemudian HTTP request dikirimkan melalui internet menuju server. Request tersebut diterima oleh server Django yang dijalankan melalui `manage.py`. Selanjutnya, `urls.py` berfungsi untuk memetakan pola URL yang diminta dan meneruskannya ke fungsi atau class yang sesuai di `views.py`. Di dalam `views.py`, request akan diproses sesuai logika aplikasi. Jika dibutuhkan, view akan berinteraksi dengan `models.py` untuk membaca maupun menyimpan data pada database. Model bertugas mengatur dan mengelola data aplikasi dengan mendefinisikan struktur tabel dalam database melalui class dan atribut.

Setelah data selesai diolah, hasilnya akan digabungkan dengan template HTML yang mengatur tampilan halaman. Proses ini menghasilkan sebuah halaman web yang sudah dirender secara utuh. Terakhir, Django mengirimkan HTTP response berisi halaman tersebut kembali ke browser, sehingga pengguna dapat melihat hasilnya di layar.

Singkatnya, alur Django adalah:  
Pengguna → Request → urls.py → views.py → models.py + DB → Template HTML → Response → Pengguna.  


### ⚙️ Peran `settings.py`
Dalam proyek Django, `settings.py` berperan sebagai pusat **konfigurasi utama** yang mengatur berbagai aspek aplikasi. Misalnya, ketika membuat aplikasi baru bernama `main`, aplikasi tersebut harus didaftarkan pada bagian `INSTALLED_APPS` di dalam berkas `settings.py` agar dapat dikenali dan dijalankan oleh proyek. File ini menyimpan berbagai pengaturan penting, seperti konfigurasi database, daftar aplikasi yang digunakan (INSTALLED_APPS), middleware, pengaturan keamanan (misalnya SECRET_KEY, DEBUG, dan ALLOWED_HOSTS), hingga pengaturan internasionalsasi seperti bahasa dan zona waktu.

Dengan kata lain, `settings.py` adalah inti dari setiap proyek Django, tempat developer mengatur lingkungan proyek sesuai kebutuhan, baik untuk tahap pengembangan maupun produksi. Karena semua komponen Django merujuk pada file ini, perubahan yang dilakukan di settings.py akan langsung memengaruhi perilaku seluruh aplikasi.   


### 📲 Cara Kerja Migrasi Database
Migrasi database di Django bekerja sebagai mekanisme untuk mengubah struktur tabel basis data sesuai dengan perubahan model yang didefinisikan pada kode program. Saat developer membuat atau mengubah model di `models.py`, perubahan tersebut tidak langsung tercermin di database. Untuk menerapkannya digunakan dua langkah utama:
1. `python manage.py makemigrations` -> membuat berkas migrasi skema model sebelum diaplikasikan ke dalam database.
2. `python manage.py migrate` -> menerapkan skema model yang telah dibuat ke dalam database Django lokal.  


### 🤔 Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak karena sifatnya yang batteries included, sehingga sudah menyediakan banyak fitur bawaan untuk mempercepat proses pengembangan. Framework ini juga menggunakan arsitektur Model-View-Template (MVT) yang terstruktur, sehingga pemula dapat dengan mudah memahami konsep penting seperti routing, templating, dan manajemen database tanpa perlu membangun semuanya secara manual.

Selain itu, Django dibangun dengan Python, bahasa yang sederhana dan familiar bagi banyak pemula, sehingga proses belajar terasa lebih ringan. Dokumentasi yang rapi dan komunitas yang besar juga menjadi keunggulan penting, karena memudahkan siapa pun menemukan panduan maupun solusi ketika menghadapi kesulitan. Dengan kombinasi ini, Django menjadi pilihan ideal sebagai framework pengenalan dalam dunia pengembangan perangkat lunak.  


### 👩‍💻 Feedback untuk Asisten Dosen Tutorial 1
Pada sesi Tutorial 1, asisten dosen yang mendampingi sangat membantu. Beliau terbuka terhadap setiap pertanyaan, serta aktif membimbing mahasiswa dalam menyelesaikan permasalahan yang ditemui. Selain itu, dokumen Tutorial 1 yang disusun juga sudah sangat baik. Langkah-langkahnya lengkap, runtut, dan rinci, disertai penjelasan di setiap tahap sehingga mudah dipahami. Bagi saya, dokumen tersebut sangat memudahkan untuk belajar pembuatan web dari nol karena alurnya jelas dan terstruktur. Secara keseluruhan, tutorial ini memberikan pengalaman belajar yang positif dan bermanfaat.