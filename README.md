# Pertemuan 05 Perulangan Python

Nama: Nayla Solahiyah
NIM: 2225250045
Kelas: 3A

## Tujuan
Menggunakan for dan while untuk menyelesaikan masalah iteratif.

## Cara Menjalankan
python3 kuis/kuis2_deret_aritmetika.py

## Algoritma Kuis 2
1. Masukkan nilai a, d, dan n.
2. Cek nilai n. Kalau n kurang dari atau sama dengan 0, masukkan lagi sampai benar.
3. Atur nilai total menjadi 0.
4. Ulangi perhitungan sebanyak n kali.
5. Hitung nilai setiap suku dan tampilkan hasilnya.
6. Tambahkan setiap suku ke total.
7. Setelah selesai, tampilkan jumlah semua suku.

## Hasil Pengujian
| Input (a, d, n) | Keluaran yang Diharapkan | Keluaran Aktual | Status |
|---|---|---|---|
| 2, 3, 5 | Suku: 2, 5, 8, 11, 14; Jumlah: 40.00 | Suku: 2.00, 5.00, 8.00, 11.00, 14.00; Jumlah: 40.00 | Lulus |
| 10, -2, 4 | Suku: 10, 8, 6, 4; Jumlah: 28.00 | Suku: 10.00, 8.00, 6.00, 4.00; Jumlah: 28.00 | Lulus |
| 1.5, 0.5, 3 | Suku: 1.5, 2.0, 2.5; Jumlah: 6.00 | Suku: 1.50, 2.00, 2.50; Jumlah: 6.00 | Lulus |

## Refleksi
Kesalahan yang perlu diperhatikan adalah meletakkan `total = 0` di dalam perulangan. Kalau diletakkan di dalam loop, nilai total akan kembali menjadi 0 setiap kali perulangan berjalan. Jadi, `total = 0` harus diletakkan sebelum perulangan, sedangkan penjumlahan setiap suku dilakukan di dalam perulangan.

## Referensi
- RPS Algoritma dan Pemrograman OBE Untirta. Dokumen Program Studi S1 Pendidikan Matematika, Tahun Ajaran 2026/2027 Ganjil.
- Python Software Foundation. Python 3 Documentation: Control Flow Tools.
- Visual Studio Code Documentation: Python in Visual Studio Code.
- GitHub Docs: Creating a New Repository dan Adding Locally Hosted Code to GitHub.
- Downey, A. B. (2015). Think Python: How to Think Like a Computer Scientist, 2nd ed.