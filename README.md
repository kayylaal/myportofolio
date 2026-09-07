Nama : Kayla Kirana Ali Trimardhany

NPM : 2506603854

Kelas : PBP A

Hobi : Tidur

Jurusan : Sistem Informasi

### Tugas 1

1. Ya, saya menggunakan eleme semantik HTML5 yaitu <section> karena portofolio saya terdiri dari 3 section, yaitu hero/profile (yang berisi nama, foto, bio, dan links), lalu section projects (berisi cards project2 yang telah saya buat), dan socials/social works (yang berisi kegiatan sosial untuk masyarakat dan bumi yang pernah saya lakukan). Penggunaan elemen semantik section sangat membantu saya, karena saya jadi dapat mengarahkan langsung ke tiap section dengan menunjuk id-nya saja. Selain itu, penulisan dan pembacaan kode juga jadi lebih mudah karena jadi terpisah dengan jelas dan dapat diubah2 tanpa khawait tidak sengaja merusak kode section lain. Saya juga lumayan concern dengan aksesibilitas, jadi screen reader mudah mengenali struktur halaman.

Saya juga memakai elemen semantik lainnya seperti <header> untuk navbar, <nav> untuk menu, <main> untuk isi, <footer> untuk footer, satu <h1> tunggal untuk nama lengkap, serta alt di semua gambar untuk aksesibilitas. Saya tidak memakai <article>/<aside> karena websitenya bukan artikel atau konten sampingan, melainkan hanya satu portofolio. 

Jujur awalnya sempat salah, hero awalnya dua <h1> (Kayla dan Ali kepisah kolom), ternyata setelah minta review ChatGPT itu membuat struktur heading tidak valid, jadi kugabung saja "Kayla" tetap <h1> dengan aria-label nama lengkap, dan "Ali" jadi span dekoratif. 

2. Jujur awalnya saya hanya memikirkan bagaimana tampilannya di desktop, dan saya lumayan idealis dan ingin lebih dekoratif dan lumayan ribet layout hero-nya (nama - foto - nama). Akhirnya saya sadar kalau saat dibikin responsive ke mobile jadi berantakan dan kacau. Jadinya saya minta bantuan AI untuk cari solusi, awalnya saya kasih prototype figma untuk mengganti layout mobile jadi berbeda, dan saya bertanya bagaimana solusi di dalam kodenya. Kata AI: "trik display: contents — kolom desktop "dipecah" supaya tiap isinya bisa ditempatkan manual lewat grid areas (Kayla gede di atas, Ali + foto berdampingan, tombol vertikal di kiri, bio dan tagline rata kanan di bawah). Di mobile yang diprioritaskan foto (tetap gede, nggak boleh kepotong — makanya rasionya dikunci) dan nama, tombol mengecil jadi kolom vertikal" dan saya setuju dengan solusi itu. Jadi saya coba implementasi kedua layout berbeda untuk mobile dan desktop untuk menyesuaikan. Untuk bagian lainnya tidak ada yang diubah.

3. Batasan yang saya rasakan adalah tidak boleh pakai JS, harus murni menggunakan HTML dan CSS. Tadinya saya ingin menambahkan progress scroll bar horizontal untuk section projects dan social works agar user tahu sudah sejauh apa. Saya juga ingin menambahkan kalau region atas dihover akan muncul navbarnya sendiri, dan navbar bisa hilang sendiri dengan animasi. Selain itu ada ide unik yang sempat saya coba tapi tidak jadi diimplementasikan juga karena keterbatasan, yaitu mengganti icon kursor dan membuat trace tiap menggerakan kursor. Mungkin ketiga itu akan saya implementasikan di tugas-tugas selanjutnya jika diizinkan menggunakan JS/library lain.

Tools yang dipakai: ChatGPT (untuk brainstorming & metaprompting) dan OpenCode (untuk melakukan kode repetitif dan terlalu rumit)
Strategi prompting: awalnya saya mencari2 sendiri dulu di sosial media (karena saya banyak menyimpan refernsi2 untuk website portfolio), YouTube, dan blog tutorial soal cara bikin carousel horizontal, cara positioning pakai grid/flex, dan contoh portofolio orang dari Pinterest. Kalau tidak menemukan tutorial yang pas atau buntu (saat hero hancur pas dibuka di HP), baru aku tanya AI dengan screenshot + pertanyaan menanyakan solusi + kalau masih bingung, minta kode refrensinya
Bagian spesifik yang dibantu AI: cara membuat horizontal carousel dan membuat kontennya dapat di-scroll, cara mengatur positioning beberapa elemen agar sesuai dengan desain yang dibuat, cara membuat layout desktop menjadi responsive di mobile ketika layout awal hancur, mencari solusi ketika terdapat masalah pada spacing, alignment, atau ukuran elemen tertentu.
Keterbatasan AI + perbaikan manual: saat membuat section hero, aku punya standar yang sangat spesifik, dan AI tidak bisa mengetahui itu secara pasti, jadi aku coba untuk cari saran bagaimana membagi2nya, lalu positioningnya aku buat sendiri (coba nilai padding-top, margin negatif, dan clamp() font-size) Lesson learned: AI cepat dan membantu dalam bikin kerangka dan pola berulang, tapi untuk visual taste yang presisi, lebih tepat kode sendiri dengan mata manusia.
Prompt log (gambaran besar):
1. Aku mau bikin bagian social works yang bisa discroll tapi belakangnya tetap ada tali panjang gitu. Kalau pakai HTML dan CSS sederhana, struktur dan CSS-nya sebaiknya gimana?
2. Aku mau posisi heronya Kayla di kiri, foto di tengah, dan Ali di kanan. Aku sudah punya HTML-nya. Gimana cara mengatur layout-nya dengan CSS Grid supaya posisinya sesuai?
3. Layout desktopku sudah seperti ini, tapi ketika dibuka di mobile posisinya berantakan. Kira-kira bagian CSS mana yang perlu diubah supaya tetap responsive?
4. Aku sudah coba beberapa cara tapi hasilnya belum sesuai. Bisa kasih beberapa alternatif cara untuk mengatur posisi elemen ini tanpa mengubah struktur HTML terlalu banyak?