# Penjadwal Aktivitas

## Deskripsi Singkat
Penjadwal Aktivitas adalah aplikasi *desktop* berbasis Python yang dirancang untuk membantu pengguna mengelola jadwal kegiatan sehari-hari. Aplikasi ini menerapkan arsitektur *Separation of Concerns* (SoC) dengan memisahkan antarmuka (UI), logika database, dan tampilan (*styling*).

## Fitur Utama
- **CRUD Operasi**: Menambah, melihat, dan menghapus jadwal.
- **Database Presisten**: Data tersimpan dengan aman menggunakan SQLite (`penjadwal.db`).
- **Desain Eksternal**: Tampilan dipercantik dengan file eksternal `style.qss`.
- **Form Terpisah**: Input data lebih fokus menggunakan dialog (`QDialog`).

## Teknologi yang Digunakan
- **Bahasa Pemrograman**: Python 3.x
- **GUI Framework**: PySide6
- **Database**: SQLite3

## Cara Menjalankan Aplikasi
1. Pastikan Python sudah terinstal di sistem Anda.
2. Buka terminal atau command prompt, arahkan ke direktori proyek ini.
3. Instal library PySide6 (jika belum ada) dengan menjalankan:
   ```bash
   pip install PySide6