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

---

## TUGAS 5 - PBP 2025/2026
Berikut adalah jawaban dari pertanyaan yang terdapat pada Tugas 5:

### Urutan prioritas pengambilan CSS selector
Jika suatu elemen HTML memiliki beberapa CSS selector yang mengaturnya, maka browser akan menentukan gaya mana yang digunakan berdasarkan specificity (tingkat kekhususan) dan urutan deklarasi. Urutan prioritasnya adalah sebagai berikut:
1. **Inline Style**. Contoh: `<p style="color: red;">Teks ini merah</p>` memiliki prioritas tertinggi
2. **ID selector** (#id). Contoh: `#judul { color: blue; }`. 
3. **Class selector**, **pseudo-class**, dan **attribute selector**
    Contoh:
    ```css
    .teks { color: green; }         /* class */
    p:hover { color: orange; }      /* pseudo-class */
    input[type="text"] { ... }      /* attribute selector */
    ```
4. **Tag / element selector**. Contoh: `p { color: black; }`
5. **Important rule** (!important) dapat mengesampingkan semua urutan di atas dan memberikan prioritas tertinggi untuk suatu property. Contoh:
    ```html
    <div id="header" class="menu">Title</div>
    ```
    ```css
    #header { color: blue; }
    .menu { color: green !important; }
    div { color: red; }
    ```
    teks akan berwarna hijau, karena aturan .menu memiliki !important, sehingga mengalahkan selector #header meskipun ID lebih spesifik.

### Mengapa responsive design menjadi konsep yang penting? Berikan contoh aplikasi dan jelaskan
Responsive design penting karena memungkinkan tampilan website beradaptasi secara otomatis dengan berbagai ukuran layar (desktop, tablet, maupun smartphone). Dengan responsive design, pengguna akan mendapatkan pengalaman yang konsisten dan nyaman tanpa harus melakukan zoom atau scroll horizontal.
Selain itu, responsive design juga meningkatkan aksesibilitas, user engagement, dan peringkat SEO, karena Google lebih memprioritaskan website yang mobile-friendly.

**Contoh Aplikasi yang sudah menerapkan Responsive Design:**
- Google: Halaman pencarian Google otomatis menyesuaikan layout dan ukuran font sesuai lebar layar.
- Youtube: Video, kolom komentar, dan rekomendasi otomatis berpindah posisi jika layar diperkecil.

**Contoh Aplikasi yang belum menerapkan Responsive Design:**
- SIAK NG (academic.cs.ui.ac.id): Hanya sesuai untuk tampilan dekstop. Saat dibuka lewat HP, layout-nya melebar sehingga pengguna harus scroll ke samping atau zoom in/out untuk membaca isi.
![Image](https://github.com/user-attachments/assets/6a17026c-d4ef-4b54-a6ef-8172b3f38ed5)

### Perbedaan margin, border, dan padding, serta bagaimana pengimplementasiannya?
1. **Padding**
Memberi jarak antara konten elemen dan batas (border) elemen itu sendiri. Implementasi: 
```css
div {
  padding: 20px;
}
```
2. **Border**
Garis pembatas di antara padding dan margin, mengelilingi elemen (seperti bingkai di luar padding). Implementasi:
```css
div {
  border: 2px solid black;
}
```
3. **Margin**
Memberi jarak antara elemen tersebut dengan elemen lain di sekitarnya (ruang kosong di luar border elemen). Implementasi:
```css
div {
  margin: 15px;
}
```
**Ilustrasi Box Model:**
![image](https://github.com/user-attachments/assets/44220ac6-0279-4d66-954b-ef511837a854")

### Konsep flex box dan grid layout
1. **Flexbox**
Flexbox adalah sistem layout 1 dimensi, yang berfungsi untuk mengatur tata letak elemen secara fleksibel dalam satu baris atau satu kolom. Elemen-elemen di dalam container fleksibel ini akan otomatis menyesuaikan ukuran dan posisi berdasarkan ruang yang tersedia.

**Kegunaan Flexbox:**
- Meratakan elemen secara horizontal atau vertikal dengan mudah.
- Mengatur jarak antar elemen tanpa banyak perhitungan manual.
- Cocok untuk layout sederhana seperti navbar, tombol-tombol dalam baris, atau card yang berjejer.

**Contoh penggunaan:**
```html
<div style="display: flex; justify-content: center; gap: 10px;">
  <div style="background: lightblue; padding: 10px;">1</div>
  <div style="background: lightgreen; padding: 10px;">2</div>
  <div style="background: lightcoral; padding: 10px;">3</div>
</div>

```

2. **CSS Grid Layout**
Grid layout adalah sistem layout 2 dimensi, yang memungkinkan kita untuk mengatur elemen dalam baris dan kolom secara bersamaan. Dengan grid, kita bisa membuat struktur layout yang kompleks seperti halaman web utama dengan sidebar, header, dan konten utama.

**Kegunaan Grid Layout:**
- Membuat layout halaman yang rapi dan responsif.
- Cocok untuk struktur besar seperti tampilan dashboard, galeri gambar, atau tampilan e-commerce
- Lebih mudah untuk membagi area dan menyusun elemen dalam grid.

**Contoh Penggunaan**
```html
<div style="display: grid; grid-template-columns: 1fr 2fr; gap: 10px;">
  <div style="background: lightblue; padding: 10px;">Sidebar</div>
  <div style="background: lightgreen; padding: 10px;">Konten utama</div>
</div>

```

---
# Langkah Pengimplementasian
## Implementasi Fungsi Edit dan Hapus
###  1. Buat fungsi pada `views.py` untuk edit dan hapus
```python
# Fungsi untuk mengedit product
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    
    context = {
        'form' : form
    }

    return render(request, "edit_product.html", context)
```

```python
# Fungsi untuk menghapus product
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```

### 2. Impor fungsi edit dan hapus ke dalam urls.py dan tambahkan path url nya
```python
from main.views import delete_product, edit_product
urlpatterns = [
    ...
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product')
]
```

### 3. Buat file template `edit_product.html` kemudian lakukan kustomisasi pada file tersebut
### 4. Munculkan tombol edit dan delete pada `main.html`
```html
     <a href="{% url 'main:show_news' news.id %}"><button>Read More</button></a>
     {% if user.is_authenticated and news.user == user %}
     <a href="{% url 'main:edit_news' news.pk %}">
         <button>
             Edit
         </button>
     </a>
     <a href="{% url 'main:delete_news' news.pk %}">
      <button>
          Delete
      </button>
  </a>
```

## Buat Navigation Bar yang responsif
### 1. Buat file template `navbar.html` pada main/templates dan kemudian lakukan kustomisasi sesuai dengan fitur yang diperlukan
### 2. Tautkan navbar tersebut ke dalam `main.html` dengan menggunakan tags include (`{% include 'navbar.html' %}`)
```html
{% extends 'base.html' %}
{% block content %}
{% include 'navbar.html' %}
...
{% endblock content%}
```

## Styling CSS
### 1. Hubungkan `global.css` dan script Tailwind ke `base.html`
### 2. Custom styling ke global.css
### 3. Styling pada Navbar
### 4. Styling halaman login, register, detail product, create product, edit product dengan css framework
### 5. Styling home dengan menambahkan card product
**Jika belum ada produk yang tersedia, tampilkan gambar dan tulisan yang sesuai**
yaitu dengan cara menambahkan no-product.png pada folder static/images. Kemudian modifikasi main.html untuk menghubungkan card_product.html dan no-product.png
