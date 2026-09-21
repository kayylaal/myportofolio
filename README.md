Nama : Kayla Kirana Ali Trimardhany \
NPM : 2506603854 \
Kelas : PBP A \
Hobi : Tidur \
Jurusan : Sistem Informasi

## MyPortofolio

Website portfolio saya yang dibuat dengan Django. Halaman utama berisi hero/profile, daftar Projects, dan Social Works. Datanya tidak di-hardcode di template, tapi disimpan di database sehingga bisa ditambah, diubah, dan dihapus lewat form. Data yang sama juga  disediakan dalam bentuk JSON beserta filter pencarian `?title=`.

Fitur yang sudah jalan:
* Projects: halaman list (`/projects/`, datanya diambil dari JSON lalu di-deserialize), tambah (`/projects/add/`), ubah (`/projects/<id>/edit/`), hapus (modal konfirmasi, POST), dan JSON (`/api/projects/`)
* Social Works: sama seperti di `/socialworks/`, tambah/ubah/hapus, JSON di `/api/socialworks/`, plus field `year` (Char/Text/URL/Integer)
* Halaman lain: `/` (profile), `/experiences/` (tampilan), `/admin/`. Semua halaman memakai `extends base.html` agar strukturnya konsisten.

Teknologi: Django 6.1, Python 3.13 (pakai `./env/bin/python`), SQLite untuk lokal dan PostgreSQL untuk produksi, WhiteNoise, python-dotenv.

Cara menjalankan:
1. Migrasi database: `./env/bin/python manage.py migrate`
2. Jalankan server: `./env/bin/python manage.py runserver`, lalu buka `http://127.0.0.1:8000/`
3. Cek kesehatan kode: `./env/bin/python manage.py check` dan `./env/bin/python manage.py test main`
4. Cek JSON via browser/Postman (harus 200 OK): `/api/projects/`, `/api/projects/?title=susun`, `/api/socialworks/`, `/api/socialworks/?title=aiesec`

### Tugas 1


1. Ya, saya menggunakan elemen semantik HTML5 yaitu `<section>` karena portofolio saya terdiri dari 3 section, yaitu hero/profile (yang berisi nama, foto, bio, dan links), lalu section projects (berisi cards project-project yang telah saya buat), dan socials/social works (yang berisi kegiatan sosial untuk masyarakat dan bumi yang pernah saya lsayakan). Penggunaan elemen semantik section sangat membantu saya, karena saya jadi dapat mengarahkan langsung ke tiap section dengan menunjuk id-nya saja. Selain itu, penulisan dan pembacaan kode juga jadi lebih mudah karena jadi terpisah dengan jelas dan dapat diubah-ubah tanpa khawatir tidak sengaja merusak kode section lain. Saya juga lumayan concern dengan aksesibilitas, jadi screen reader mudah mengenali struktur halaman.

   Saya juga memakai elemen semantik lainnya seperti `<header>` untuk navbar, `<nav>` untuk menu, `<main>` untuk isi, `<footer>` untuk footer, satu h1 tunggal untuk nama lengkap, serta alt di semua gambar untuk aksesibilitas. Saya tidak memakai `<article>`/`<aside>` karena websitenya bukan artikel atau konten sampingan, melainkan hanya satu portofolio.

   Jujur awalnya sempat salah, hero awalnya dua h1 (Kayla dan Ali kepisah kolom), ternyata setelah minta review ChatGPT itu membuat struktur heading tidak valid, jadi kugabung saja "Kayla" tetap h1 dengan aria-label nama lengkap, dan "Ali" jadi span dekoratif.

2. Jujur awalnya saya hanya memikirkan bagaimana tampilannya di desktop, dan saya lumayan idealis dan ingin lebih dekoratif dan lumayan ribet layout hero-nya (nama - foto - nama). Akhirnya saya sadar kalau saat dibikin responsive ke mobile jadi berantakan dan kacau. Jadinya saya minta bantuan AI untuk cari solusi, awalnya saya kasih prototype figma untuk mengganti layout mobile jadi berbeda, dan saya bertanya bagaimana solusi di dalam kodenya. Kata AI: "trik display: contents — kolom desktop "dipecah" supaya tiap isinya bisa ditempatkan manual lewat grid areas (Kayla gede di atas, Ali + foto berdampingan, tombol vertikal di kiri, bio dan tagline rata kanan di bawah). Di mobile yang diprioritaskan foto (tetap gede, nggak boleh kepotong — makanya rasionya dikunci) dan nama, tombol mengecil jadi kolom vertikal" dan saya setuju dengan solusi itu. Jadi saya coba implementasi kedua layout berbeda untuk mobile dan desktop untuk menyesuaikan. Untuk bagian lainnya tidak ada yang diubah.

3. Batasan yang saya rasakan adalah tidak boleh pakai JS, harus murni menggunakan HTML dan CSS. Tadinya saya ingin menambahkan progress scroll bar horizontal untuk section projects dan social works agar user tahu sudah sejauh apa. Saya juga ingin menambahkan kalau region atas dihover akan muncul navbarnya sendiri, dan navbar bisa hilang sendiri dengan animasi. Selain itu ada ide unik yang sempat saya coba tapi tidak jadi diimplementasikan juga karena keterbatasan, yaitu mengganti icon kursor dan membuat trace tiap menggerakan kursor. Mungkin ketiga itu akan saya implementasikan di tugas-tugas selanjutnya jika diizinkan menggunakan JS/library lain.

**Dokumentasi & AI Disclosure**

Tools yang dipakai: ChatGPT (untuk brainstorming & metaprompting) dan OpenCode (untuk melsayakan kode repetitif dan terlalu rumit)

Strategi prompting: awalnya saya mencari-cari sendiri dulu di sosial media (karena saya banyak menyimpan referensi-referensi untuk website portfolio), YouTube, dan blog tutorial soal cara bikin carousel horizontal, cara positioning pakai grid/flex, dan contoh portofolio orang dari Pinterest. Kalau tidak menemukan tutorial yang pas atau buntu (saat hero hancur pas dibuka di HP), baru saya tanya AI dengan screenshot + pertanyaan menanyakan solusi + kalau masih bingung, minta kode referensinya

Bagian spesifik yang dibantu AI: cara membuat horizontal carousel dan membuat kontennya dapat di-scroll, cara mengatur positioning beberapa elemen agar sesuai dengan desain yang dibuat, cara membuat layout desktop menjadi responsive di mobile ketika layout awal hancur, mencari solusi ketika terdapat masalah pada spacing, alignment, atau ukuran elemen tertentu.

Keterbatasan AI + perbaikan manual: saat membuat section hero, saya punya standar yang sangat spesifik, dan AI tidak bisa mengetahui itu secara pasti, jadi saya coba untuk cari saran bagaimana membagi-baginya, lalu positioningnya saya buat sendiri (coba nilai padding-top, margin negatif, dan clamp() font-size). Lesson learned: AI cepat dan membantu dalam bikin kerangka dan pola berulang, tapi untuk visual taste yang presisi, lebih tepat kode sendiri dengan mata manusia.

Prompt log (gambaran besar):

1. Aku mau bikin bagian social works yang bisa discroll tapi belakangnya tetap ada tali panjang gitu. Kalau pakai HTML dan CSS sederhana, struktur dan CSS-nya sebaiknya gimana?
2. Aku mau posisi heronya Kayla di kiri, foto di tengah, dan Ali di kanan. saya sudah punya HTML-nya. Gimana cara mengatur layout-nya dengan CSS Grid supaya posisinya sesuai?
3. Layout desktopku sudah seperti ini, tapi ketika dibuka di mobile posisinya berantakan. Kira-kira bagian CSS mana yang perlu diubah supaya tetap responsive?
4. Aku sudah coba beberapa cara tapi hasilnya belum sesuai. Bisa kasih beberapa alternatif cara untuk mengatur posisi elemen ini tanpa mengubah struktur HTML terlalu banyak?

### Tugas 2

1. Pertama, user membuka web portofolio, lalu portofolio/urls.py (urls proyek) menerima request lalu mencocokkan pattern "" men-forward ke app main. main/urls.py lalu mencocokkan experiences/ dan memanggil view show_experiences untuk menampilkan experiences. View lalu menjalankan Project.objects.all() dan SocialWork.objects.all() untuk ambil data dari database lewat model. Data lalu dimasukkan ke context dictionary (dikirim ke template experiences.html), lalu template merender HTML dengan django template language (for loop). HTML response lalu dikirim balik ke browser untuk dilihat user.

2. Data disimpan di model bukan hardcoded di template agar lebih maintainable (mudah diganti2), scalable (bisa menghapus/menambah data tanpa mengedit kode), resuable (data bisa dipakai di beberapa halaman), concern terpisah (kode logic terpisah dari template), dan memudahkan collaboration melalui admin page. Kalau hardcoded, setiap perubahan harus mengubah kode langsung sehingga rawan error dan sulit untuk dimaintain.

3. Perbedaan makemigrations dan migrate adalah makemigrations itu untuk membuat file migrasi (instruksi perubahan) tetapi tidak mengubah database, outputnya adalah file .py di folder migrations, sedangkan migrate untuk menjalankan file migrasi ke database sesuai instruksi, outputnya adalah tabel database yang sudah diupdate. 
Contoh yang saya alami adlah saat menambahkan model Project dan Social Works. 

**Dokumentasi & AI Disclosure**

Tools yang dipakai: ChatGPT (untuk brainstorming) dan OpenCode (untuk debug)

Strategi prompting: saya biasanya coba sendiri dulu di vscode sesuai penjelasan di website pbp, langsung lihat hasilnya di browser. Kalau hasilnya tidak sesuai atau error (misalnya overlay meluap dari foto, atau flip card tidak jalan di mobile), baru saya tanya AI dengan menjelaskan masalahnya + screenshot. Kalau masih bingung, saya minta alternatif solusi atau kode referensi.

Bagian spesifik yang dibantu AI: membuat flip card animation untuk social works pakai pure CSS, membuat unit test Django (3 kasus: URL + template, data muncul, empty state)

Keterbatasan AI + perbaikan manual: untuk di mobile, AI tidak memikirkan bahwa hover tidak berfungsi di touch device, jadi saya tambahkan sendiri interaksi agar bisa di-tap. Lesson learned: untuk detail visual dan aksesibilitas manusia, lebih tepat verifikasi sendiri dengan mata manusia.

Prompt log (gambaran besar):

Social works cards kalau di-hover kebalik kayak kartu flip, balik jadi putih polos #FCF9F1 dengan deskripsi warna abu.
Bikin unit test Django yang cover: URL akses + template tepat, data muncul di HTML, dan empty state muncul kalau data kosong.

### Tugas 3

1. Saya pakai `ModelForm` karena form-nya langsung nyambung ke model, jadi field, `max_length`, URL, dan validasinya ngikutin model tanpa ditulis ulang di HTML. Kalau bikin form manual, aturan di template dan di model bisa beda, terus validasi sama `save()` harus ditulis sendiri jadi rawan salah. Contoh yang saya alami adalah saat bikin `SocialWorkForm`, saya tinggal isi `fields = [title, description, photo, year]` lalu `form.is_valid()` dan `form.save()`. `{% csrf_token %}` wajib karena tiap POST dicek `CsrfViewMiddleware`, kalau tidak ada token request ditolak 403. Fungsinya biar form tidak bisa dikirim dari situs lain atas nama user yang lagi login (serangan CSRF).

2. JSON lebih disukai daripada XML karena penulisannya lebih ringkas (tidak banyak tag buka-tutup), jadi payload lebih kecil dan cepat dibaca. JSON juga langsung nyambung ke JavaScript (`JSON.parse`), gampang dipakai frontend dan mobile, tetap kebaca manusia, dan tool seperti Postman dan REST API sekarang umumnya pakai JSON.

3. Alurnya saat saya kembalikan data dalam bentuk JSON adalah request masuk ke view `get_socialworks_json`, lalu view ambil `SocialWork.objects.all()` dan filter `title__icontains` kalau ada `?title=`. Setelah itu `serializers.serialize("json", queryset)` mengubah queryset jadi string JSON, lalu dikirim lewat `HttpResponse(..., content_type="application/json")`. Untuk halaman webnya (`show_socialworks`), saya panggil fungsi JSON itu lalu `serializers.deserialize` supaya JSON berubah lagi jadi object model sebelum dikirim ke template. Serialisasi itu perlu karena object model Django tidak bisa langsung jadi JSON, masih berupa tipe Python dan relasi, jadi harus diubah dulu ke format standar yang bisa di-parse browser.

**Dokumentasi & AI Disclosure**

Tools yang dipakai: ChatGPT (untuk brainstorming) dan OpenCode (untuk debug)

Strategi prompting: saya coba tulis sendiri dulu di vscode mengikuti pola Projects yang sudah jalan di tutorial 3, langsung cek dengan `check`. Kalau error (misalnya `NoReverseMatch` atau `TemplateDoesNotExist`), baru saya tanya AI dengan copy error + screenshot. Kalau masih ragu soal kerapian, saya tanya apakah lebih baik disamakan saja atau dibuat terpisah.

Bagian spesifik yang dibantu AI: debug saat URL atau variabel template tidak cocok (misal `create_socialwork` vs `create_socialworks`, `thumbnail` vs `photo`).

Keterbatasan AI + perbaikan manual: AI sempat menyarankan class CSS baru (`socialwork-header`, dll), padahal CSS saya cuma punya class `project-*`. Jadi saya samakan saja class-nya dengan Project biar tidak redundan. 

Lesson learned: untuk beberapa masalah seperti efisiensi, kadang manusia lebih memiliki ide.

Prompt log (gambaran besar):

1. Apa class-nya samain aja sama Project biar nggak redundan dan tetap kepakai styling-nya?
2. Coba debug, `NoReverseMatch` untuk create/update SocialWork padahal URL sudah ada, kira-kira nama yang salah di mana?
3. Coba debug, halaman `/socialworks/` error `TemplateDoesNotExist`, file mana yang belum kebaca?
4. Tolong cek apakah ada kode yang salah/redundan?
