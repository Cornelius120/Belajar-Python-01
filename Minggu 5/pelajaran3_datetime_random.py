# Modul datetime digunakan untuk bekerja dengan tanggal dan waktu
# Modul random digunakan untuk menghasilkan nilai acak

import datetime
import random

# Menampilkan waktu saat ini
waktu_sekarang = datetime.datetime.now()
print("Waktu saat ini:", waktu_sekarang)

# Membuat tanggal tertentu
tanggal_ulang_tahun = datetime.date(2025, 12, 25)
print("Tanggal Ulang Tahun:", tanggal_ulang_tahun)

# Menggunakan modul random
angka_acak = random.randint(1, 100)  # menghasilkan angka acak antara 1–100
print("Angka acak:", angka_acak)

# Pilihan acak dari list
buah = ["apel", "jeruk", "mangga", "pisang"]
print("Buah pilihan acak:", random.choice(buah))


"""
📘 **Penjelasan:**

* `datetime.now()` untuk waktu saat ini.
* `random.randint(a, b)` menghasilkan angka acak dari a sampai b.
* `random.choice()` memilih elemen acak dari list.
"""
