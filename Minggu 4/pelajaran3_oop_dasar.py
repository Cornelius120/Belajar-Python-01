# OOP (Object-Oriented Programming) membantu mengorganisasi kode menjadi objek dan class


# Membuat class Mahasiswa
class Mahasiswa:
    # Konstruktor (__init__) dijalankan saat objek dibuat
    def __init__(self, nama, jurusan, ipk):
        self.nama = nama  # atribut nama
        self.jurusan = jurusan  # atribut jurusan
        self.ipk = ipk  # atribut ipk

    # Method untuk menampilkan data
    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Jurusan: {self.jurusan}")
        print(f"IPK: {self.ipk}")

    # Method tambahan untuk menentukan status kelulusan
    def cek_kelulusan(self):
        if self.ipk >= 3.0:
            print("Status: Lulus")
        else:
            print("Status: Belum Lulus")


# Membuat objek dari class Mahasiswa
mhs1 = Mahasiswa("Miyamura", "Informatika", 3.8)

# Memanggil method
mhs1.tampilkan_info()
mhs1.cek_kelulusan()


"""
📘 **Penjelasan:**

* `class` adalah template untuk membuat objek.
* `__init__` disebut konstruktor, otomatis dijalankan saat objek dibuat.
* `self` mewakili objek itu sendiri.
* `method` = fungsi di dalam class.
"""
