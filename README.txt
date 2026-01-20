NAMA APLIKASI
Aplikasi Store Digital Top Up Diamond Game

DESKRIPSI
Aplikasi ini merupakan simulasi store digital top up diamond game
seperti Codashop. Konsumen dapat memilih paket diamond, memasukkan
ID Player, memilih metode pembayaran, dan menyimpan transaksi.

Aplikasi ini dibuat untuk keperluan Final Project / UAS
dan tidak terhubung dengan sistem pembayaran atau server game asli.

TEKNOLOGI YANG DIGUNAKAN
- Python
- PyQt6 (GUI Desktop)
- Supabase (Database Cloud)

FITUR APLIKASI
- Store paket diamond (harga ditentukan sistem)
- Input ID Player
- Pilih metode pembayaran
- Simpan transaksi ke database Supabase
- Lihat dan hapus riwayat transaksi

STRUKTUR FILE
- main.py        : Tampilan dan alur aplikasi (View)
- controller.py  : Logika dan validasi input (Controller)
- model.py       : Koneksi dan CRUD database Supabase (Model)
- utils.py       : Fungsi pendukung
- requirements.txt : Daftar library

CARA MENJALANKAN
1. Install library:
   pip install -r requirements.txt
2. Jalankan aplikasi:
   python main.py

CATATAN
Aplikasi ini bersifat simulasi untuk pembelajaran.
