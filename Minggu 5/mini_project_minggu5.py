# Program Absensi Mahasiswa menggunakan OOP, datetime, dan file handling

import datetime


class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def absen(self):
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.nama} ({self.nim}) hadir pada {waktu}"


# List untuk menyimpan daftar absensi
absensi = []

jumlah = int(input("Masukkan jumlah mahasiswa yang hadir: "))

for i in range(jumlah):
    print(f"\nMahasiswa ke-{i+1}")
    nama = input("Nama: ")
    nim = input("NIM: ")

    mhs = Mahasiswa(nama, nim)
    absensi.append(mhs.absen())

# Simpan absensi ke file
with open("absensi.txt", "w") as file:
    for data in absensi:
        file.write(data + "\n")

print("\nData absensi berhasil disimpan ke 'absensi.txt'.")


"""
📘 **Penjelasan:**

* Program menggunakan class `Mahasiswa` untuk menyimpan data.
* `datetime` digunakan untuk mencatat waktu kehadiran.
* Data absensi disimpan ke file `absensi.txt`.
"""
