# THUNDR clubs
_Bring the Energy of Lightning to your Match_

Check out here: [THUNDR clubs Web](https://jessica-tandra-thundrclubs.pbp.cs.ui.ac.id/)

Nama      : Jessica Tandra  
NPM       : 2406355445  
Kelas     : PBP B  

### Archive Tugas
- [Tugas 2 - PBP 2025/2026](https://github.com/newjeasnz/Thundr-clubs/wiki/TUGAS-2-%E2%80%90-PBP-2025-2026)
- [Tugas 3 - PBP 2025/2026](https://github.com/newjeasnz/Thundr-clubs/wiki/TUGAS-3-%E2%80%90-PBP-2025-2026)
- [Tugas 4 - PBP 2025/2026](https://github.com/newjeasnz/Thundr-clubs/wiki/TUGAS-4-%E2%80%90-PBP-2025-2026)
- [Tugas 5 - PBP 2025/2026](https://github.com/newjeasnz/Thundr-clubs/wiki/TUGAS-5-%E2%80%90-PBP-2025-2026)

---

## TUGAS 6 - PBP 2025/2026
Berikut adalah jawaban dari pertanyaan yang terdapat pada Tugas 6:

### Apa perbedaan antara synchronous request dan asynchronous request?
Synchronous request dan asynchronous request berbeda pada cara program menunggu respons dari server. Pada synchronous request, program akan berhenti dan menunggu sampai server mengirimkan balasan sebelum melanjutkan eksekusi kode berikutnya. Artinya, eksekusi kode bersifat berurutan, sehingga jika respons server lambat, seluruh program akan terblokir sampai data diterima. Sebaliknya, asynchronous request memungkinkan program untuk tetap berjalan tanpa menunggu respons server. Saat request dikirim, program dapat mengeksekusi kode lain, dan ketika balasan dari server sudah siap, sebuah callback atau mekanisme penanganan tertentu akan dijalankan. Dengan demikian, asynchronous request lebih efisien dalam mengelola operasi yang memerlukan waktu tunggu, seperti pengambilan data dari API atau operasi I/O, karena tidak membuat program berhenti sementara menunggu server merespons.

### Bagaimana AJAX bekerja di Django (alur request–response)?
1. **Event di browser**
Pengguna melakukan aksi di halaman web, misalnya menekan tombol atau mengisi form. JavaScript menangkap event ini dan memicu request AJAX.

2. **Mengirim request AJAX**
JavaScript membuat request HTTP (biasanya GET atau POST) ke server Django tanpa me-reload halaman. Data tambahan bisa dikirim sebagai query parameter atau body request.

3. **Django menerima request**
Request masuk ke Django melalui URL routing (urls.py) yang mengarah ke view tertentu. View ini bisa berupa fungsi atau class-based view.

4. **Memproses request di server**
Di view, Django memproses data yang dikirim, misalnya mengambil data dari database, melakukan perhitungan, atau validasi input.

5. **Membuat response**
Setelah diproses, view Django mengembalikan response, biasanya berupa JSON (JsonResponse) karena format ini mudah diolah oleh JavaScript di sisi client.

6. **JavaScript menerima response**
Browser menerima response JSON tanpa me-reload halaman. JavaScript kemudian mem-parsing data ini dan memperbarui elemen HTML sesuai kebutuhan, misalnya menampilkan data baru atau menandai status tertentu. Terakhir, pengguna melihat hasil update di halaman secara real-time, sementara halaman tetap berada di posisi yang sama, tanpa reload penuh.

### Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Keuntungan menggunakan AJAX dibandingkan render biasa di Django terletak pada efisiensi dan pengalaman pengguna. Dengan render biasa, setiap kali halaman perlu diperbarui, browser melakukan request penuh ke server, memuat ulang seluruh halaman, dan menampilkan kembali semua konten. Hal ini bisa terasa lambat dan kurang responsif, terutama jika hanya sebagian kecil konten yang berubah.

Sedangkan dengan AJAX, hanya data yang dibutuhkan yang dikirim dan diterima dari server, biasanya dalam format JSON, tanpa me-reload seluruh halaman. Ini membuat interaksi menjadi lebih cepat dan halus karena pengguna tetap berada pada halaman yang sama, sementara konten tertentu diperbarui secara real-time. Selain itu, AJAX memungkinkan interaksi yang lebih dinamis, seperti validasi form, filter data, atau update tabel secara langsung, sehingga pengalaman pengguna terasa lebih responsif dan modern.

### Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Untuk memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django, ada beberapa hal penting yang harus diperhatikan. 
1. Gunakan HTTPS agar data yang dikirim, termasuk username dan password, terenkripsi saat berpindah dari browser ke server. Ini mencegah penyadapan data sensitif.
2. Aktifkan CSRF protection. Django memiliki mekanisme CSRF token untuk mencegah serangan cross-site request forgery. Saat menggunakan AJAX, pastikan token CSRF dikirim bersama request POST. Biasanya, token ini diambil dari cookie csrftoken dan disertakan di header request.
3. Validasi input di server. Jangan mengandalkan validasi di sisi client saja karena bisa dimanipulasi. Pastikan Django memeriksa username, email, password, dan aturan keamanan lain sebelum membuat user baru atau memproses login.
4. Batasi percobaan login untuk mencegah brute-force attack. Misalnya, blokir IP atau akun sementara setelah beberapa kali percobaan login gagal.
5. Hindari menampilkan pesan terlalu detail pada error login. Misalnya, jangan bilang “password salah” atau “username tidak ditemukan” secara spesifik karena bisa membantu pihak ketiga menebak akun.

Dengan kombinasi HTTPS, CSRF protection, validasi server-side, pembatasan percobaan login, dan handling error yang aman, fitur Login dan Register berbasis AJAX tetap aman digunakan.

### Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
AJAX secara signifikan meningkatkan pengalaman pengguna pada website karena memungkinkan interaksi yang lebih cepat dan responsif. Dengan AJAX, halaman tidak perlu di-reload penuh setiap kali pengguna melakukan aksi, sehingga perubahan konten bisa ditampilkan secara real-time. Misalnya, saat mengisi form, memfilter data, atau memuat komentar baru, pengguna dapat melihat hasilnya langsung tanpa menunggu refresh halaman. Hal ini membuat website terasa lebih halus, modern, dan interaktif, serta mengurangi waktu tunggu yang bisa membuat pengguna frustrasi. Selain itu, AJAX juga memungkinkan pengelolaan data secara dinamis, sehingga pengguna dapat melakukan beberapa aksi sekaligus tanpa kehilangan konteks halaman yang sedang digunakan.