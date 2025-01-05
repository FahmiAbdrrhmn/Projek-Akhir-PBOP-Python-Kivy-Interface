# Projek Akhir PBOP - Sistem Manajemen Reservasi Hotel

## Deskripsi Proyek
Proyek ini bertujuan untuk mengembangkan sistem manajemen reservasi hotel menggunakan Python, Kivy untuk antarmuka pengguna, dan PostgreSQL untuk database. Sistem ini memungkinkan pengguna untuk mengelola data tamu, kamar, dan reservasi, serta mengekspor data ke file Excel.

## Fitur Utama
- **Manajemen Data Tamu**: Menambahkan, memperbarui, dan menghapus data tamu hotel.
- **Manajemen Data Kamar**: Menambahkan, memperbarui, dan menghapus data kamar hotel.
- **Manajemen Data Reservasi**: Menambahkan dan menghapus reservasi hotel yang dibuat oleh tamu.
- **Ekspor Data ke Excel**: Ekspor data kamar, tamu, dan reservasi ke file Excel untuk analisis lebih lanjut.

## Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama untuk aplikasi.
- **Kivy**: Framework untuk membangun antarmuka pengguna (UI) aplikasi desktop.
- **PostgreSQL**: Sistem manajemen basis data yang digunakan untuk menyimpan data tamu, kamar, dan reservasi.
- **openpyxl**: Untuk mengekspor data ke file Excel.
- **psycopg2**: Untuk menghubungkan aplikasi Python dengan database PostgreSQL.

## Instalasi

### Persyaratan
Pastikan Anda memiliki hal-hal berikut sebelum memulai:
1. **Python** (versi 3.x) terinstal di sistem Anda.
2. **PostgreSQL** sudah terinstal dan dikonfigurasi di sistem Anda.
3. **Kivy**: Framework untuk membangun antarmuka aplikasi.
4. **openpyxl** dan **psycopg2**: Library untuk mengekspor data ke Excel dan berinteraksi dengan database PostgreSQL.

### Langkah-Langkah Instalasi

**Venv dan Install Requirements**:
```shell
python -m venv myenv
myenv\scripts\activate.bat
pip install -r requirements.txt
```

## Lisensi
MIT License

Copyright (c) [2024] [Fahmi Abdurrahman]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
