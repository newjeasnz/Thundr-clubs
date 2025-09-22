# THUNDR clubs
_Bring the Energy of Lightning to your Match_

Check out here: [THUNDR clubs Web](https://jessica-tandra-thundrclubs.pbp.cs.ui.ac.id/)

Nama      : Jessica Tandra  
NPM       : 2406355445  
Kelas     : PBP B  

### Archive Tugas
- [Tugas 2 - PBP 2025/2026](https://github.com/newjeasnz/Thundr-clubs/wiki/TUGAS-2-%E2%80%90-PBP-2025-2026)

---

## TUGAS 3 - PBP 2025/2026
Berikut adalah jawaban dari pertanyaan yang terdapat pada Tugas 3:

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery adalah proses fundamental yang memungkinkan sebuah platform berfungsi secara maksimal. Ia merupakan mekanisme yang memastikan data dapat berpindah secara aman dan efisien antara berbagai komponen, seperti database, server, dan antarmuka pengguna. Tanpa sistem ini, informasi tidak akan sampai ke pengguna atau layanan lain tepat waktu, sehingga mengganggu fungsionalitas, kinerja, dan pengalaman pengguna dari platform tersebut.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Meskipun memiliki beberapa kekurangan, JSON secara keseluruhan dianggap lebih baik dan lebih populer daripada XML karena tiga alasan utama, yaitu: sintaks yang lebih sederhana, ukuran file yang lebih kecil, dan kecepatan pemrosesan yang lebih tinggi.

- **Sederhana dan Ringkas**: Sintaks JSON yang minimalis jauh lebih mudah dibaca dan ditulis oleh manusia maupun mesin dibandingkan XML. Selain itu, JSON lebih ringkas Karena JSON tidak menggunakan tag pembuka dan penutup yang berlebihan seperti XML, sehingga ukuran filenya lebih kecil dan secara signifikan mengurangi penggunaan bandwidth dan mempercepat transfer data.

- **Kecepatan Pemrosesan**: Proses parsing (membaca dan mengurai) data JSON jauh lebih cepat daripada XML. Dalam aplikasi yang sering melakukan pertukaran data (seperti API), kecepatan ini sangat menentukan responsivitas dan pengalaman pengguna.

- **Integrasi Native** : Karena sintaksnya yang mirip dengan objek JavaScript, JSON dapat diolah secara native oleh JavaScript tanpa memerlukan library tambahan yang kompleks, menjadikannya lebih mudah diimplementasi dalam web.

Meskipun XML memiliki keunggulan dalam validasi skema dan dukungan namespace, JSON tetap dianggap lebih unggul dan lebih populer. Hal ini karena JSON menawarkan kecepatan, keringkasan, dan kemudahan implementasi yang sangat krusial, terutama untuk aplikasi web modern.


### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
`is_valid()` adalah method pada form Django yang berfungsi untuk melakukan validasi terhadap data yang dikirimkan oleh pengguna. Method ini memeriksa apakah data di dalam form (yang berasal dari `request.POST`) memenuhi semua aturan yang telah ditentukan di dalam `ProductForm`, seperti tipe data, batasan karakter, dan apakah semua field yang wajib diisi sudah terisi.

Jika semua data memenuhi aturan, `is_valid()` akan mengembalikan nilai `True` dan data akan diproses lebih lanjut (misalnya disimpan dalam database). Sebaliknya, jika ada satu atau lebih field yang datanya tidak valid, method ini akan mengembalikan nilai `False` dan memberikan pesan-pesan error yang relevan.

Method `is_valid()` adalah penjaga gerbang utama yang melindungi aplikasi dari data yang tidak diinginkan atau bahkan berbahaya. Method ini memastikan bahwa hanya data yang valid dan sesuai dengan aturan yang dapat disimpan ke dalam database. Tanpa validasi ini, keamanan aplikasi dan integritas data tidak akan terjamin.


### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` adalah mekanisme keamanan yang krusial di Django untuk melindungi form dari serangan CSRF (*Cross-Site Request Forgery*). `csrf_token` ini adalah sebuah nilai unik yang ditambahkan ke dalam setiap formulir. Fungsinya memastikan bahwa permintaan yang dikirim ke server benar-benar berasal dari formulir yang sah di situs kita, bukan dari situs lain yang berbahaya.

Secara singkat, proses serangan CSRF dimulai ketika pengguna yang sedang login di situs kita kemudian mengunjungi situs berbahaya milik penyerang. Situs berbahaya tersebut secara otomatis memaksa browser pengguna untuk mengirimkan request ke server kita. Karena browser pengguna secara otomatis menyertakan kredensial yang valid, dan tanpa token tersebut, server kita tidak bisa membedakan permintaan yang diterima berasal dari sumber yang sah. Alhasil, server memproses permintaan penyerang dan membiarkan mereka mengubah data pengguna atau melakukan tindakan lain yang dapat merugikan pengguna.

Berikut alur lebih lengkap dari proses penyerangan CSRF:
1. Pengguna login ke situs kita (misalnya, `ThundrClubs.com`). Browser pengguna sekarang memiliki session cookie yang membuktikan bahwa mereka sudah terotentikasi.
2. Penyerang membuat situs web berbahaya (misalnya, `situs-jahat.com`). Di situs ini, penyerang membuat formulir HTML tersembunyi yang secara otomatis mengirimkan permintaan ke URL di `ThundrClubs.com`, misalnya `ThundrClubs.com/add-to-cart/`.
3. Pengguna yang masih login di `ThundrClubs.com` mengunjungi `situs-jahat.com`.
4. Tanpa sepengetahuan pengguna, browser pengguna secara otomatis menjalankan formulir tersembunyi tersebut.
5. Tanpa adanya `csrf_token` untuk divalidasi, Django melihat permintaan ini sebagai permintaan sah yang berasal dari pengguna yang terotentikasi. Situs kita akan memprosesnya, menambahkan produk ke keranjang, mengubah data, atau melakukan tindakan lain tanpa sepengetahuan atau persetujuan pengguna.

----
### Langkah Pengimplementasian.
### 1. Tambahkan 4 fungsi `views` baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
**Langkah-langkah:**
1. **Pada `views.py`, tambahkan _import_ `HttpResponse` dan `Serializer`**
    ```python
    from django.http import HttpResponse
    from django.core import serializers
    ```

2. **Tambahkan 4 fungsi baru pada View untuk format JSON dan XML**
    - **View untuk melihat objek dalam format XML**
    ```python
    def show_xml(request):
        data = Product.objects.all()
        xml_data = serializers.serialize("xml", data)
        return HttpResponse(xml_data, content_type="application/xml")
    ```

    - **View untuk melihat objek dalam format JSON**
    ```python
    def show_json(request):
        data = Product.objects.all()
        json_data = serializers.serialize("json", data)
        return HttpResponse(json_data, content_type="application/json")
    ```

    - **View untuk melihat objek dalam format XML by ID**
    ```python
    def show_xml_id(request, id):
        data = Product.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", data)
        return HttpResponse(xml_data, content_type="application/xml")
    ```

    - **View untuk melihat objek dalam format JSON by ID**
    ```python
    def show_json_id(request, id):
        data = Product.objects.filter(pk=id)
        json_data = serializers.serialize("json", data)
        return HttpResponse(json_data, content_type="application/json")
    ```

### 2. Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 1.
**Langkah-langkah:**
1. **Pada `main/urls.py` _import_ fungsi yang sudah dibuat pada `views.py`**
    ```python
    from django.urls import path
    from main.views import show_main, show_json, show_xml, show_json_id, show_xml_id
    ```

2. **Tambahkan _path_ URL ke dalam `urlpatterns` untuk masing-masing views dalam format JSON dan XML**
    ```python
    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_id, name='show_xml_id'),
        path('json/<str:id>/', show_json_id, name='show_json_id'),
    ]

    ```

### 3. Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman `form`, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
**Langkah-langkah:**
1. **Buat berkas dan direktori baru `templates/base.html` dan isi berkas tersebut**
    ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {% block meta %} {% endblock meta %}
    </head>

    <body>
        {% block content %} {% endblock content %}
    </body>
    </html>
    ```

2. **Masukkan berkas `base.html` ke dalam `settings.py` pada variable TEMPLATES**
    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'], // di sini
            'APP_DIRS': True,
        }
    ]
    ```

3. **Ubah berkas `main.html` untuk membuat halaman utama yang memiliki tombol "Add" serta tombol "Detail" pada setiap data objek model**
    ```html
    {% extends 'base.html' %}
    {% block content %}
    <h1>{{ app_name }}</h1>

    <h4>Name: </h4>
    <p>{{ name }}</p> 
    <h4>Class: </h4>
    <p>{{ class }}</p>

    <a href="{% url 'main:create_product' %}">
    <button>+ Add Product</button>
    </a>

    <hr>

    {% if not product_list %}
    <p>Belum ada product yang tersedia.</p>
    {% else %}

    {% for product in product_list %}
    <div class="card">
        
        <div class="card-content">
            <h2 class="product-title">
                <a href="{%url 'main:show_detail_product' product.id %}"
                style="text-decoration: none; color: inherit;">
                {{ product.name }}
            </a>
        </h2>
        
        <div class="card-image">
            {% if product.thumbnail %}
                <img src="{{ product.thumbnail }}" alt="Thumbnail" width="150" height="100" style="object-fit: cover; border-radius: 8px;">
            {% else %}
                <div class="no-thumbnail">No Image Available</div>
            {% endif %}
        </div>

        <p><b>Price:</b> Rp {{ product.price }}</p>
            <p><b>Category:</b> {{ product.get_category_display }}</p>
            <p><b>Description:</b> {{ product.description }}</p>

            {% if product.is_featured %}
                <p class="featured">🌟 Featured Product </p>
            {% endif %}

            <a href="{% url 'main:show_detail_product' product.id %}">
                Detail
            </a>
        </div>
    </div>
    <br /><br />
    {% endfor %}

    {% endif %}
    {% endblock content %}
    ```


### 4. Membuat halaman `form` untuk menambahkan objek model pada app sebelumnya.
**Langkah-langkah:**
1. **Buat `main/forms.py` untuk model `Product` menggunakan `ModelForm`**
    ```python
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ['name', 'price', 'category', 'description', 'thumbnail', 'is_featured']
    ```

2. **Buat Function baru dalam View untuk Input Form**
    ```python
    from django.shortcuts import render, redirect, get_object_or_404
    from django.http import HttpResponse
    from django.core import serializers
    from main.models import Product
    from main.forms import ProductForm

    ...
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')
        
        context = {'form': form}
        return render(request, "create_product.html", context)
    ...
    ```

3. **Buat template HTML `create_product.html` sebagai halaman `form`**
    ```html
    {% extends 'base.html' %} 
    {% block content %}
    <p><a href="{% url 'main:show_main' %}"><button>← Back</button></a></p>
    <h1>Add Product</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add New Product" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```

4. **Tambahkan URL routing untuk Form di `urls.py`**
    ```python
    from django.urls import path
    from main.views import show_main, show_json, show_xml, show_json_id, show_xml_id, create_product, 

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product/', create_product, name='create_product'),
        ...
    ]
    ```

### 5. Membuat halaman yang menampilkan detail dari setiap data objek model.
**Langkah-langkah:**
1. **Buat Function baru dalam View untuk detail Product**
    ```python
    def show_detail_product(request, id):
        product = get_object_or_404(Product, pk=id)

        context = {
            'product': product
        }

        return render(request, "detail_product.html", context)
    ...
    ```

2. **Buat template HTML `detail_product.html` sebagai halaman yang menampilkan detail Product**
    ```html
    {% extends 'base.html' %}
    {% block content %}

    <p><a href="{% url 'main:show_main' %}"><button>← Back</button></a></p>

    <h1>{{ product.name }}</h1>

    {% if product.thumbnail %}
    <img src="{{ product.thumbnail }}" alt="Thumbnail" width="300">
    <br /><br />
    {% endif %}

    <p><b>Price:</b> Rp {{ product.price }}</p>
    <p><b>Category:</b> {{ product.get_category_display }}</p>
    <p><b>Description:</b> {{ product.description }}</p>

    {% if product.is_featured %}
        <p><b>🌟 Featured Product</b></p>
    {% endif %}

    {% endblock content %}
    ```

3. **Buat URL routing untuk detail Product di `urls.py`**
    ```python
    from main.views import show_main, show_json, show_xml, show_json_id, show_xml_id, create_product, show_detail_product

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product/', create_product, name='create_product'),
        path('product/<str:id>', show_detail_product, name='show_detail_product'),
        ...
    ]
    ```

----
### Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Pada tutorial 2, asisten dosen sudah sangat membantu dan terbuka terhadap pertanyaan kami yang ada selama sesi tutorial 2 berlangsung. Dokumen tutorialnya juga terstruktur dengan baik, dengan materi yang relevan dan praktis, sehingga sangat efektif untuk menguatkan pemahaman.

### Hasil API Call dengan Postman
**Format XML (All)**
![image](https://github.com/user-attachments/assets/c8822cf3-8da6-4c5d-8ee4-f1eb6c3398f8)

**Format JSON (All)**
![image](https://github.com/user-attachments/assets/291f619d-8b18-43ab-be63-17e2d6f7cf83)

**Format XML by ID**
![image](https://github.com/user-attachments/assets/59d177c0-4755-4560-9cb4-84ff90d5fbb5)

**Format JSON by ID**
![image](https://github.com/user-attachments/assets/392dbb94-f129-4444-b7ed-4d68b053480b)