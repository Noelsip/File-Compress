# Compressor - Press File

Aplikasi desktop sederhana untuk mengompres file gambar (JPG/PNG) dan PDF dengan antarmuka grafis yang user-friendly.

## 📋 Deskripsi

Compressor adalah aplikasi Python berbasis GUI yang memungkinkan pengguna untuk mengurangi ukuran file gambar dan PDF dengan mudah. Program ini dilengkapi dengan berbagai opsi kualitas dan resize untuk memberikan kontrol penuh atas hasil kompresi.

## ✨ Fitur

- **Kompresi Gambar**: Mendukung format JPG, JPEG, dan PNG
- **Kompresi PDF**: Mengurangi ukuran file PDF dengan PyPDF2
- **Kontrol Kualitas**: Slider kualitas dari 10-100 untuk mengatur tingkat kompresi
- **Opsi Resize**: Pilihan untuk meresize gambar (50%, 75%, atau tanpa resize)
- **Preset Kualitas**: Tombol cepat untuk setting kualitas (Tinggi, Seimbang, Kompres Kuat)
- **Antarmuka Intuitif**: GUI yang mudah digunakan dengan Tkinter
- **Info File**: Menampilkan informasi ukuran file sebelum dan sesudah kompresi

## 🛠️ Instalasi

### Prasyarat
- Python 3.7 atau versi lebih baru
- pip (Python package installer)

### Langkah Instalasi

1. **Clone atau download repository ini:**
   ```bash
   git clone <repository-url>
   cd Press-File
   ```

2. **Install dependencies yang diperlukan:**
   ```bash
   pip install -r requirements.txt
   ```

   Atau install secara manual:
   ```bash
   pip install pillow pypdf2 pymupdf
   ```

3. **Jalankan aplikasi:**
   ```bash
   python main.py
   ```

## 📖 Cara Penggunaan

### Langkah-langkah Menggunakan Aplikasi:

1. **Jalankan Program**
   ```bash
   python main.py
   ```

2. **Pilih File**
   - Klik tombol "📁 Pilih File"
   - Pilih file gambar (JPG/PNG) atau PDF yang ingin dikompres
   - Aplikasi akan menampilkan informasi ukuran file

3. **Atur Kualitas Kompresi**
   - Gunakan slider untuk mengatur kualitas (10-100)
   - Atau gunakan preset yang tersedia:
     - **Kualitas Tinggi (85)**: Untuk hasil terbaik dengan kompresi ringan
     - **Seimbang (60)**: Keseimbangan antara ukuran dan kualitas
     - **Kompres Kuat (30)**: Untuk ukuran file minimal

4. **Pilih Opsi Resize (Opsional)**
   - **Tanpa Resize**: Mempertahankan ukuran asli
   - **75% Ukuran**: Mengurangi dimensi menjadi 75%
   - **50% Ukuran**: Mengurangi dimensi menjadi 50%

5. **Kompres File**
   - Klik tombol "🗜️ KOMPRES FILE"
   - Pilih lokasi dan nama file output
   - Tunggu proses kompresi selesai

6. **Lihat Hasil**
   - Aplikasi akan menampilkan informasi hasil kompresi
   - File baru akan tersimpan dengan suffix "_compressed"

## 🎯 Tips Penggunaan

### Untuk Hasil Optimal:

- **File Gambar Besar (>5MB)**: Gunakan kualitas 30-50 + resize 50%
- **Foto untuk Web**: Kualitas 60-70 sudah cukup
- **Arsip/Backup**: Kualitas 80-90 untuk menjaga detail
- **PDF Dokumen**: Program akan otomatis mengoptimalkan

### Panduan Kualitas:

| Kualitas | Penggunaan | Keterangan |
|----------|------------|------------|
| 80-100   | Foto penting, cetak | Kualitas tinggi, ukuran besar |
| 60-79    | Web, email | Seimbang antara kualitas dan ukuran |
| 40-59    | Sharing cepat | Kompresi sedang |
| 20-39    | Ukuran minimal | Kualitas rendah tapi ukuran kecil |
| 10-19    | Ekstrem | Hanya untuk kebutuhan khusus |

## 📁 Struktur File

```
Press-File/
├── main.py              # File utama aplikasi
├── requirements.txt     # Dependencies Python
└── README.md           # Dokumentasi ini
```

## 🔧 Dependencies

- **Pillow (PIL)**: Library untuk manipulasi gambar
- **PyPDF2**: Library untuk manipulasi file PDF
- **PyMuPDF**: Library tambahan untuk kompresi PDF yang lebih baik (opsional)
- **Tkinter**: GUI toolkit (built-in Python)

## ⚠️ Catatan Penting

- **Backup File Asli**: Selalu simpan copy file asli sebelum kompresi
- **Kualitas Rendah**: Setting kualitas di bawah 30 dapat merusak gambar
- **Format PNG**: Kompresi PNG terbatas dibanding JPG
- **File Besar**: Proses kompresi file besar membutuhkan waktu

## 🐛 Troubleshooting

### Error Umum:

1. **"Gagal mengompres gambar"**
   - Pastikan file tidak corrupt
   - Cek format file yang didukung

2. **"Tipe file tidak didukung"**
   - Program hanya mendukung JPG, PNG, dan PDF

3. **Library tidak ditemukan**
   - Install ulang dependencies: `pip install -r requirements.txt`

## 🤝 Kontribusi

Jika ingin berkontribusi pada proyek ini:
1. Fork repository
2. Buat branch fitur baru
3. Commit perubahan
4. Push ke branch
5. Buat Pull Request

## 📄 Lisensi

Proyek ini dibuat untuk tujuan edukasi dan penggunaan personal.

## 📞 Kontak

Jika ada pertanyaan atau masalah, silakan buat issue di repository ini.

---

**Selamat menggunakan File Compressor! 🚀**