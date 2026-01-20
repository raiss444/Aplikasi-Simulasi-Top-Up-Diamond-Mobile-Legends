# 🛒 Aplikasi Simulasi Top Up Diamond Mobile Legends

## 📖 Deskripsi
Aplikasi desktop berbasis **Python (PyQt6)** untuk simulasi top-up diamond Mobile Legends.  
Aplikasi ini dibuat sebagai proyek akademik dengan tujuan memberikan pengalaman simulasi transaksi yang realistis, interaktif, dan edukatif.

### ✨ Fitur Utama
- Validasi **User ID** dengan format `12345678(1234)`
- Pilihan paket diamond dengan harga diskon, bonus, dan reward
- Metode pembayaran interaktif (Dana, Ovo, Gopay, Qris)
- Popup checkout dengan detail harga + pajak 11%
- Penyimpanan transaksi melalui fungsi `tambah_transaksi` (lihat `model.py`)
- Antarmuka sederhana dengan ikon dan tema profesional

---

## 🎯 Tujuan
- Melatih konsep pemrograman GUI menggunakan PyQt6
- Menyediakan aplikasi edukatif untuk simulasi transaksi digital
- Membuat aplikasi dengan antarmuka yang mudah digunakan dan jelas

---

## ⚙️ Teknologi yang Digunakan
- **Python 3.x**
- **PyQt6** (GUI Framework)
- **Supabase** (opsional, untuk backend transaksi)
- **GitHub** (version control & repository hosting)

---

## 🚀 Cara Instalasi & Menjalankan
1. Clone repositori:
   ```bash
   git clone https://github.com/raiss444/Aplikasi-Simulasi-Top-Up-Diamond-Mobile-Legends.git
   cd Aplikasi-Simulasi-Top-Up-Diamond-Mobile-Legends
   
2.Install dependencies: 
pip install -r requirements.txt

3.Pastikan file ikon (mlbb.png, diamond.png, dana.png, ovo.png, gopay.png, dll.) ada di folder resources/.

4.Jalankan Aplikasi:
python main.py

🗄️ Database

Aplikasi ini menggunakan Supabase sebagai backend database untuk menyimpan data transaksi top-up diamond.

📌 Nama Tabel: transaksi_topup

📋 Struktur Kolom:

🆔 user_id → Menyimpan User ID Mobile Legends

💎 diamond → Jumlah diamond yang dibeli

📦 paket → Nama paket diamond

💰 harga → Harga transaksi

💳 metode → Metode pembayaran (Dana, OVO, GoPay, QRIS)

📅 tanggal → Tanggal transaksi

📊 Data pada tabel ini digunakan untuk:

Menyimpan riwayat transaksi

Menampilkan laporan transaksi

Evaluasi hasil simulasi top-up

📂 Link Google Drive
Untuk file tambahan (video presentasi, build aplikasi .exe, dan dokumen pendukung), link : https://drive.google.com/file/d/1NYYV2VDIVG2hWivoIpQgCqyAMVcvRLGD/view?usp=drive_link

🔗 Google Drive - Aplikasi Simulasi Top Up Diamond Mobile Legends (drive.google.com in Bing)

📸 Tampilan Aplikasi
Form input User ID dengan validasi format

Pilihan paket diamond dengan harga diskon

Popup checkout interaktif

Ikon metode pembayaran (Dana, Ovo, Gopay, Qris)

🎥 Video Presentasi
Link video presentasi: YouTube(https://youtu.be/RFpUxm6yM18)

👨‍💻 Kontributor
Rais Asa Madani – Teknik Informatika
