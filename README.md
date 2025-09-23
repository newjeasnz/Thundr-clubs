# THUNDR clubs
_Bring the Energy of Lightning to your Match_

Check out here: [THUNDR clubs Web](https://jessica-tandra-thundrclubs.pbp.cs.ui.ac.id/)

Nama      : Jessica Tandra  
NPM       : 2406355445  
Kelas     : PBP B  

### Archive Tugas
- [Tugas 2 - PBP 2025/2026](https://github.com/newjeasnz/Thundr-clubs/wiki/TUGAS-2-%E2%80%90-PBP-2025-2026)
- [Tugas 3 - PBP 2025/2026](https://github.com/newjeasnz/Thundr-clubs/wiki/TUGAS-3-%E2%80%90-PBP-2025-2026)

---

## TUGAS 4 - PBP 2025/2026
Berikut adalah jawaban dari pertanyaan yang terdapat pada Tugas 4:

### Apa itu Django `AuthenticationForm`? Jelaskan juga kelebihan dan kekurangannya.
AuthenticationForm adalah form built-in yang disediakan Django di modul `django.contrib.auth.forms` untuk memfasilitasi proses login pengguna. Form ini menangani validasi username dan password, sehingga developer tidak perlu menulis validasi login secara manual.

Fungsi utama:
1. Memvalidasi apakah username dan password yang dimasukkan sesuai dengan data di database.
2. Memberikan pesan error otomatis jika login gagal (misalnya username tidak ada atau password salah).
3. Dapat langsung digunakan di view untuk login, atau dikustomisasi sesuai kebutuhan.

Kelebihan:
1. Mudah digunakan dan terintegrasi dengan Django
    Form ini sudah siap pakai untuk login dan bisa langsung bekerja dengan `login()` dan middleware `AuthenticationMiddleware`.
2. Validasi otomatis dan aman
    Memeriksa username dan password sesuai database, menggunakan hash password.
3. Dukungan pesan error yang jelas
    Feedback otomatis membantu user memahami alasan login gagal, misalnya password salah atau username tidak ada.

Kekurangan:
1. Kurang fleksibel untuk kebutuhan khusus
    Misal login menggunakan email, captcha, atau multi-factor authentication (2FA) memerlukan kustomisasi tambahan.
2. Tampilan terbatas -> Form ini hanya menangani logika validasi, tidak mencakup desain tampilan.
3. Validasi terbatas
    Hanya mengecek username dan password. Pengecekan lain seperti status user (misal banned, belum verifikasi email, atau role tertentu) harus ditambahkan secara manual.


### Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
- **Autentikasi:** Proses memastikan identitas seseorang (misalnya melalui password dan username). Dalam konteks web, ini biasanya berarti memastikan bahwa user yang mencoba mengakses aplikasi memang siapa yang dia klaim. 
    - Contoh: login dengan username & password. Django akan mengecek apakah username dan password cocok dengan yang tersimpan di database.

    **Implementasi di Django:**  
    Django memiliki modul built-in yaitu `django.contrib.auth`. yang menyediakan kerangka kerja lengkap untuk autentikasi dan otorisasi pengguna. Modul ini memungkinkan developer untuk mengelola login, logout, user, permission, dan grup tanpa harus membangun sistem keamanan dari nol. Fitur utama yang tersedia:  
        1. Model user (`django.contrib.auth.models.User`) → Menyimpan informasi identitas pengguna, seperti username, password, email, dsb  
        2. Login & logout (`django.contrib.auth.login()` dan `logout()`) 
            - Fungsi `login(request, user)` menyimpan sesi pengguna yang telah berhasil autentikasi.
            - Fungsi `logout(request)` menghapus informasi sesi, sehingga pengguna dianggap keluar (unauthenticated).  
        3. Form login (`AuthenticationForm`) → berfungsi memvalidasi username dan password dan memberikan error secara otomatis jika login gagal  
        4. Middleware (`AuthenticationMiddleware`) → Secara otomatis menambahkan objek `request.user` ke setiap request. Jika user sudah login, request.user berisi objek User dan jika belum, berisi AnonymousUser. Middleware menyediakan informasi user sehingga otorisasi bisa dilakukan di view atau template.  

- **Otorisasi:** Proses pemberian hak akses atau izin kepada pengguna yang telah terautentikasi, untuk melakukan tindakan tertentu atau mengakses sumber daya (resources) tertentu dalam sistem komputer sesuai dengan hak akses yang dimiliki.
    - Contoh: Dalam sebuah aplikasi web, pengguna yang login sebagai “Admin” bisa menghapus artikel, sedangkan pengguna “Member” hanya bisa membaca dan mengomentari artikel.

    **Implementasi di Django:**
    1. Django mengatur hak akses menggunakan permissions dan groups.
    2. Permissions bisa di-assign per model atau view tertentu.
    3. Django juga mendukung groups untuk mengelompokkan permission, misalnya group “Admin” atau “Editor”.
    4. Otorisasi biasanya dicek menggunakan:
        - Decorator `@login_required` → hanya pengguna yang login bisa mengakses view.
        - Decorator `@permission_required('app_name.permission_codename')` → memeriksa izin tertentu


### Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
1. **Cookies**  
Cookies adalah berkas data berukuran kecil yang disimpan pada sisi klien (browser) oleh server. Cookies kemudian akan dikirim kembali oleh browser pada setiap permintaan (request) berikutnya ke server yang sama. Dengan demikian, cookies berfungsi untuk mempertahankan informasi state di sisi klien.
- **Kelebihan cookies:**
    - Seluruh browser modern telah mendukung cookies tanpa perlu konfigurasi tambahan.
    - Cookies dapat diset untuk bertahan meskipun browser ditutup, sehingga berguna untuk menyimpan preferensi pengguna dalam jangka panjang.
    - Mengurangi beban server -> karena data disimpan di sisi klien, server tidak perlu menyimpan informasi state untuk setiap pengguna.

- **Kekurangan cookies:**
    - Ukuran terbatas –> cookies umumnya memiliki batas kapasitas sekitar 4 KB per domain.
    - Cookies disimpan di sisi klien sehingga rentan terhadap manipulasi dan serangan, seperti Cross-Site Scripting (XSS).
    - Overhead jaringan: cookies dikirim pada setiap permintaan HTTP, sehingga dapat meningkatkan ukuran request dan response.
    - Penyimpanan data penting seperti kata sandi dalam cookies sangat tidak disarankan.

2. **Session**  
Session adalah mekanisme penyimpanan state yang dikelola di sisi server. Pada session, klien hanya menyimpan sebuah pengenal (session ID), biasanya melalui cookie, sedangkan data state yang sesungguhnya tersimpan di server (misalnya dalam memori, file, atau basis data).
- **Kelebihan session:**  
    - Keamanan lebih tinggi
    - Mendukung penyimpanan data kompleks
    - Administrator atau aplikasi dapat mengatur, menghapus, maupun memperbarui data session secara langsung dari sisi server.

- **Kekurangan session:**  
    - Karena seluruh data dikelola oleh server, maka semakin banyak pengguna aktif akan semakin besar pula penggunaan basis data
    - Ketergantungan pada session ID, apabila session ID hilang maka state juga hilang
    - Tidak persisten secara default -> sebagian besar session berakhir ketika browser ditutup


### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Secara default, penggunaan cookies tidak sepenuhnya aman. Cookies pada dasarnya adalah data yang disimpan di sisi klien (browser) dan dikirim kembali ke server setiap kali melakukan request. Hal ini menimbulkan sejumlah potensi risiko, di antaranya:
1. **Pencurian cookies (Session Hijacking)**
Apabila cookies tidak dienkripsi atau tidak dikirim melalui koneksi aman (HTTPS), pihak ketiga dapat melakukan penyadapan (sniffing) dan mencuri cookies, yang kemudian dapat digunakan untuk mengambil alih sesi pengguna.
2. **Cross-Site Scripting (XSS)**
Jika aplikasi rentan terhadap XSS, penyerang dapat menyisipkan script berbahaya yang mengakses cookies pengguna dan mengirimkannya ke penyerang.
3. **Cross-Site Request Forgery (CSRF)**
Cookies secara otomatis dikirim dalam setiap request ke domain terkait, sehingga dapat dimanfaatkan untuk melakukan request berbahaya tanpa sepengetahuan pengguna.

Penanganan Cookies di Django:
1. Secure Flag (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`) -> memastikan cookies hanya dikirim melalui HTTPS.
2. HttpOnlyFlag (`SESSION_COOKIE_HTTPONLY`) -> mencegah akses cookies oleh JavaScript, sehingga lebih aman dari XSS.
3. SameSite Attribute (`SESSION_COOKIE_SAMESITE`, `CSRF_COOKIE_SAMESITE`) -> membatasi pengiriman cookies hanya untuk request dari domain yang sama, mengurangi risiko CSRF.
4. Session Framework -> Django hanya menyimpan session ID di cookies, sementara data sesi disimpan di server, sehingga data sensitif tidak terekspos.

---
# Langkah Pengimplementasian
### 1. Mengimplementasikan fungsi registrasi, login, dan logout
- **Fungsi Registrasi**
    - Buat form pada untuk pendaftaran pengguna baru dengan mengimport `UserCreationForm`.
    - Buat fungsi register pada `views.py` yang menangani form registrasi dan menyimpan akun pengguna ke database ketika data di-submit
    - Redirect pengguna ke halaman login setelah registrasi berhasil.
    ```python
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages

    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
    ```
    - Buat template baru sebagai tampilan form registrasi yaitu `register.html`
    - Impor fungsi register yang ada di `views.py` ke dalam `urls.py` dan tambahkan path url nya

- **Fungsi Login**
    - Buat autentikasi login dengan mengimport `authenticate`, `login`, dan `AuthenticationForm`
    - Tambahkan fungsi login_user pada `views.py`
    ```python
    from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
    from django.contrib.auth import authenticate, login
    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                    user = form.get_user()
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:show_main"))
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response

        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)
    ```
    - Buat template sebagai tampilan login user dengan membuat file `login.html`
    - Impor fungsi login_user yang ada di `views.py` ke dalam `urls.py` dan tambahkan path url nya

- **Fungsi Logout**
    - Buat autentikasi logout dengan mengimport `logout` dan kemudian tambahkan fungsi logout_user pada `views.py`
    ```python
    from django.contrib.auth import authenticate, login, logout
    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```
    - Tambahkan button logout pada halaman utama
    - Impor fungsi logout_user yang ada di `views.py` ke dalam `urls.py` dan tambahkan path url nya


### 2. Menghubungkan model Product dengan User.
-  Pada model `Product` tambahkan ForeignKey `User`, sehingga setiap produk yang dibuat dapat dikaitkan dengan pengguna yang membuat produk tersebut
    ```python
    from django.contrib.auth.models import User
    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ...
    ```

    - Buat file migrasi model
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

    - Pada `views.py`, modifikasi fungsi `create_product` dengan menggunakan `commit=False` agar field user dapat diisi dengan request.user sebelum objek disimpan. Selain itu, modifikasi fungsi  `show_main` dengan menambahkan filter berdasarkan query parameter (all atau my).

### 3. Menampilkan detail informasi pengguna yang sedang logged in
- Pada halaman utama, tampilkan detail informasi pengguna yang sedang logged in
    - Pastikan view show_main dan show_detail_product menggunakan `@login_required` untuk memastikan hanya pengguna yang sudah login yang bisa mengakses halaman tersebut
    - Di view, ambil data pengguna yang sedang login dengan `request.user`
    ```python
    def show_main(request):
        filter_type = request.GET.get("filter", "all")
        if filter_type == "all":
            products = Product.objects.all()
        else:
            products = Product.objects.filter(user=request.user)
            
        context = {
            'app_name': 'THUNDR clubs',
            'name': request.user.username,
        ...}
    ```
    - Di template `main.html`, tampilkan informasi pengguna
    ```html
    <h4>Name: </h4>
    <p>{{ name }}</p> 
    ```

### 4. Menerapkan Cookies untuk Last Login
- Django secara otomatis menyimpan waktu terakhir pengguna login di field `last_login` di model `User`.
    - Import `HttpResponseRedirect`, `reverse`, dan `datetime` pada `views.py`
    - Modifikasi fungsi login_user untuk menyimpan cookie yang menyimpan timestamp terakhir login
    ```python
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    ...
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```
    - pada `show_main`, tambahkan `'last_login': request.COOKIES['last_login']` ke dalam variabel context
    - Hapus cookie last_login setelah melakukan logout dengan mengubah `logout_user`.
    - Di template, tampilkan waktu login terakhir
    ```html
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ```

### 5. Membuat Dua Akun Pengguna dengan Dummy Data
Saya membuat dua akun berbeda dengan username jessica dan tandra. Masing2 akun memiliki 3 produk:
- username jessica  
![my product](https://github.com/user-attachments/assets/15ee0d4c-45b7-402a-9a9c-f1af206cd476)  
![my product](https://github.com/user-attachments/assets/1c24e391-c71b-4134-b8b2-19a69cbcd7d2)  
![detail](https://github.com/user-attachments/assets/5ee2c0c4-9c9a-477b-9b5c-63a7a5e53876)  

- username tandra  
![my product](https://github.com/user-attachments/assets/01263a1e-d75c-4a68-8baf-ae48fa7ec608)  
![my product](https://github.com/user-attachments/assets/3a4d7d24-eadd-4255-87a4-25ccbbf973f5)  
![detail](https://github.com/user-attachments/assets/6ef39cc4-ba77-4f11-87ea-492908e46b90)  